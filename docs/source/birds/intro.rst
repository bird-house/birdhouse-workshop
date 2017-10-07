.. _birds_intro:

Introduction
============

`Birdhouse`_ is a collection of `Web Processing Service`_ (WPS) related Python components
to support climate data analysis. Birdhouse uses OGC/WPS software from the
`GeoPython`_ project, like PyWPS and OWSLib.

The aim of Birdhouse is to support (climate science) projects to setup a Web Processing Service
infrastructure.

Birdhouse is the *Home* of several *Birds*, the components of the Birdhouse ecosystem.
There are birds for the Web Processing client side, to make the WPS service access more convenient
and also as an example for project own Web UIs. There are fully configured WPS services with
example processes, which run *out-of-the-box* and can be forked and used as template.
There is also a middleware component to control the access to WPS services.

The Birdhouse documentation gives an
`overview of the architecture <http://birdhouse.readthedocs.io/en/latest/overview.html>`_.

The Birdhouse components can be installed with a simple ``make install``.
See the `installation documentation <http://birdhouse.readthedocs.io/en/latest/installation.html>`_
for details.

All Birdhouse components are Open Source and released under the `Apache License`_.
The source code is available on `GitHub`_.



.. _Birdhouse: http://bird-house.github.io/
.. _Web Processing Service: http://opengeospatial.org/standards/wps
.. _GeoPython: https://geopython.github.io/
.. _Apache License: http://birdhouse.readthedocs.io/en/latest/license.html
.. _GitHub: https://github.com/bird-house
