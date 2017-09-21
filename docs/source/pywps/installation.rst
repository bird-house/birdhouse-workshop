.. _pywps_installation:

Installation
============

Requirements
------------

See :ref:`prepare`.

Activate the conda workshop enviroment::

    $ source activate workshop

Aim
---

We are going to install PyWPS and run a some example processes.

Objectives:

* You will learn how to install PyWPS and start a WPS service.


Install PyWPS
-------------

You can install PyWPS via conda.
Make sure you install PyWPS from the *birdhouse conda channel*::

    $ conda install -c birdhouse pywps

Let's see if this has worked::

    $ python -c "import pywps"

This bash command will load the pywps library and close the console.
If the install was properly done no error messages will appear.

Start the demo WPS service
--------------------------

This workshop includes a demo service with some example processes. Let's try them.

Start the service by issuing the following command::

    $ python demo/demo.py

If everything went well you should have a console output as follows::

  Configuration file(s) ['demo/default.cfg'] loaded
  starting WPS service on http://localhost:5000/wps
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Service check
-------------

To test the service open your internet browser to this address: http://127.0.0.1:5000/wps.

You will get an XML exception report by the PyWPS service::

  <?xml version="1.0" encoding="UTF-8"?>
  <!-- PyWPS 4.0.0 -->
  <ows:ExceptionReport xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/ows/1.1 http://schemas.opengis.net/ows/1.1.0/owsExceptionReport.xsd" version="1.0.0">
    <ows:Exception exceptionCode="MissingParameterValue" locator="service" >
      <ows:ExceptionText>service</ows:ExceptionText>
    </ows:Exception>
  </ows:ExceptionReport>

The good thing ... the service is talking to you :)

Test PyWPS
----------

Test the WPS service itself using a GetCapabilities request;
insert this address in your browser:
http://127.0.0.1:5000/wps?SERVICE=WPS&REQUEST=GetCapabilities

In the GetCapabilities XML document notice the following:

* Abstract describing service
* Service provider
* Process Offerings (Title, Abstract, Metadata)

Say hello
---------

We can run now our first process.
The GetCapabilities XML document tells us that this WPS serivce has a process with identifier ``say_hello``.
Please find this description in the document. It should look like this::

    <wps:Process wps:processVersion="1.3.2">
      <ows:Identifier>say_hello</ows:Identifier>
      <ows:Title>Process Say Hello</ows:Title>
    </wps:Process>

Now, we need some more details about this process. Therefore we do a DescribeProcess request;
insert this address in your browser:
http://127.0.0.1:5000/wps?SERVICE=WPS&REQUEST=DescribeProcess&VERSION=1.0.0&IDENTIFIER=say_hello

The resulting XML document tells us something about the input and output parameters,
for example there is a parameter ``name``::

      <Input minOccurs="1" maxOccurs="1">
        <ows:Identifier>name</ows:Identifier>
        <ows:Title>Input name</ows:Title>
        <LiteralData>
          <ows:DataType ows:reference="urn:ogc:def:dataType:OGC:1.1:string">string</ows:DataType>
          <ows:AnyValue/>
        </LiteralData>
      </Input>

Let us now execute a ``say_hello`` process with the ``name`` *Birdy*:
http://127.0.0.1:5000/wps?SERVICE=WPS&REQUEST=Execute&VERSION=1.0.0&IDENTIFIER=say_hello&DataInputs=name=Birdy

If all wents well, you get an output parameter with the value *Hello Birdy*::

  <wps:ProcessOutputs>
    <wps:Output>
      <ows:Identifier>response</ows:Identifier>
      <ows:Title>Output response</ows:Title>
      <wps:Data>
        <wps:LiteralData dataType="urn:ogc:def:dataType:OGC:1.1:string" uom="urn:ogc:def:uom:OGC:1.0:unity">Hello Birdy</wps:LiteralData>
      </wps:Data>
    </wps:Output>
  </wps:ProcessOutputs>


Excercise
---------

Your task is to implement a meaningful test for our ``simple_plot`` function.

Start hacking ``plotter.py`` in your favorite editor and run ``pytest`` frequently.

Read the comments carefully to make this work and do not trust every line of code.

Links
-----

Notebooks, tutorials ...
