from django.contrib import admin
from hvad.admin import TranslatableAdmin
from .models import Carousel, CarouselEntry
from image_cropping import ImageCroppingMixin


class CarouselEntryAdmin(ImageCroppingMixin, TranslatableAdmin):
    list_display = ('navigation_entry_translated',
                    'order',
                    'text_over_image_translated',
                    'image_display_in_admin')

    class Meta:
        model = CarouselEntry


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', )
    fields = ('carousel_name', 'carousel_entries')


admin.site.register(CarouselEntry, CarouselEntryAdmin)
admin.site.register(Carousel, CarouselAdmin)
