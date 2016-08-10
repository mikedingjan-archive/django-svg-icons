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
