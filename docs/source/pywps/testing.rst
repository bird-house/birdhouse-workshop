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

Start by trying the **GetCapabilities** request:

.. code-block:: bash

    $ wget -q -O - "http://127.0.0.1:5000/wps?service=WPS&request=GetCapabilities"

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


Writing a unit test
-------------------



Exercise
--------

Links
-----

Notebooks, tutorials ...

https://github.com/PyWPS/pywps-workshop/blob/master/03-Testing.md
