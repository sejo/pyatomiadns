Welcome to pyatomiadns's documentation!
=======================================

This is the main and official documentation for pyatomiadns. pyatomiadns is still in BETA, test before use!

My name is Jochen Maes and you can contact me @ firstname dot sejo dash it dot be, I'm also online on freenode, oftc as sejo.
I wrote this to be able to populate my dns servers with ansible.

The ansible module can be found under pyatomiadns/ansible/atomiadns.py.

You can find the code of this project here:
https://github.com/sejo/pyatomiadns


One should also investigate https://github.com/sejo/django_atomiadns for a sane webapp.


Thanks
======

For the release of the 1.3 release I would like to thank `Amplidata NV`_ for the time I was allowed to spend on creating and testing the 1.3 branch.

How to test
===========

On github in the vagrant folder you will see a Vagrant file and a crude ansible playbook.
This playbook shows you how to install and configure atomiadns and runs some basic ansible commands for atomiadns.

I use the standard precise64 box:

.. code-block:: bash

    vagrant box add precise64 http://files.vagrantup.com/precise64.box

Run above command to get the correct box.


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

.. _Amplidata NV: http://amplidata.com