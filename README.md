vmf-batch
=============

Batch conversion script for the VMF file format.

Setup
-----

This script is tested under Python 3.4 and requires ``music21`` version 2.0.4 or later, and vmf-converter.

Creating a virtualenv
~~~~~~~~~~~~~~~~~~~~~

It is recommended to use a virtual environment to isolate projects on your filesystem.

From a command prompt, run the following to create your virtualenv::

    $ pyvenv-3.4 {venvname}

where {venvname} is the name of your virtualenv.

Activating the virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~

The virtualenv that was created can be activated by navigating to the root directory
of the virtualenv and running the following::

    $ source ./bin/activate

Known issue in Ubuntu 14.04 LTS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On Ubuntu 14.04 LTS, there is a known bug with pre-installing pip into the virtualenv.
In this case, use the following::

    $ pyvenv-3.4 --without-pip {venvname}

This will install the virtualenv without pip installed. Activate this virtualenv and
run the following to install pip and setuptools.

.. code-block:: bash

    $ wget https://pypi.python.org/packages/source/s/setuptools/setuptools-3.4.4.tar.gz
    $ tar -vzxf setuptools-3.4.4.tar.gz
    $ cd setuptools-3.4.4
    $ python setup.py install
    $ cd ..
    $ wget https://pypi.python.org/packages/source/p/pip/pip-1.5.6.tar.gz
    $ tar -vzxf pip-1.5.6.tar.gz
    $ cd pip-1.5.6
    $ python setup.py install
    $ cd ..
    $ rm -rf pip-1.5.6 pip-1.5.6.tar.gz setuptools-3.4.4 setuptools-3.4.4.tar.gz

Now you should have a virtualenv which is ready for population.

Installing project dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the virtualenv activated, navigate to the project root and run::

    $ pip install -r requirements.txt

This will install the dependencies of this project.

Usage
-----

To use this script, from the command prompt use the following command::

    $ python vmf_batch.py {sourceDir} {targetDir} {targetFormat}
    
``{sourceDir}``: The absolute path of the source directory containing the files to convert.
``{targetDir}``: The absolute path of the target directory where converted files should be saved.
``{targetFormat}``: The format to convert to.