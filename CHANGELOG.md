0.1.1 (09-08-2016)
==================

 - Removed caching in favor of loading the JSON file on runtime
 - Created a BaseReader class which can be subclassed to any format
 - Implemented a Icomoon reader class [Icomoon website](http://icomoon.io)
 - Introduced `SVG_ICONS_READER_CLASS` setting to override the reader class
   defaults to:  `svg_icons.readers.icomoon.IcomoonReader`

 Bug fixes
 ---------
 - Fixed the default width and height settings


0.1.0 (09-08-2016)
==================

 - Initial django-svg-icons package
