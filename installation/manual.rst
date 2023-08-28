.. _sec_install_manual:

Manual Installation
=========================


.. _sec_manual_req:

Requirements
-------------

MAD requires the following things to be installed available on your server:

- A server/computer running Linux. RaspberryPis do work, but aren't recommended
- A 64-bit CPU for MAD is also highly recommended since some optional parts of MAD do require to run on 64-bit. It does have a fallback for 32-bit CPUs though
- MariaDB server
- Python 3.8 or 3.8 and Python's package manager command line tool :code:`pip`. 3.9 is currently not supported!
- Use a :code:`virtualenv` to install dependencies. Have a look at `this <https://docs.python.org/3/tutorial/venv.html>`_ and `this <https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>`_ if you're new to :code:`virtualenv`

.. _sec_manual_system_prep:

System preparation
-------------------

.. note::

  This whole article assumes a fresh installed `Ubuntu 20.04 Server <https://www.ubuntu.com/download/server>`_. If you're running a more recent version of Ubuntu or another Linux distribution - that's totally fine, but keep in mind there may be some difference in your setup.

.. _sec_manual_database:

MariaDB
---------

You need a Database with full permissions. That DB can be located on a different Server, but needs to be accessible by your MAD server.

If you are plan to use `PMSF <https://github.com/pmsf/PMSF>`_ as a webfrontend: use at least MariaDB 10.2 or higher!

.. code-block:: bash

  sudo apt update
  sudo apt install mariadb-server
  sudo mysql_secure_installation

Log in to your Database and create a dedicated user for MAD. To create a new database and grant permissions for your
dedicated MAD database user you must run the following command (make sure to change "my_database_user" and "password" to
the correct values):

.. code-block:: sql

  CREATE DATABASE my_database_name;
  CREATE USER 'my_database_user'@'localhost' IDENTIFIED BY 'password';
  GRANT ALL PRIVILEGES ON my_database_name.* TO 'my_database_user'@'localhost';
  FLUSH PRIVILEGES;

.. _sec_manual_client_libs:

Install client libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: bash

  sudo apt install default-libmysqlclient-dev

.. TODO fix internal links

.. _sec_manual_db_schema:

Database schema
^^^^^^^^^^^^^^^^

MAD will install the latest database schema automatically on initial boot and no additional steps are required. If you encounter any issues the up-to-date schema can be found `here <https://raw.githubusercontent.com/Map-A-Droid/MAD/master/scripts/SQL/rocketmap.sql>`_.


.. _sec_manual_python:

Python
--------

Since Ubuntu 20.04 does comes with a pre-installed python3.8 version but without a pip3 installation, run this command to install it:

.. code-block:: bash

  apt install python3-pip python3-wheel

Make sure you have the right version installed, since even if python3.8 is installed, the `python3` command could still point to `python3.5` or below!
Check if `pip` and `python` is installed correctly by running:

- :code:`python3 --version` - should return 3.8.x
- :code:`pip3 --version` - If it returns a version that is related to your python version, it is working.

.. _sec_manual_py_venv:

Virtual Environment
^^^^^^^^^^^^^^^^^^^^

A virtual environment is a way to install python packages in a different location to avoid potential version conflicts with other software like RocketMAD or MADevice. It's like a standalone version of python, independent of your "normal" python. Install it with:

.. code-block:: bash

  apt install python-virtualenv

And create a new virtual environment called :code:`mad_env` in your home directory:

.. code-block:: bash

  virtualenv -p python3 ~/mad_env

Whenever you see :code:`python3` or :code:`pip3` in the documentation, use :code:`~/mad_env/bin/python3` and :code:`~/mad_env/bin/pip3` instead. And, of course, use a different environment location for different python tools.

You can activate the virtual environment via :code:`source ~/mad_env/bin/activate`. This makes sure you can simply call :code:`python3` or :code:`pip3` wherever you are and it will perform all commands with the Python version and the dependencies form your virtualenvironment. Have a look at `this <https://docs.python.org/3/tutorial/venv.html>`_ or `this <https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>`_ link for more information.

.. _sec_manual_mad:

MAD
----

Next Step is to clone this repository and install all the required pip packages:

.. code-block:: bash

  git clone https://github.com/Map-A-Droid/MAD.git

Change into in the directory of MAD and run:

.. code-block:: bash

  pip3 install -r requirements.txt

MAD will also check the screen on your phone every now and then to check for errors. Make sure you have the required dependencies installed on your system. Unfortunately, there's no package for opencv on RaspberryPi which means you have to build it on your own. You should be able to find out how with a quick search on the web.

.. code-block:: bash

  sudo apt-get install tesseract-ocr python3-opencv

Another but optional dependency you may want to install is `ortools <https://developers.google.com/optimization>`_. MAD utilizes ortools to generate more optimized routes for your areas and it is as quick as MAD's built-in routing algorithm if not even faster. The downside of this as states in :ref:`the requirements<Requirements>` is, that you need a 64-bit server.

.. code-block:: bash

  pip3 install ortools

.. _sec_manual_config:

Configuration
^^^^^^^^^^^^^^

Copy config.ini.example (from the configs folder in the MAD repo) to "config.ini" (also in the configs folder):

.. code-block:: bash

  cp configs/config.ini.example configs/config.ini

and then edit the config file accordingly. 

The next step is to configure MAD. This will only start MAD's web frontend called MADmin.

.. warning::
 MAD will not actually scan in configmode! The mode is for the first configuration only. Remove the :code:`-cm` when you are done.

.. code-block:: bash

  python3 start.py 

By default MADmin will be available on http://your_server_ip:5000.

.. _sec_manual_running:

Running
---------

If everything is set up correctly, you can start MAD:

.. code-block:: bash

  python3 start.py

.. _sec_manual_extra:

Further steps
-------------

Review and implement anything related to the `security section <../security>`_.
