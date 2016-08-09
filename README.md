Django SVG Icons
================

Simple django templatetag to display `SVG` icons in your django application.
Icon paths will loaded from a provided `JSON` file, formatted according the icomoon format.

More info: [Icomoon website](http://icomoon.io/)


Installation
------------

Installation from pypi via pip

    pip install django-svg-icons


Configuration
-------------

In your django project add `svg_icons` to your installed apps and set the `SVG_ICONS_SOURCE_FILE` setting to your source file.

    INSTALLED_APPS = [
        # ...
        'svg_icons',
    ]

    SVG_ICONS_SOURCE_FILE = '/path/to/source_file.json'

### Settings

Configuration and defaults of the templatetag are defined in django settings.

#### SVG_ICONS_READER_CLASS
_default: `svg_icons.readers.icomoon.IcomoonReader`_<br/>
Reader class to load the SVG data file and serve the right icon data

#### SVG_ICONS_SOURCE_FILE
Location of the (icomoon formatted) source file which contains the paths of all `svgs`

#### SVG_ICONS_DEFAULT_WIDTH
_default: 22_<br/>
Default width which gets set when no width or size is provided.

#### SVG_ICONS_DEFAULT_HEIGHT
_default: 22_<br/>
Default height which gets set when no height or size is provided.


Usage
-----

In your templates you can load the templatetag and start including your icons.

    {% load svg_icons %}
    {% icon 'icon_name' %}

The templatetag accepts some kwargs for icon configuration as well.

 - **size** for setting both width and height
 - **width** for only setting a specific width
 - **height** for only setting a specific height
 - **className** css classnames applied on the `<svg>` object

All kwargs are optional, when not provided the deaults are used.

    {% icon 'icon_name' size=50 className="css classnames" %}


Todo
----

 - Write tests
