import json
from importlib import import_module

from django.core.cache import cache
from django.conf import settings
from django.template import Library, TemplateSyntaxError

reader_class = getattr(settings, 'SVG_ICONS_READER_CLASS', 'svg_icons.readers.icomoon.IcomoonReader')

try:
    module, cls = reader_class.rsplit('.', 1)
    module = import_module(module)
    Reader = getattr(module, cls)
except ImportError:
    raise ValueError("No valid icon reader class found.")

register = Library()
icons = Reader()

default_width = getattr(settings, 'SVG_ICONS_DEFAULT_WIDTH', 22)
default_height = getattr(settings, 'SVG_ICONS_DEFAULT_HEIGHT', 22)


@register.inclusion_tag('svg_icons/icon.html')
def icon(name, **kwargs):
    """Render the SVG icon paths returned by the
    icon reader in the template.

    """
    width = kwargs.get('width', default_width)
    height = kwargs.get('height', default_height)
    return {
        'width': kwargs.get('size', width),
        'height': kwargs.get('size', height),
        'className': kwargs.get('className'),
        'paths': icons.get_svg_paths(name),
    }
