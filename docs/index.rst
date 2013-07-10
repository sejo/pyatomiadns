.. pyatomiadns documentation master file, created by
sphinx-quickstart on Wed Jul 10 14:01:19 2013.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive.

Welcome to pyatomiadns's documentation!
=======================================

Contents:

.. toctree::
    :maxdepth: 2

TODO
====

- create setup.py file
- create pypi package
- improve documentation
- improve checks on generated methods
- improve errorhandling
- ... other idea's?


How to generate the api client file
===================================

I created a yaml file with most of the API calls that the Atomiadns json API supports, you can adapt however you want it.
Each time to change it you should rebuild the pyatomiadns.client module.
This is how to do it :

.. code-block:: bash

    source venv/bin/activate #if your virtualenv is in venv
    cd pyatomiadns/client_builder
    python builder.py api.yaml

Running the previous commands should have generated a new client.py file.


Generated API
=============

.. automodule:: pyatomiadns.client

.. autoclass:: AtomiaClient
    :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

