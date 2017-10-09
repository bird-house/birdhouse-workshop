.. _pywps_installation:

Installation
============

Requirements
------------

See :ref:`prepare`.

Activate the conda workshop enviroment:

.. code-block:: bash

    $ source activate workshop

Aim
---

We are going to install *PyWPS* and run some example processes.

Objectives:

* You will learn how to install `PyWPS`_, start a WPS service and execute a process.


Install PyWPS
-------------

You can install PyWPS via conda.
Make sure you install PyWPS from the *birdhouse* conda channel. We also need the
*conda-forge* channel, and the channels must be provided in the displayed order
(channel priority):

.. code-block:: bash

    $ conda install -c birdhouse -c conda-forge pywps gdal

Let's see if this has worked:

.. code-block:: bash

    $ python -c "import pywps"

This bash command will load the pywps library and close the console.
If the install was properly done *no error messages* will appear.

Start the demo WPS service
--------------------------

This workshop includes a demo service with some example processes. Let's try them.

Start the service by running the following command:

.. code-block:: bash

    # change to workshop root folder
    $ cd ~/birdhouse-workshop/
    # start demo service
    $ python demo/demo.py

If everything went well you should have a console output as follows:

.. code-block:: bash

  Configuration file(s) ['demo/default.cfg'] loaded
  starting WPS service on http://localhost:5000/wps
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

.. warning::
  If you need to start the service on a different port then 5000, you must edit
  the port in the PyWPS configuration ``demo/default.cfg``::

    [server]
    url = http://localhost:5001/wps
    outputurl = http://localhost:5001/outputs

Service check
-------------

To test the service, open your internet browser to this address: http://127.0.0.1:5000/wps.

Alternatively, you can also try ``curl``:

.. code-block:: bash

  $ curl "http://127.0.0.1:5000/wps"

You will get an XML exception report by the PyWPS service:

.. code-block:: xml

  <?xml version="1.0" encoding="UTF-8"?>
  <!-- PyWPS 4.0.0 -->
  <ows:ExceptionReport xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/ows/1.1 http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd" version="1.0.0">
    <ows:Exception exceptionCode="MissingParameterValue" locator="service" >
      <ows:ExceptionText>service</ows:ExceptionText>
    </ows:Exception>
  </ows:ExceptionReport>

The good thing ... the service is running and talking to you :)

Test PyWPS
----------

Test the WPS service itself using a **GetCapabilities** request;
insert this address in your browser:

http://127.0.0.1:5000/wps?service=WPS&request=GetCapabilities

.. code-block:: bash

  $ curl "http://127.0.0.1:5000/wps?service=WPS&request=GetCapabilities"

In the **GetCapabilities** XML document notice the following:

* Abstract describing service
* Service provider
* Process Offerings (Title, Abstract, Metadata)

Say hello
---------

We can run now our first process.
The **GetCapabilities** XML document tells us that this WPS serivce has a process with identifier ``say_hello``.
Please find this description in the document. It should look like this:

.. code-block:: xml
   :emphasize-lines: 2

    <wps:Process wps:processVersion="1.3.2">
      <ows:Identifier>say_hello</ows:Identifier>
      <ows:Title>Process Say Hello</ows:Title>
    </wps:Process>

Now, we need some more details about this process. Therefore we do a **DescribeProcess** request;
insert this address in your browser:

http://127.0.0.1:5000/wps?service=WPS&request=DescribeProcess&version=1.0.0&identifier=say_hello

.. code-block:: bash

  $ curl "http://127.0.0.1:5000/wps?service=WPS&request=DescribeProcess&version=1.0.0&identifier=say_hello"

The resulting XML document tells us something about the *input* and *output* parameters,
for example there is an input parameter ``name``:

.. code-block:: xml
   :emphasize-lines: 2

      <Input minOccurs="1" maxOccurs="1">
        <ows:Identifier>name</ows:Identifier>
        <ows:Title>Input name</ows:Title>
        <LiteralData>
          <ows:DataType ows:reference="urn:ogc:def:dataType:OGC:1.1:string">string</ows:DataType>
          <ows:AnyValue/>
        </LiteralData>
      </Input>

Let us now execute the ``say_hello`` process with an input parameter ``name`` *Birdy*:

http://127.0.0.1:5000/wps?service=WPS&request=Execute&version=1.0.0&identifier=say_hello&DataInputs=name=Birdy

.. code-block:: bash

  $ curl "http://127.0.0.1:5000/wps?service=WPS&request=Execute&version=1.0.0&identifier=say_hello&DataInputs=name=Birdy"

If all went well, you get an output parameter with the value *Hello Birdy*:

.. code-block:: xml
   :emphasize-lines: 6

    <wps:ProcessOutputs>
      <wps:Output>
        <ows:Identifier>response</ows:Identifier>
        <ows:Title>Output response</ows:Title>
        <wps:Data>
          <wps:LiteralData dataType="urn:ogc:def:dataType:OGC:1.1:string" uom="urn:ogc:def:uom:OGC:1.0:unity">Hello Birdy</wps:LiteralData>
        </wps:Data>
      </wps:Output>
    </wps:ProcessOutputs>


Exercise 1
----------

Try the ``say_hello`` again with some other input values.

Exercise 2
----------

Before you fall into *sleep* ... let's do another exercise.
Our service has another process. Which one is it?

Please find it and run an execute request ... you need to know the input parameters.

Links
-----

* `PyWPS Flask Demo <http://pywps-demo.readthedocs.io/en/latest/>`_

.. _PyWPS: http://pywps.org/
