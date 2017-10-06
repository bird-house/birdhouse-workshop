.. _testing_plotter:

Testing the Plot Function
=========================

Prepare
-------

See :ref:`prepare`.

Activate the Conda workshop enviroment:

.. code-block:: bash

    $ source activate workshop

Aim
---

We are going to write a unit test for our Python plot function.

Objectives:

* You will learn how to write a unit test with *pytest*.


Run pytest
----------

Go to the plotter tutorial source:

.. code-block:: bash

    $ cd ~/birdhouse-workshop/tutorials/02_testing_plotter

Run the ``plotter.py`` like in the previous tutorial and see if it works:

.. code-block:: bash

    $ python plotter.py

Now, we want to implement a unit test for our plot function.
We are using `pytest <https://docs.pytest.org/en/latest/contents.html>`_ as testing framework.
Install it via conda:

.. code-block:: bash

    $ conda install -c conda-forge pytest

Run now *pytest* on our plotting module:

.. code-block:: bash

    $ pytest plotter.py
    E       NotImplementedError: This test is not implemented yet. Help wanted!

Oops ... the test is not working yet.

Exercise
--------

Your task is to implement a meaningful test for our ``simple_plot`` function.

Start hacking ``plotter.py`` in your favorite editor and run ``pytest`` frequently.

.. warning::

  Read the comments carefully to make this work and **do not trust each line of code**.

Links
-----

* pytest: https://docs.pytest.org/en/latest/
