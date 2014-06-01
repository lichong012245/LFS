from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.files import get_thumbnailer
from hvad.models import TranslatableModel, TranslatedFields
from hvad.manager import TranslationManager
from image_cropping import ImageRatioField, ImageCropField
from paintstore.fields import ColorPickerField

from .settings import IMAGE_WIDTH, IMAGE_HEIGHT


class Carousel(models.Model):
    carousel_name = models.CharField(_('carousel name'), max_length=255)
    carousel_entries = models.ManyToManyField('CarouselEntry', related_name='carousel', blank=True)

    def __unicode__(self):
        return unicode(self.carousel_name)


class CarouselEntryManager(TranslationManager):
    pass


class CarouselEntry(TranslatableModel):
    translations = TranslatedFields(
        text_over_image=models.CharField(_('image text'), max_length=255),
        navigation_entry=models.CharField(_('navigation entry'), max_length=30),
    )

    image = ImageCropField(_('image'), upload_to='carousel')
    cropped = ImageRatioField(
        'image', '{0}x{1}'.format(IMAGE_WIDTH, IMAGE_HEIGHT), size_warning=True)
    order = models.PositiveIntegerField(unique=True)
    text_background_color = ColorPickerField(blank=True)

    objects = CarouselEntryManager()

    def __unicode__(self):
        return self.navigation_entry_translated()

    def text_over_image_translated(self):
        try:
            return self.text_over_image
        except:
            return self.translations.all()[0].text_over_image
    text_over_image_translated.short_description = 'Image Text'

    def navigation_entry_translated(self):
        try:
            return self.navigation_entry
        except:
            return self.translations.all()[0].navigation_entry
    navigation_entry_translated.short_description = 'Navigation Text'

    def cropped_img_url(self):
        return get_thumbnailer(self.image).get_thumbnail({
            'size': (IMAGE_WIDTH, IMAGE_HEIGHT),
            'box': self.cropped,
            'crop': True,
            'detail': True,
        }).url

    def image_display_in_admin(self):
        return "<a href='{0}'><img src='{0}' width='{1}' height='{2}'></a>".format(
            self.cropped_img_url(),
            IMAGE_WIDTH / 3,
            IMAGE_HEIGHT / 3)
    image_display_in_admin.allow_tags = True
    image_display_in_admin.short_description = 'Image Preview'

    def carousel_entry_id(self):
        return 'entry{}'.format(self.order)

    class Meta:
        verbose_name_plural = _('carousel entries')
        ordering = ('order', )
