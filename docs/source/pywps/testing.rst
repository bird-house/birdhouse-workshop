.. _pywps_testing:

Testing
=======

Requirements
------------

See :ref:`prepare`.

Activate the conda workshop enviroment:

.. code-block:: bash

    $ source activate workshop

Aim
---

As you develop more complex process and use more structured datasets,
using simply a web browser to test becomes impractical.
In this chapter you get acquainted with alternative tools to interact with a PyWPS instance.

Objectives:

* You will learn how to test a PyWPS process.

wget
----

Start by trying the *GetCapabilities* request:

.. code-block:: bash

    $ wget -q -O - "http://127.0.0.1:5000/wps?service=WPS&request=GetCapabilities"

Important question: Why ``-q``, ``-O -`` and ``"`` in the comnand:

``-q``
  quit verbose information about requests.
``-O -``
  Output to file, but since the file is ``-`` the content will be dumped into the prompt.
``"``
  Otherwise wget would not consider ``&`` as part of the URL and would cut it.

curl
----



XML Request using Poster
------------------------

As requests and data become more structure and lengthy, concatenating all
parameters into a URL for a GET type request becomes difficult or impossible.
For this reason the WPS standard allows the definition of requests as XML documents
sent to the server using the POST method of the HTTP protocol.

It is also possible to use wget (or curl) for POST requests but then the
command line because to extensive.

Poster is an add-on for various popular web browsers that allows the creation and execution of HTTP POST requests.

Works on Chromium:

https://chrome.google.com/webstore/detail/chrome-poster/cdjfedloinmbppobahmonnjigpmlajcd


Prepare GET and POST example.

http://geoprocessing.info/wpsdoc/1x0ExecutePOST
http://wiki.ieee-earth.org/Documents/GEOSS_Tutorials/GEOSS_Provider_Tutorials/Web_Processing_Service_Tutorial_for_GEOSS_Providers/Section_2%3a_Introduction_to_WPS


XML Request using RESTClient
----------------------------

Works only on Firefox:

http://restclient.net/

Prepare GET and POST example.


Exceptions
----------

*ExceptionReport* is an important feature of WPS. In WPS 1.0.0 we have the following exceptions:

**MissingParameterValue**
  The request does not include a parameter value or a default cannot be found.

**InvalidParameterValue**
  The request contains an invalid parameter value.

**NoApplicableCode**
  Generic exception, no other code could be applied.

**NotEnoughStorage**
  The server does not have enough space available.

Try the following request:

http://127.0.0.1:5000/wps?service=WPS&request=DescribeProcess

The exception is *MissingParameterValue*:

.. code-block:: xml

  <?xml version="1.0" encoding="UTF-8"?>
  <ows:ExceptionReport xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/ows/1.1 http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd" version="1.0.0">
  <ows:Exception exceptionCode="MissingParameterValue" locator="version" >
    <ows:ExceptionText>Missing version</ows:ExceptionText>
  </ows:Exception>
  </ows:ExceptionReport>

The *version* parameter is missing.

In case of Python errors in the called process, PyWPS will dump the Python stack into the *ExceptionReport*.


Exercise
--------

Try ``wget`` with some of the previouse *DescribeProcess* and *Execute* requests.

Links
-----

Notebooks, tutorials ...

https://github.com/PyWPS/pywps-workshop/blob/master/03-Testing.md
