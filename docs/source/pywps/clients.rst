.. _pywps_clients:

Clients
=======

Requirements
------------

See :ref:`prepare`.

Activate the conda workshop enviroment::

    $ source activate workshop

Aim
---

We are going to write use a WPS client.

Objectives:

* You will learn how to use a WPS client.
* You will learn to use Jupyter Notebooks.

Birdy
-----

`Birdy <http://birdy.readthedocs.io/en/latest/>`_ is a command-line client for Web Processing Services.

Install it via conda:

.. code-block:: bash

    $ conda install -c birdhouse birdhouse-birdy

Start the demo WPS service:

.. code-block:: bash

    $ python demo/demo.py

Let birdy know the WPS service URL:

.. code-block:: bash

    $ export WPS_SERVICE=http://localhost:5000/wps

See which processes are available:

.. code-block:: bash

    $ birdy -h
    usage: birdy [<options>] <command> [<args>]

Show the description of ``say_hello``:

.. code-block:: bash

    $ birdy say_hello -h
    usage: birdy say_hello [-h] --name [NAME]
                       [--output [{response} [{response} ...]]]

Run ``say_hello``:

.. code-block:: bash

    $ birdy say_hello --name Birdy
    [ProcessAccepted 0/100] PyWPS Process say_hello accepted
    [ProcessSucceeded 0/100] PyWPS Process Process Say Hello finished
    Output:
    response=Hello Birdy


OWSLib
------

use notebook.

Phoenix
-------

Just an online example.

QGIS
----

Maybe a screenshot.

Exercise
--------

Links
-----

Notebooks, tutorials ...
