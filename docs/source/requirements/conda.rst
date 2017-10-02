.. _requirements_conda:

Conda
=====

`Conda`_ is an Open Source package and environment manager that can help to
manage project dependencies. Conda works on Linux, macOS and Windows.
It was created for Python programs, but it can package and
distribute software for any language.
Therefore it allows us to use it for multi-language projects.

Conda allows you to build your own packages and share them via channels on
`Anaconda Cloud`_.
There is a community effort to build and maintain packages needed by various projects,
called `Conda Forge`_.

You can create conda environments with a specified list of packages,
similar to Python virtualenv.
These environemnts can be documented by a ``environment.yml`` configuration file
and shared with others.

.. warning::
  In this workshop we will install *all* software packages using `Conda`_.

Installation
------------

.. note::
  If you already have Conda/Anaconda installed, you can use it in this workshop.
  See: :ref:`dkrz`.

.. note::
  You don't need admin rights to install conda and conda packages.

Download and install the appropriate Miniconda installer
from https://conda.io/miniconda.html

With Anaconda you can create environments that use any Python version (e.g. Python 2.7 or Python 3.6),
so install the latest Python 3.x and if you find out later you need a Python 2.7 environment, you can create one.


Linux/macOS
+++++++++++

You can *copy and paste* the following script to install Miniconda with default settings:

.. code-block:: bash

    if [[ $(uname) == "Darwin" ]]; then
      url=https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
    elif [[ $(uname) == "Linux" ]]; then
      url=https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    fi
    curl $url -o miniconda.sh
    bash miniconda.sh -b
    export PATH=$HOME/miniconda3/bin:$PATH

We also recommend to add the following line to your ``~/.bashrc`` file to
make Miniconda the Python found first than the system Python:

.. code-block:: bash

    export PATH=$HOME/miniconda3/bin:$PATH

Windows
+++++++

Run the installer, choose *Just Me* (not *All Users*), and choose a *Install Location* owned by you.

.. todo::
  Screenshots for Windows installation.

Check your Python version
-------------------------

We are using Python 3.6::

  $ which python
  $HOME/miniconda3/bin/python
  $ python --version
  Python 3.6.2 :: Continuum Analytics, Inc.

Links
-----

* https://www.anaconda.com/blog/developer-blog/conda-data-science/
* https://github.com/ioos/notebooks_demos/blob/master/webpage/other_resources.md


.. _Conda: http://conda.io/
.. _Anaconda Cloud: https://anaconda.org/conda-forge
.. _Conda Forge: https://conda-forge.org/
