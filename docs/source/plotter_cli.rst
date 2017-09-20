.. _plotter_cli:

Adding a Command-Line Interface
===============================

Prepare
-------

See :ref:`prepare`.

Activate the conda workshop enviroment::

    $ source activate workshop

Aim
---

We are going to write a command line interface (CLI) for our plot function.

Objectives:

* You will learn how to write a CLI with the Python library `argparse <https://docs.python.org/3/library/argparse.html>`_.


Run the plotter CLI
-------------------

Go to the plotter tutorial source::

    $ cd birdhouse-workshop/tutorials/03_plotter_cli

See the command line options of our plotter::

    $ python plotter.py -h
    usage: plotter.py [-h] [-V [VARIABLE]] dataset

Plot our well-know image::

    $ python plotter.py --variable air ../data/air.mon.ltm.nc

Exercise 1
-----------

Play a little bit with the command line. Try some other options (``-V``),
use invalid input (water) and skip some arguments.

Exercise 2
----------

Extend the command line and the plot function with an optional parameter for
the map projection.

Open your editor on ``plotter.py`` ... and happy hacking.

Don't forget to test often::

  $ pytest plotter.py
