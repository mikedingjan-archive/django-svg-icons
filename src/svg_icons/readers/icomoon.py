import json
import logging

from svg_icons.readers.base import BaseReader

logger = logging.getLogger(__name__)


class IcomoonReader(BaseReader):

    def read_source_file(self):
        """Read Icomoon format into memory.

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
        items = {}
        data = json.load(open(self.source_file, 'r'))
        for icon in data['icons']:
            props, icon_data = icon.get('properties'), icon.get('icon')
            if not props or not icon_data:
                logger.warning("Invalid Icomoon format for: {}".format(icon))
                continue
            items[props['name']] = icon_data['paths']
        return items
