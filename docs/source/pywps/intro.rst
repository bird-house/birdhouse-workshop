.. _pywps_intro:

Introduction
============

In the following we describe WPS in general and `PyWPS`_.

What is WPS?
------------

Web Processing Service (WPS) is part of the OWS standards defined by OGC,
while WFS, WMS, WCS, SOS are used for transfer of data (upload, download, transformation?),
WPS is used for data processing on the server (All processing is done on server side).

WPS provides a standard interface for input, output, process discovery and execution.
WPS is normally used for geospatial data to run spatial processes.

.. figure:: ../_static/wps_adamsteer.png

    Taken from: http://pointclouds.nci.org.au/talks/f4g_pointwps_adamsteer.pdf


What is PyWPS?
--------------

`PyWPS`_ is a WPS implementation written in the Python language.
The current version is 4.0.0.

* Server (HTTP-WSGI)
* OGC WPS implementation
* Python 3 support
* Based on a webframework (werkzeug)
* Native WSGI itegration (Better server integration)
* MIT license (can be used in comercial projects)

PyWPS has been used in multiple projects concerning geospatial data processing:

* `List of scientifical publications <http://pywps.org/science/>`_
* `PyWPS gallery <http://pywps.org/gallery/>`_

A brief introdution to WPS
--------------------------

WPS is part of the OGC service suit (OWS) and some operations are common to other
services (e.g. **GetCapabilities**), but others specific to WPS itself.

WPS requests:

* **GetCapabilities**
* **DescribeProcess**
* **Execute**

**GetCapabilities**
  this request provides a list of available services.

**DescribeProcess**
  describes a process indicating the inputs and outputs required by the process
  to execute and/or for metadata information.

**Execute**
  this request will accept inputs/outputs, processing conditions (async/sync)
  and will run the process on the server.


WPS async/sync
##############

Some processes are time consuming, so it is better to start the process and
later query the server for its status or output. This is refered as a async execute request

If you are confident that the process being executed is fast you can request a sync execution
where the client waits for the immeditely reply from server withoutput (no need to pull the output later).


WPS input/output
################

WPS has 3 sorts of data I/O:

* **Literal**
* **ComplexData**
* **BoundingBox**

The **Literal** is any number (float, int) and string.
**ComplexData** is geospatial data in multiple formats (mimetype, e.g: ``application/gml+xml``)
that can be integrated into the WPS request/response, when using vectorial data
this one is transformed into XML and raster binary data coded into base64
(binary coding using ascii symbols).

WPS versions
------------

WPS 1.0.0 was released in 2007, the new WPS 2.0.0 was released in 2015.
So far major implementations have only used WPS 1.0.0.

WPS 1.0.0 can start processes, but there is no way to stop them before the process
reaches its conclusion... it is like a car without brakes. But not all is bad.
New WPS 2.0.0 allows for processes to be cancelled.

Links
-----

* `PyWPS`_
* `PyWPS Workshop <https://github.com/PyWPS/pywps-workshop>`_


.. _PyWPS: http://pywps.org/
