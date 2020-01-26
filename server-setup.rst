============
Server setup
============

System preparation
==================

.. note::

  This whole article assumes a fresh installed `Ubuntu 18.04 Server <https://www.ubuntu.com/download/server>`_. If you're running another Linux distribution - that's totally fine, but keep in mind there may be some difference to your setup.


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

Install client libraries
------------------------
.. code-block:: bash

  sudo apt install default-libmysqlclient-dev

.. TODO fix internan links

Database schema
---------------

MAD will install the latest database schema automatically on initial boot and no additional steps are required.  It will install the basic RocketMAD tables but may not be completely up to date.  Running RocketMAD for the first time should execute their required changes. Follow the guide from the `official Rocketmap documentation <https://OSM-Rocketmap.readthedocs.io/>`_. 

.. warning::
 Make sure to clone the  `RocketMAD <https://github.com/cecpk/RocketMAD/>`_ fork instead of the normal one.

Python
======

Since Ubuntu 18.04 does comes with a pre-installed python3.6 version but without a pip3 installation, run this command to install it:

.. code-block:: bash

  apt install python3-pip

Make sure you have the right version installed, since even if python3.6 is installed, the `python3` command could still point to `python3.5` or below!
Check if `pip` and `python` is installed correctly by running:

- :code:`python3 --version` - should return 3.6.x
- :code:`pip3 --version` - If it returns a version that is related to your python version, it is working.

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

Configuration
=============

Copy the example config file and rename it to "config.ini":

.. code-block:: bash

  cp configs/config.ini.example configs/config.ini

and edit the config file accordingly.

The next step is to configure MAD via MADmin - the web frontend:

.. code-block:: bash

  python3 configmode.py

By default MADmin will be available on http://your_server_ip:5000. 

Geofences
---------

First you want to add a geofence. You can do that by either drawing a fence on the map (use the icon on the top right corner) or pasting a list of coordinates (Settings --> Geofences).

Areas
-----

Next step is to create an area. Go to Settings --> Areas and click on the green plus. Choose a mode you want to scan (Have a look at the different `scanning modes <../faq#what-s-the-difference-betwen-these-scanning-modes>`_) and fill in the settings.

Walkers
-------

Walkers are responsible for the assignment of the areas to the devices. If you just want a device on one area the whole time, create a walker and add that area with :code:`coords` set as walker mode.

Devices
-------

Add your device and assign it to the walker.

 Every other setting like :code:`Auth`, :code:`IV Lists` and :code:`Shared Settings` are optional.

Running
=======

If everything is set up correctly, you can start MAD:

.. code-block:: bash

  python3 start.py

Deploying behind a Reverse Proxy
================================

MAD supports being run behind a Reverse Proxy.  

NGINX
-----

The reverse proxy relies on the header, :code:`X-Script-Name`, to inform MADmin on how to construct the URIs.  For our examples we will use the following:

- Using NGINX as our reverse proxy
- MADmin runs on localhost
- MADmin uses port 5000
- We wish to access the site at '/madmin'
- The FQDN we are using to access MADmin is 'mapadroid.local'
- We only want files 100MB or less to be uploaded
- SSL Ceritificate is located at /etc/ssl_cert.crt
- SSL Certificate Key is located at /etc/ssl_key.pem

Configuring HTTP
^^^^^^^^^^^^^^^^
MADmin URL: :code:`http://mapadroid.local/madmin`

.. code-block:: bash

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
^^^^^^^^^^^^^^^^^
MADmin URL: :code:`https://mapadroid.local/madmin`

.. code-block:: bash

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

Apache2
-------
Apache does a lot already automatically, but make sure that the module :code:`proxy` and :code:`rewrite` is installed and enabled. This following config shows a setup where every http request will be redirected to https. And the https vhost is forwading the request to MADmin.

If no SSL is needed, paste the two lines starting with `Proxy` to the first code block and delete 443 vhost block plus the rewrite block in the first block.

.. code-block:: bash

  <VirtualHost *:80>

          ProxyPreserveHost On
          ProxyRequests Off
          ServerName madmin.example.com

          ErrorLog ${APACHE_LOG_DIR}/gohildesheim.de_error.log
          CustomLog ${APACHE_LOG_DIR}/gohildesheim.de_access.log combined

          <IfModule mod_rewrite.c>
                  RewriteEngine On
                  RewriteCond %{HTTPS} off
                  RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI} [R=301,L]
          </IfModule>
  </VirtualHost>
  <VirtualHost *:443>

      ProxyPreserveHost On
      ProxyRequests Off

      ServerName madmin.example.com
      ProxyPass / http://localhost:5000/
      ProxyPassReverse / http://localhost:5000/

      SSLEngine on
      SSLCertificateKeyFile /etc/ssl_key.pem
      SSLCertificateFile /etc/ssl_cert.crt

      ErrorLog ${APACHE_LOG_DIR}/madmin_error.log
      CustomLog ${APACHE_LOG_DIR}/madmin_access.log combined
  </VirtualHost>


Docker
======

.. note::
  If you don't know anything about Docker, you probably want ignore this step.

.. warning::
  MAD's Docker support is community driven and untested by MAD's core developers!

Set up Docker
-------------

