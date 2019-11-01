============
Server setup
============

System preparation
==================

.. note::

  This whole article assumes a fresh installed `Ubuntu 18.04 Server <https://www.ubuntu.com/download/server>`_. If you're running another Linux distribution - that's totally fine, but keep in mind there may be some difference to your setup.

If you're already running a Ubuntu 18.04 setup, you can skip this part.

Edit the file /etc/update-manager/release-upgrades:

.. code-block:: bash

  sudo nano /etc/update-manager/release-upgrades

On the line that says :code:`Prompt=..` change it to :code:`Prompt=normal`. Save with :kbd:`ctrl` + :kbd:`o` and exit with :kbd:`ctrl` + :kbd:`x`

Now, make sure LXD is removed:

.. code-block:: bash

  sudo dpkg --force depends -P lxd; sudo dpkg --force depends -P lxd-client

Next, we need to make everything nice and updated

.. code-block:: bash

  sudo apt update
  sudo apt upgrade

Now look for and update Ubuntu.

.. code-block:: bash

  sudo do-release-upgrade

Simply follow the prompts and agree to anything it asks (pretty much anyhow) until it asks to reboot. Decline to restart, then exit WSL by typing `exit`. Do not close your terminal window.

Back in the terminal window, type bash once more.

Now, let's install openCV

.. code-block:: bash

  sudo apt-get install python3-opencv

MySQL / MariaDB
===============

