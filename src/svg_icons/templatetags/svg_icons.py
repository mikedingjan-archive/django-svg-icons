import json

from django.core.cache import cache
from django.conf import settings
from django.template import Library, TemplateSyntaxError

register = Library()


@register.inclusion_tag('svg_icons/icon.html')
def icon(name, **kwargs):
    """Render a SVG icon defined in a json file to our template.

    ..:json example (stripped)::
        {
          "icons": [
            {
              "icon": {
                "paths": [
                  "M365.339 474.828c-19.319-12.616-42.222-18.062....."
                ]
              },
              "properties": {
                "name": "tools"
              }
            }
          ]
        }

    """
    cache_key = ':'.join([
        getattr(settings, 'SVG_ICONS_CACHE_KEY_PREFIX', 'svg-icons'), name])
    icon_paths = cache.get(cache_key)
    if not icon_paths:
        source_file = getattr(settings, 'SVG_ICONS_SOURCE_FILE', False)
        if not source_file:
            raise ValueError("SVG_ICONS_SOURCE_FILE needs to be set")

        data = json.load(open(source_file, 'r'))
        for icon_data in data['icons']:
            if name != icon_data['properties']['name']:
                continue
            icon_paths = icon_data['icon']['paths']

        if not icon_paths:
            raise TemplateSyntaxError("Requested icon does not exist")

        cache.set(cache_key, icon_paths)

    width = kwargs.get('width', settings.SVG_ICONS_DEFAULT_WIDTH)
    height = kwargs.get('height', settings.SVG_ICONS_DEFAULT_HEIGHT)
    return {
        'width': kwargs.get('size', width),
        'height': kwargs.get('size', height),
        'className': kwargs.get('className'),
        'paths': icon_paths,
    }
