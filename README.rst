Ren'Py Language for Liclipse
============================

This is a Ren'Py language for LiClipse, a lightweight extensible editor
for Eclipse. (For more information, visit http://brainwy.github.io/liclipse/)

To install Ren'Py support copy dist/renpy.liclipse into the liclipse
languages directory.

Regenerating
------------

After changing src/renpy.tmpl.liclipse, it's necessary to regenerate the
renpy.liclipse file.

To generate the file and install Ren'Py support, run:

    python build.py -l `path_to_liclipse`

Where `path_to_licipse` should be either the LiClipse install directory,
or the install directory of Eclipse with LiClipse installed.

To just generate renpy.liclipse, run::

    python build.py -o renpy.liclipse

