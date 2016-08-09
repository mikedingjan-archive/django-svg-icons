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


@register.inclusion_tag('svg_icons/icon.html')
def icon(name, **kwargs):
    """Render the SVG icon paths returned by the
    icon reader in the template.

    """
    width = kwargs.get('width', settings.SVG_ICONS_DEFAULT_WIDTH)
    height = kwargs.get('height', settings.SVG_ICONS_DEFAULT_HEIGHT)
    return {
        'width': kwargs.get('size', width),
        'height': kwargs.get('size', height),
        'className': kwargs.get('className'),
        'paths': icons.get_svg_paths(name),
    }