You need a Database with full permissions. That DB can be located on a different Server, but needs to be accessible by your MAD server. Use MariaDB, no other database system is supported (MySQL kinda works, but doesn't support every feature).

If you are plan to use `PMSF <https://github.com/whitewillem/PMSF>`_ as a webfrontend: use at least MySQL 8 or MariaDB 10.2 or higher!

.. code-block:: bash

  sudo apt update
  sudo apt install mariadb-server
  sudo mysql_secure_installation

Log in to your Database and create a dedicated user for MAD (if you don't know how, check out `this tutorial <https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql>`_).

Create a new database and grant permissions for your dedicated MAD database user:

.. code-block:: sql

  CREATE DATABASE my_database_name;
  GRANT ALL PRIVILEGES ON my_database_name.* TO 'my_database_user'@'localhost';
  FLUSH PRIVILEGES;

.. TODO fix internan links

MAD is using the RocketMap database schema, you can either install it using `OSM-Rocketmap <https://github.com/cecpk/OSM-Rocketmap>`_ or, if you just want the database and not the complete frontend of RM, use the [databasesetup.py](../extras/scripts#databasesetup-databasesetup-py) script.

If you want to use OSM-Rocketmap, set it up and launch it for the first time. It will create the the tables automatically. Follow the guide from the `official Rocketmap documentation <https://osm-rocketmap.readthedocs.io/>`_, but make sure to clone the `OSM-Rocketmap <https://github.com/cecpk/OSM-Rocketmap>`_ fork instead of the normal one.

.. code-block:: bash

  python3 runserver.py

.. TODO update this reference

Rocketmap will only act as a webfrontend. See [webfrontends](/extras/webfrontends) for more informations.

Install client libraries
------------------------
.. code-block:: bash

  sudo apt install default-libmysqlclient-dev

After all this is over, follow the Linux part about installing, scroll down to header MAD/PIP-Packages. Some parts might be repeated, don't worry about it.

Running MAD is now exactly the same as running it on Linux, except that your mariadb is running on Windows, and you're going a bit slower than if you would have just listened and installed on Linux directly in the first place.

Python
======

Since Ubuntu 18.04 does comes with a pre-installed python3.6 version but without a pip3 installation, run this command to install it:

.. code-block:: bash

  apt install python3-pip

Make sure you have the right version installed, since even if python3.6 is installed, the `python3` command could still point to `python3.5` or below!
Check if `pip` and `python` is installed correctly by running:

- :code:`python3 --version` - should return 3.6.x
- :code:`pip3 --version` - If it returns a version, it is working.

MAD
===

Next Step is to clone this repository and install all the required pip packages:

.. code-block:: bash

  git clone https://github.com/Map-A-Droid/MAD.git

Change into in the directory of MAD and run:

.. code-block:: bash

  pip3 install -r requirements.txt

MAD will also check the screen on your phone every now and then to check for errors. Make sure you have the required dependencies installed on your system:

.. code-block:: bash

  sudo apt-get install tesseract-ocr python3-opencv

If you are encountering the error :code:`OSError: mysql_config not found`, make sure you have the apt package :code:`default-libmysqlclient-dev` installed.

Configuration
=============

Copy the example config file and rename it to "config.ini":

.. code-block:: bash

  cp configs/config.ini.example configs/config.ini

and edit the config file accordingly.

The next step is to configure the so-called "mappings.json" (located in configs/mappings.json). This file is responsible to "map" your phones to walkers etc. The easiest way to configure MAD is through MADmin - the web frontend:

.. code-block:: bash

  python3 configmode.py

By default MADmin will be available on http://your_server_ip:5000. Go to "Settings" and start with adding an area. The type is depending on what do you want to scan. Every type and option of it has a description explaining itself.

Running
=======

If everything is set up correctly, you can start MAD:

.. code-block:: bash

  python3 start.py

Deploying behind a Reverse Proxy
================================

MAD supports being run behind a Reverse Proxy.  The reverse proxy relies on the header, `X-Script-Name`, to inform MADmin on how to construct the URIs.  For our examples we will use the following:
* Using NGINX as our reverse proxy
* MADmin runs on localhost
* MADmin uses port 5000
* We wish to access the site at '/madmin'
* The FQDN we are using to access MADmin is 'mapadroid.local'
* We only want files 100MB or less to be uploaded
* SSL Ceritificate is located at /etc/ssl_cert.crt
* SSL Certificate Key is located at /etc/ssl_key.pem

Configuring HTTP
----------------
MADmin URL: `http://mapadroid.local/madmin`

.. code-block::

  server {
      listen 80;
      server_name mapadroid.local;

      location ~ /madmin(.*)$ {
          proxy_set_header X-Real-IP  $remote_addr;
          proxy_set_header X-Forwarded-For $remote_addr;
          proxy_set_header X-Forwarded-Proto http;
          proxy_set_header X-Script-Name /madmin;
          proxy_set_header Host $host;
          proxy_pass http://localhost:5000$1$is_args$args;
          client_max_body_size 100M;
      }
  }

Configuring HTTPS
-----------------
MADmin URL: `https://mapadroid.local/madmin`

.. code-block::

  server {
      listen 443 ssl;
      ssl_certificate /etc/ssl_cert.crt;
      ssl_certificate_key /etc/ssl_key.pem;
      server_name mapadroid.local;

      location ~ /madmin(.*)$ {
          proxy_set_header X-Real-IP  $remote_addr;
          proxy_set_header X-Forwarded-For $remote_addr;
          proxy_set_header X-Forwarded-Proto https;
          proxy_set_header X-Script-Name /madmin;
          proxy_set_header Host $host;
          proxy_pass http://localhost:5000$1$is_args$args;
          client_max_body_size 100M;
      }
  }


Docker
======

.. note::
  If you don't know anything about Docker, you probably want ignore this step.

.. warning::
  MAD's Docker support is community driven and untested by MAD's core developers!

Setup MAD and Rocketmap database.
---------------------------------

In this section we explain how to setup MAD and a Rocketmap database using docker-compose.

Preparations
----------------

You can just copy & paste this to do what is written below:

.. code-block:: none

  mkdir MAD-docker && \
  cd MAD-docker && \
  mkdir mad && \
  mkdir mad/configs && \
  touch docker-compose.yml && \
  mkdir docker-entrypoint-initdb && \
  wget -O docker-entrypoint-initdb/rocketmap.sql https://raw.githubusercontent.com/Map-A-Droid/MAD/master/scripts/SQL/rocketmap.sql && \
  cd mad/configs/ && \
  touch mappings.json && \
  wget -O config.ini https://raw.githubusercontent.com/Map-A-Droid/MAD/master/configs/config.ini.example && \
  mkdir geofences && cd ../../

This will:

#. Create a directory `MAD-docker`.
#. Create a file `docker-compose.yml`.
#. Create a directory `MAD-docker/mad`. (here we store MAD related stuff)
#. Create a directory `MAD-docker/mad/configs`. (here we store config files for MAD). Here you store your `config.ini`, `mappings.json` and a directory `geofences` (which contains your geofences). Examples for these files can be found @github https://github.com/Map-A-Droid/MAD/tree/master/configs
#. Create a directory `MAD-docker/docker-entrypoint-initdb`
#. Download the Rocketmap Database Schema: https://raw.githubusercontent.com/Map-A-Droid/MAD/master/SQL/rocketmap.sql and store it in the directory `docker-entrypoint-initdb`.

Your directory should now look like this:

.. code-block:: python

  MAD-docker/
    docker-compose.yml
    docker-entrypoint-initdb/
      rocketmap.sql
    mad/
    configs/
      config.ini
      mappings.json
      geofences/

If you start from scratch, add the following content to `mad/configs/mappings.json`:

.. code-block:: json

  {
    "areas": {
      "entries": {},
      "index": 0
    },
    "auth": {
      "entries": {},
      "index": 0
    },
    "devices": {
      "entries": {},
      "index": 0
    },
    "devicesettings": {
      "entries": {},
      "index": 0
    },
    "migrated": true,
    "monivlist": {
      "entries": {},
      "index": 0
    },
    "walker": {
      "entries": {},
      "index": 0
    },
    "walkerarea": {
      "entries": {},
      "index": 0
    }
  }

If you have an existing mappings.json, because you used MAD before, then just copy it over.

Writing the docker-compose file
-------------------------------

We use docker-compose to deploy and manage our services.

Fill docker-compose.yml with the following content. Below we explain the details of every service.

.. code-block:: yaml

  version: '2.4'
  services:
    mad:
      container_name: pokemon_mad
      image: mapadroid/map-a-droid
      restart: always
      volumes:
        - /etc/timezone:/etc/timezone:ro
        - /etc/localtime:/etc/localtime:ro
        - ./mad/configs/geofences:/usr/src/app/configs/geofences
        - ./mad/configs/config.ini:/usr/src/app/configs/config.ini
        - ./mad/configs/mappings.json:/usr/src/app/configs/mappings.json
        - ./volumes/mad/files:/usr/src/app/files
        - ./volumes/mad/logs:/usr/src/app/logs
      depends_on:
        - rocket-db
      networks:
        - default
      ports:
        - "8080:8080"
        - "8000:8000"
        - "5000:5000"

    rocket-db:
      container_name: pokemon_rocketdb
      image: mariadb:10.3
      restart: always
      command: ['mysqld', '--character-set-server=utf8mb4', '--collation-server=utf8mb4_unicode_ci']
      environment:
        MYSQL_ROOT_PASSWORD: StrongPassword
        MYSQL_DATABASE: rocketdb
        MYSQL_USER: rocketdb
        MYSQL_PASSWORD: AnotherStrongPassword
        TZ: Europe/Berlin
      volumes:
        - ./volumes/rocketdb:/var/lib/mysql
        - ./docker-entrypoint-initdb:/docker-entrypoint-initdb.d
      networks:
        - default

The docker-compose file defines a set of services.

"mad" service
-----------------

The "mad" service is a docker-container based on the image `mapadroid/map-a-droid <https://hub.docker.com/r/mapadroid/map-a-droid>`_ , which is automatically built by dockerhub whenever a push to the `master` happens, using this `Dockerfile <https://github.com/Map-A-Droid/MAD/blob/master/Dockerfile>`_.

In the docker image, the whole MAD repository is located in "/usr/src/app".

**Volumes:**

* The volumes define what is mounted into the docker-container.
* On one hand we mount the **configuration files (config.ini, mappings.json)** and the **geofences** we need.
* On the other hand we "mount out" the **files/directories produced by MAD**, such as the directory "logs" and also the "files" directory, which contains all calculated routes, position files and stats. As usual, volumes are needed for everything **you do not want to loose** after you take the docker-container down. Without these volumes, MAD would have to recalculate the routes everytime you take your container up.

**Ports:**

* The docker-image exposes ports 8080 (RGC), 8000 (Pogodroid) and 5000 (Madmin) by default.
* We publish these ports and map them on ports of our host. So e.g. https://your-domain.com:8080 will point to port 8080 of the container, 8000 to 8000 and 5000 to 5000. In this case in RGC you would put https://your-domain.com:8080 as target, in pogodroid http://your-domain.com:8000 and madmin would be reachable under https://your-domain.com:5000.

"rocket-db" service
-------------------

The "rocket-db" service is docker-container based on `mariadb:10.3 <https://hub.docker.com/_/mariadb>`.
It will start a mariadb database server and automatically create the defined used :code:`MYSQL_USER` with password :code:`MYSQL_PASSWORD`.

Your job here is to set secure passwords for :code:`MYSQL_ROOT_PASSWORD` and :code:`MYSQL_PASSWORD`.

The database is reachable in the default network as `rocket-db`, so in your config.ini it looks like this:

.. code-block:: none

  dbip: rocket-db                      # IP adress or hostname of the mysql server
  dbusername: rocketdb                 # USERname for database
  dbpassword: AnotherStrongPassword    # Password for that username
  dbname: rocketdb                     # Name of the database

You can see that we mount the directory "docker-entrypoint-initdb" to "/docker-entrypoint-initdb.d/"
All .sql scripts in this directory are executed, once the container starts.

Database deployment
-------------------

Let's deploy the database, shall we?
Just execute:

.. code-block:: bash

  docker-compose up -d rocket-db

This will start the "rocket-db" service and execute rocketmap.sql in docker-entrypoint-initdb.
Take a look at the logs:

.. code-block:: bash

  docker-compose logs -f rocket-db

and verify that the database was initialized without problems.

Deploy MAD
----------

To deploy MAD you just execute

.. code-block:: bash

  docker-compose up -d mad

Look at the logs with:

.. code-block:: bash

  docker-compose logs -f mad

2 Some useful commands to maintain MAD + DB

Useful commands
---------------
**Dump DB:**

.. code-block:: bash

  docker-compose exec -T rocket-db /usr/bin/mysqldump -uroot -pStrongPassword rocketdb  > $(date +"%Y-%m-%d")_rocketmap_backup.sql

**Restore DB:**

.. code-block:: bash

  cat <backup>.sql | docker-compose exec -T rocket-db /usr/bin/mysql -uroot -pStrongPassword rocketdb

**MySQL CLI:**

.. code-block:: bash

  docker-compose exec rocket-db /usr/bin/mysql -uroot -pStrongPassword rocketdb

**Further useful Docker tools:**

* **Router:** `Traefik <https://docs.traefik.io>`_ is recommended, which is really easy to use and also runs as Docker container. To secure the docker-socket (which traefik has access to) we recommend the `docker-socket-proxy <https://github.com/Tecnativa/docker-socket-proxy>`_ by Tecnativa.
* **Automatic updates:** `Watchtower <https://github.com/containrrr/watchtower>`_ is a useful tool which will update your docker-services once there are newer images available
* **Pokealarm, PMSF:** check out our docker-compose used `here <https://github.com/Breee/pogo-map-package>`_
