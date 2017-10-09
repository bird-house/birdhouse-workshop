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

    $ wget -q -O caps.xml \
      "http://127.0.0.1:5000/wps?service=WPS&request=GetCapabilities"

Important question: Why ``-q``, ``-O`` and ``"`` in the comnand:

``-q``
  quit verbose information about requests.
``-O``
  Output to file. You can use ``-``, and the content will be dumped into the prompt.
``"``
  Otherwise wget would not consider ``&`` as part of the URL and would cut it.

curl
----

Similar to *wget* you can also use *curl* to retrieve the *GetCapabilities* XML document:

.. code-block:: bash

  $ curl -s -o caps.xml \
    "http://127.0.0.1:5000/wps?service=WPS&request=GetCapabilities"

``-s``
    silent mode ... no progress bar.
``-o``
  Output to file. You can use ``-``, and the content will be dumped into the prompt.

RESTClient (Firefox only)
-------------------------

You can use the `RestClient`_ Firefox plugin to run requests.

Here is an example with a **GetCapabilities** request using HTTP method **GET**:

.. image:: ../_static/rest-client-get.png

XML HTTP Post Request
---------------------

As requests and data become more structure and lengthy, concatenating all
parameters into a URL for a GET type request becomes difficult or impossible.
For this reason the WPS standard allows the definition of requests as XML documents
sent to the server using the POST method of the HTTP protocol.

Here is an example with an **Execute** request using HTTP method **POST**:

.. image:: ../_static/rest-client-post.png

It is using the
`XML description <https://github.com/bird-house/birdhouse-workshop/blob/master/tutorials/11_pywps_testing/execute_req.xml>`_
of the **Execute** request.

It is also possible to use curl (or wget) for POST requests:

.. code-block:: bash

  $ curl -H "Content-Type: text/xml" -X POST \
    -d@execute_req.xml http://localhost:5000/wps

``-d@``
  pass data from the given filename (XML payload)

``-X``
  HTTP method, GET or POST

``-H``
  Header variable, in our case we set the Content-Type.

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

.. code-block:: bash

  $ curl "http://127.0.0.1:5000/wps?service=WPS&request=DescribeProcess"

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


Exercise 1
----------

Try ``wget`` or ``curl`` with some of the previous *DescribeProcess* and *Execute* requests.

Exercise 2
----------

Run the **POST** request using the prepared XML payload.

Change into the tutorial ``processes`` folder:

.. code-block:: bash

  $ cd ~/birdhouse-workshop/tutorials/11_pywps_testing

Make sure no WPS service is running ... stop it with ``CTRL-c``.

Start the demo service:

.. code-block:: bash

    $ python ../../demo/demo.py

Use the above ``curl`` command with the payload ``execute_req.xml``, which you can find in this folder.
Modify the input parameters of the payload.

.. note::
  There is another POST request example in the
  `point-clouds talk by NCI <http://pointclouds.nci.org.au/talks/f4g_pointwps_adamsteer.pdf>`_.

Links
-----

* `RestClient <http://restclient.net/>`_
* `Poster on Chrome <https://chrome.google.com/webstore/detail/chrome-poster/cdjfedloinmbppobahmonnjigpmlajcd>`_
* `PyWPS workshop <https://github.com/PyWPS/pywps-workshop/blob/master/03-Testing.md>`_
* `Geoprocessing Info <http://geoprocessing.info/wpsdoc/1x0ExecutePOST>`_
* `WPS Tutorial <http://wiki.ieee-earth.org/Documents/GEOSS_Tutorials/GEOSS_Provider_Tutorials/Web_Processing_Service_Tutorial_for_GEOSS_Providers/Section_2%3a_Introduction_to_WPS>`_
