:tocdepth: 2

#############################
Settings for Django SVG Icons
#############################

Django SVG Icons is customizable to your needs by implementing a few settings
in your own django project.


Source file
===========

This one is required and shoud point to your SVG paths source file.

.. code-block:: python

    SVG_ICONS_SOURCE_FILE = '/path/to/file.json'


Reader class
============

Use this to implement a other format than the default ``Icomoon`` reader.

.. code-block:: python

    SVG_ICONS_READER_CLASS = 'svg_icons.readers.icomoon.IcomoonReader'

Availble reader classes are

 - Icomoon ``svg_icons.readers.icomoon.IcomoonReader``


Icon Dimensions
===============

Default dimensions can be defined, this setting is not required and will
have a default value of 22

.. code-block:: python

    SVG_ICONS_DEFAULT_WIDTH = 22
    SVG_ICONS_DEFAULT_HEIGHT = 22
