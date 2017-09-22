.. _prepare:

Getting Started
===============

Clone the workshop repo from Github:

.. code-block:: bash

    $ git clone https://github.com/bird-house/birdhouse-workshop.git

Create the workshop conda envionment:

.. code-block:: bash

    $ conda create -n workshop python=3

Activate the conda workshop enviroment:

.. code-block:: bash

    $ source activate workshop

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

Remove the *workshop* conda environment:

.. code-block:: bash

    $ source deactivate
    $ conda env remove -n workshop

Create a new environment with *all* dependencies used in this workshop:

.. code-block:: bash

    $ conda create -n workshop -c birdhouse -c conda-forge \
        python=3 \
        pytest \
        netcdf4 \
        cartopy \
        pywps


Or use the ``environment.yml`` file in the top level folder:

.. code-block:: bash

   $ conda env create -f environment.yml