If you do not have a clue about docker, you maybe want to check out:

 - https://www.docker.com/why-docker
 - https://www.docker.com/resources/what-container

First of all, you have to install Docker CE and docker-compose on your system.

- Docker CE: just execute `this script <https://get.docker.com/>`_ - or read through https://docs.docker.com/install/
- Docker-compose: https://docs.docker.com/compose/install

These sites are well documented and if you follow the install instructions, you are good to go.


Setup MAD and Rocketmap database.
---------------------------------

In this section we explain how to setup MAD and a Rocketmap database using docker-compose.

Preparations
----------------

You can just copy & paste this to do what is written below:

.. code-block:: bash

  mkdir MAD-docker && \
  cd MAD-docker && \
  mkdir mad && \
  mkdir mad/configs && \
  touch docker-compose.yml && \
  mkdir docker-entrypoint-initdb && \
  wget -O docker-entrypoint-initdb/rocketmap.sql https://raw.githubusercontent.com/Map-A-Droid/MAD/master/scripts/SQL/rocketmap.sql && \
  cd mad/configs/ && \
  wget -O config.ini https://raw.githubusercontent.com/Map-A-Droid/MAD/master/configs/config.ini.example && \
  cd ../../

This will:

#. Create a directory `MAD-docker`.
#. Create a file `docker-compose.yml`.
#. Create a directory `MAD-docker/mad`. (here we store MAD related stuff)
#. Create a directory `MAD-docker/mad/configs`. (here we store config files for MAD). Here you store your `config.ini`.
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
        - ./mad/configs/config.ini:/usr/src/app/configs/config.ini
        - ./volumes/mad/files:/usr/src/app/files
        - ./volumes/mad/logs:/usr/src/app/logs
      depends_on:
        - rocketdb
      networks:
        - default
      ports:
        - "8080:8080"
        - "8000:8000"
        - "5000:5000"

    rocketdb:
      container_name: pokemon_rocketdb
      image: mariadb:10.3
      restart: always
      command: ['mysqld', '--character-set-server=utf8mb4', '--collation-server=utf8mb4_unicode_ci', '--innodb_file_per_table=1', '--event-scheduler=ON', '--sql-mode=NO_ENGINE_SUBSTITUTION']
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
* On one hand we mount the **configuration file (config.ini)**.
* On the other hand we "mount out" the **files/directories produced by MAD**, such as the directory "logs" and also the "files" directory, which contains all position files and stats. As usual, volumes are needed for everything **you do not want to loose** after you take the docker-container down.

**Ports:**

* The docker-image exposes ports 8080 (RGC), 8000 (Pogodroid) and 5000 (Madmin) by default.
* We publish these ports and map them on ports of our host. So e.g. http://your-domain.com:8080 will point to port 8080 of the container, 8000 to 8000 and 5000 to 5000. In this case in RGC you would put http://your-domain.com:8080 as target, in pogodroid http://your-domain.com:8000 and madmin would be reachable under http://your-domain.com:5000.

"rocketdb" service
-------------------

The "rocketdb" service is docker-container based on `mariadb:10.3 <https://hub.docker.com/_/mariadb>`.
It will start a mariadb database server and automatically create the defined used :code:`MYSQL_USER` with password :code:`MYSQL_PASSWORD`.

Your job here is to set secure passwords for :code:`MYSQL_ROOT_PASSWORD` and :code:`MYSQL_PASSWORD`.

The database is reachable in the default network as `rocketdb`, so in your config.ini it looks like this:

.. code-block:: none

  dbip: rocketdb                      # IP adress or hostname of the mysql server
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

  docker-compose up -d rocket-b

This will start the "rocketdb" service and execute rocketmap.sql in docker-entrypoint-initdb.
Take a look at the logs:

.. code-block:: bash

  docker-compose logs -f rocketdb

and verify that the database was initialized without problems.

Deploy MAD
----------

To deploy MAD you just execute

.. code-block:: bash

  docker-compose up -d mad

Look at the logs with:

.. code-block:: bash

  docker-compose logs -f mad

Go to `http://your-domain.com:5000` and check if the MADmin is running.


Useful commands
---------------

Some useful commands to maintain MAD + DB

**Dump DB:**

.. code-block:: bash

  docker-compose exec -T rocketdb /usr/bin/mysqldump -uroot -pStrongPassword rocketdb  > $(date +"%Y-%m-%d")_rocketmap_backup.sql

**Restore DB:**

.. code-block:: bash

  cat <backup>.sql | docker-compose exec -T rocketdb /usr/bin/mysql -uroot -pStrongPassword rocketdb

**MySQL CLI:**

.. code-block:: bash

  docker-compose exec rocketdb /usr/bin/mysql -uroot -pStrongPassword rocketdb

**Further useful Docker tools:**

* **Router:** `Traefik <https://docs.traefik.io>`_ is recommended, which is really easy to use and also runs as Docker container. To secure the docker-socket (which traefik has access to) we recommend the `docker-socket-proxy <https://github.com/Tecnativa/docker-socket-proxy>`_ by Tecnativa.
* **Automatic updates:** `Watchtower <https://github.com/containrrr/watchtower>`_ is a useful tool which will update your docker-services once there are newer images available
* **Pokealarm, PMSF:** check out our docker-compose used `here <https://github.com/Breee/pogo-map-package>`_
