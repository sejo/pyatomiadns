Welcome to pyatomiadns's documentation!
=======================================

This is the main and official documentation for pyatomiadns.

My name is Jochen Maes and you can contact me @ firstname dot sejo dash it dot be, I'm also online on freenode, oftc as sejo.
I wrote this to be able to populate my dns servers with ansible.
I'll add a link to the correct project for the ansible module when I finish it.

You can find the code of this project here:
htts://github.com/sejo/pyatomiadns

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

Contents:

.. toctree::
    :maxdepth: 2

    pyatomiadns/client


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

