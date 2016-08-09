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

In your django project add `svg_icons` to your installed apps

    INSTALLED_APPS = [
        # ...
        'svg_icons',
    ]

### Settings

Configuration and defaults of the templatetag are defined in django settings.

#### SVG_ICONS_CACHE_KEY_PREFIX
_default: svg-icons_<br/>
If enabled the found `SVG` paths can be cached and prefixed with this cache key prefix

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

The templatetag accepts some kwargs for icon configuration as well (all are optional).

 - **size** for setting both width and height
 - **width** for only setting a specific width
 - **height** for only setting a specific height
 - **className** css classnames applied on the `<svg>` object


    {% icon 'icon_name' size=50 className="css classnames" %}


Todo
----

 - Add support for other formats
 - Write tests
