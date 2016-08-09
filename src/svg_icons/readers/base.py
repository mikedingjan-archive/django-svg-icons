import json

from django.conf import settings


class SVGReaderError(Exception):
    pass


class BaseReader(object):
    """Base reader class not for direct use

    Subclass this to have your own implementation, the class
    to use can be defined in the settings with

        SVG_ICONS_READER_CLASS

    """

    def __init__(self):
        self.source_file = getattr(settings, 'SVG_ICONS_SOURCE_FILE')
        if not self.source_file:
            raise SVGReaderError(
                "SVG_ICONS_SOURCE_FILE needs to be defined for icons to work.")
        self.svg_path_data = self.read_source_file()

    def read_source_file(self):
        """Read the source file in memory

        Implement this when subclassing the Reader to
        have it read the preferred format, the implementation
        should return a dict with the icon name as key
        and the svg path as a list data as value.

        ..:example::
            {
                'icon1': [
                    "M365.339 474.828c-19.319-12.616-42.222-18.062.....",
                    "M365.339 474.828c-19.319-12.616-42.222-18.062.....",
                },
                'icon2': [
                    "M365.339 474.828c-19.319-12.616-42.222-18.062.....",
                },
            }

        """
        raise NotImplementedError

    def get_svg_paths(self, icon_name):
        """Return the path data of the requested icon."""
        path_data = self.svg_path_data.get(icon_name)
        if not path_data:
            raise SVGReaderError(
                "No path data found for icon {}".format(icon_name))
        return path_data
