from django import template
from django.shortcuts import get_object_or_404
from ..models import Carousel
from ..settings import IMAGE_WIDTH, IMAGE_HEIGHT, NAVIGATION, MENU_ENTRIES


register = template.Library()


@register.inclusion_tag('_carousel.html')
def carousel(carousel_name=None):
    carousel = get_object_or_404(Carousel, carousel_name=carousel_name)
    return {
        'carousel': carousel,
        'width': IMAGE_WIDTH,
        'height': IMAGE_HEIGHT,
        'text_box_width': IMAGE_WIDTH * 0.9,
        'navigation': NAVIGATION,
        'menu_entries': MENU_ENTRIES,
    }
