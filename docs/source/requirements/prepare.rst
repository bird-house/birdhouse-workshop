.. _prepare:

Getting Started
===============

Clone the workshop repo from Github:

.. code-block:: bash

    $ git clone https://github.com/bird-house/birdhouse-workshop.git

.. note::
  In this workshop we assume that your workshop sources are in
  your home folder ``~/birdhouse-workshop``. If the sources are located at
  a different place then you need to adapt the workshop root folder accordingly.

Create the *workshop* conda environment:

.. code-block:: bash

    $ conda create -n workshop python=3

Activate the conda *workshop* environment (Linux and macOS):

.. code-block:: bash

    $ source activate workshop

.. warning::
  On *Windows* you use the following command::

      $ activate workshop

.. tip::
  If you are a DKRZ user you can also log-in to the :ref:`DKRZ Compute Cluster <dkrz>`


I don't have git ...
--------------------

Don't worry ... the quickest way to install git is using conda:

.. code-block:: bash

    $ conda install git


If things go wrong ...
----------------------

Well, this can happen ... you can easily get into troubles with resolving conda
package dependencies. The easiest way to solve it is *tabula rasa* ... remove
the conda environment and install it from new.

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

.. _dkrz:

Using your DKRZ account (*DKRZ users only*)
---------------------------------------------

You can use your DKRZ account and log-in to `Mistral`_ to run this workshop:

.. code-block:: bash

  $ ssh -X myname@mistral.dkrz.de
  # unload conflicting modules
  $ module unload netcdf_c
  # load anaconda module
  $ module load anaconda3

You may start a `Byobu`_ session to have multiple terminal windows:

.. code-block:: bash

  $ byobu

.. _Byobu: http://byobu.co/
.. _Mistral: https://www.dkrz.de/Nutzerportal/dokumentationen/de-mistral
