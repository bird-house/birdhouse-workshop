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

  $ cd birdhouse-workshop/tutorials/10_plotter_process/processes

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

    $ cd birdhouse-workshop/tutorials/10_plotter_process

Start the WPS service:

.. code-block:: bash

    $ python ../../demo/demo.py

Check if the service is running:

http://127.0.0.1:5000/wps?service=WPS&request=GetCapabilities

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

Run an **Execute** request with an external NetCDF file.

http://127.0.0.1:5000/wps?service=WPS&request=Execute&version=1.0.0&identifier=simple_plot&datainputs=variable=air;dataset=@xlink:href=https://www.esrl.noaa.gov/psd/thredds/fileServer/Datasets/ncep.reanalysis.derived/surface/air.mon.ltm.nc

.. todo::
  Execute Request with direct output.


Links
-----

* `NOAA Thredds Catalog <https://www.esrl.noaa.gov/psd/thredds/catalog.html>`_
