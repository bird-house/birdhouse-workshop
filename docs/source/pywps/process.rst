.. _pywps_process:

Processes
=========

Requirements
------------

See :ref:`prepare`.

Activate the conda workshop enviroment::

    $ source activate workshop

Aim
---

We are going to write a PyWPS process.

Objectives:

* You will learn how to write a PyWPS process.


What is a Process?
------------------

In PyWPS a process is a python class that has the following structure:

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




Exercise
--------


Links
-----

Notebooks, tutorials ...
