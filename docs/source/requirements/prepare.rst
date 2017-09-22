.. _prepare:

Getting Started
===============

Clone the workshop repo from Github:

.. code-block:: bash

    $ git clone https://github.com/bird-house/birdhouse-workshop.git

Create the *workshop* conda environment:

.. code-block:: bash

    $ conda create -n workshop python=3

Activate the conda *workshop* environment (Linux and MacOS):

.. code-block:: bash

    $ source activate workshop

.. warning::

  On *Windows* you use the following command::

      $ activate workshop

I don't have git ...
--------------------

Don't worry ... the quickest way to install git is using conda:

.. code-block:: bash

    $ conda install git


If things go wrong ...
----------------------

Well, this can happen ... you can easily get into troubles with resolving conda
package dependencies. The easiest way to solve it is *tabula rasa* ... remove
the conda environment at install it from new.

Deactivate the current environment (Linux and MacOS):

.. code-block:: bash

    $ source deactivate

.. warning::

  On *Windows* you need to use the following command to deactivate the
  environment::

    $ deactivate

Remove the *workshop* conda environment:

.. code-block:: bash

    $ conda env remove -n workshop

Create a new *workshop* environment with *all* dependencies used in this workshop by using
a conda ``environment.yml`` file in the top level folder:

.. code-block:: bash

   $ conda env create -f environment.yml
