.. _pywps_process:

Processes
=========

Requirements
------------

See :ref:`prepare`.

Activate the conda workshop enviroment:

.. code-block:: bash

    $ source activate workshop

Aim
---

We are going to write a PyWPS process.

Objectives:

* You will learn how to write a PyWPS process.


What is a WPS Process?
----------------------

In PyWPS a process is a Python class that has the following structure:

* The parent ``Process`` class.
* Four input/ouput classes: ``ComplexInput``, ``LiteralInput``, ``ComplexOutput`` and ``LiteralOutput``
* The ``_handler(request, response)`` method
* The ``request.inputs`` and the ``response.output`` properties.

Go through the `PyWPS documentation on Processes <http://pywps.readthedocs.io/en/latest/process.html>`_.

Create your first process
-------------------------

Let's create a new process that generates a nice and simple plot from a NetCDF file.
We have written a ``simple_plot`` function, which we can use here.
We need to do the following:

1. write the PyWPS process definition,
2. call our ``simple_plot`` method,
3. activate our process in PyWPS.

Check the plotter function
--------------------------

Change into the tutorial ``processes`` folder:

.. code-block:: bash

  $ cd ~/birdhouse-workshop/tutorials/10_pywps_process/processes

You can find here the ``plotter.py`` module from our previous exercise:

.. code-block:: bash

  $ ls
  plotter.py

Let's see if it still works:

.. code-block:: bash

  $ python plotter.py -h

Generate a plot:

.. code-block:: bash

  $ python plotter.py ../../../data/air.mon.ltm.nc -V air
  dataset=['../../../data/air.mon.ltm.nc'], variable=air
  Plotting ../../../data/air.mon.ltm.nc ...
  Using map projection <cartopy.crs.PlateCarree object at 0x7fae109538e0>
  Plot written to plot.png
  Output: plot.png


Write the process definition
-----------------------------

In the ``processes/`` folder there is another file:

.. code-block:: bash

  $ ls
  wps_simple_plot.py

This file contains the process definition. Notice the input and output parameters.

Start the service
-----------------

Change into the tutorials folder:

.. code-block:: bash

    $ cd ~/birdhouse-workshop/tutorials/10_pywps_process

Start the WPS service:

.. code-block:: bash

    $ python ../../demo/demo.py

Check if the service is running:

http://127.0.0.1:5000/wps?service=WPS&request=GetCapabilities

.. code-block:: bash

   $ curl "http://127.0.0.1:5000/wps?service=WPS&request=GetCapabilities"

Notice that the ``simple_plot`` service is not activated. Well, time to exercise ...

Exercise 1
----------

Activate the ``SimplePlot`` process from the ``wps_simple_plot`` module.
See if it shows up in the **GetCapabilites** request.

.. tip::
  You need to edit ``processes/__init__.py`` and restart the demo service.

Exercise 2
----------

When the ``SimplePlot`` process is activated then run a **DescribeProcess** request.

.. tip::
  Find the process ``identifier`` of ``SimplePlot`` in the **GetCapabilities** document
  and adapt the **DescribeProcess** URL from our previous exercise.

Exercise 3
-----------

Run an **Execute** request with a remote netCDF file from a
`Thredds data server <https://www.esrl.noaa.gov/psd/thredds/catalog/Datasets/ncep.reanalysis.derived/surface/catalog.html?dataset=Datasets/ncep.reanalysis.derived/surface/air.mon.ltm.nc>`_.

Use the following request URL.

.. code-block:: bash

  http://127.0.0.1:5000/wps?
      Service=WPS&
      Request=Execute&
      Version=1.0.0&
      Identifier=PLOT_IDENTIFIER&
      DataInputs=variable=air;dataset=@xlink:href=NC_URL

Or as a one-liner:

http://127.0.0.1:5000/wps?Service=WPS&Request=Execute&Version=1.0.0&Identifier=PLOT_IDENTIFIER&DataInputs=variable=air;dataset=@xlink:href=NC_URL

You need to replace **PLOT_IDENTIFIER** with the correct
processes identifier. Replace **NC_URL** with a remote netCDF data file (HTTP, not OpenDAP),
for example:

  https://www.esrl.noaa.gov/psd/thredds/fileServer/Datasets/ncep.reanalysis.derived/surface/air.mon.ltm.nc

Notice that the output will be returned as reference, for example:

.. code-block:: xml
  :emphasize-lines: 5

  <wps:ProcessOutputs>
    <wps:Output>
      <ows:Identifier>output</ows:Identifier>
      <ows:Title>Simple Plot</ows:Title>
      <wps:Reference xlink:href="http://localhost:5000/outputs/4d075e9a-acf4-11e7-9396-acde48001122/plot_ex33_nbf.png" mimeType="image/png"/>
    </wps:Output>
  </wps:ProcessOutputs>


Exercise 4
----------

You can also run the process in
`asynchronous mode <http://pywps.readthedocs.io/en/latest/process.html#progress-and-status-report>`_
by adding the parameters ``storeExecuteResponse=true`` and ``status=true``.

.. code-block:: bash

  http://127.0.0.1:5000/wps?
      Service=WPS&
      Request=Execute&
      Version=1.0.0&
      Identifier=PLOT_IDENTIFIER&
      DataInputs=variable=air;dataset=@xlink:href=NC_URL&
      storeExecuteResponse=true&
      status=true

In this case you will a response, which tells you that the process has been accepted,
and you need to poll the status document given by the **statusLocation** URL:

.. code-block:: xml
  :emphasize-lines: 4,11

  <wps:ExecuteResponse
    service="WPS" version="1.0.0" xml:lang="en-US"
    serviceInstance="http://localhost:5000/wps?service=WPS&amp;request=GetCapabilities"
    statusLocation="http://localhost:5000/outputs/c894c1b4-acf7-11e7-b989-acde48001122.xml">
    <wps:Process wps:processVersion="1.0">
      <ows:Identifier>simple_plot</ows:Identifier>
      <ows:Title>Simple Plot</ows:Title>
      <ows:Abstract>Returns a nice and simple plot.</ows:Abstract>
    </wps:Process>
    <wps:Status creationTime="2017-10-09T15:43:10Z">
      <wps:ProcessAccepted>PyWPS Process simple_plot accepted</wps:ProcessAccepted>
    </wps:Status>
  </wps:ExecuteResponse>

.. not working with pywps on python 3
  Exercise 5
  ----------

  You can also return the output directly. For this modify the above request
  and add the ``RawDataOutput`` parameter:

  .. code-block:: bash

    http://127.0.0.1:5000/wps?
        Service=WPS&
        Request=Execute&
        Version=1.0.0&
        Identifier=PLOT_IDENTIFIER&
        DataInputs=variable=air;dataset=@xlink:href=NC_URL&
        RawDataOutput=output

Links
-----

* `PyWPS workshop <https://github.com/PyWPS/pywps-workshop/blob/master/02-Process.md>`_
* `Geoprocessing Info <http://geoprocessing.info/wpsdoc/1x0ExecuteGET>`_
* `NOAA Thredds Catalog <https://www.esrl.noaa.gov/psd/thredds/catalog.html>`_
* `Notebook with WPS requests <https://github.com/bird-house/birdhouse-workshop/blob/master/tutorials/10_pywps_process/notebooks/wps-requests.ipynb>`_
