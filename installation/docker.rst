==============
Docker
==============

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


Setup MAD and RocketMAD database.
---------------------------------

In this section we explain how to setup MAD and a RocketMAD database using docker-compose.

Preparations
------------

You can just copy & paste this to do what is written below:

.. code-block:: bash

  mkdir MAD-docker && \
  cd MAD-docker && \
  mkdir mad && \
  mkdir mad/configs && \
  mkdir rocketdb && \
  touch rocketdb/my.cnf && \
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
#. Create a directory `MAD-docker/rocketdb`. (here we store config files for mariaDb). Here you store your `my.cnf`.
#. Create a directory `MAD-docker/docker-entrypoint-initdb`
#. Download the RocketMAD Database Schema: https://raw.githubusercontent.com/Map-A-Droid/MAD/master/SQL/rocketmap.sql and store it in the directory `docker-entrypoint-initdb`.

Your directory should now look like this:

.. code-block:: python

  MAD-docker/
    docker-compose.yml
    docker-entrypoint-initdb/
      rocketmap.sql
    mad/
    rocketdb/
      my.cnf
    configs/
      config.ini

Writing the mariadb config file
-------------------------------
Fill rocketdb/my.cnf file with the following content.

.. code-block:: bash

  [mysqld]
  innodb_buffer_pool_size=1G

.. note::
You should align this setting with you available memory. It should probably not exceed 50% of your available memory.


Decrease VM swappiness
----------------------
.. code-block:: bash

  sysctl -w vm.swappiness=1

.. note::
For further details have a look at https://mariadb.com/kb/en/configuring-swappiness/


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
        - ./personal_commands:/usr/src/app/personal_commands
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
      image: mariadb:10.4
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
        - ./rocketdb:/etc/mysql/mariadb.conf.d
      networks:
        - default

The docker-compose file defines a set of services.

"mad" service
-------------

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
------------------

The "rocketdb" service is docker-container based on `mariadb:10.4 <https://hub.docker.com/_/mariadb>`.
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

  docker-compose up -d rocketdb

This will start the "rocketdb" service and execute rocketmap.sql in docker-entrypoint-initdb.
Take a look at the logs:

.. code-block:: bash

  docker-compose logs -f rocketdb

and verify that the database was initialized without problems.

Installing a webfrontend
------------------------

Add a webfrontend like RocketMAD or PMSF to your setup by just adding another container to the docker-compose.yml. Make sure to adjust the config files just like the MAD config.

RocketMAD
^^^^^^^^^

.. code-block:: bash

      rocket-mad:
        container_name: pokemon_rocketmad
        build:
            context: ./RocketMAD
        restart: always
        volumes:
            - /etc/timezone:/etc/timezone:ro
            - /etc/localtime:/etc/localtime:ro
            - ./RocketMAD/config/config.ini:/usr/src/app/config/config.ini
        depends_on:
            - rocketdb
        networks:
            - default
        ports:
            - "5500:5000"

Clone the project into the MAD-docker directory: :code:`git clone https://github.com/cecpk/RocketMAD`. This docker-compose file will expose RocketMAD on port :code:`5500`, but the internal routing is still on port :code:`5000`, so don't change that in the config. Make sure to re-build the container after updating RocketMAD: :code:`docker-compose build rocket-mad`.

PMSF
^^^^

.. code-block:: bash

      pmsf:
        container_name: pokemon_pmsf
        build:
            context: ./PMSF
        restart: always
        volumes:
            - ./PMSF/access-config.php:/var/www/html/config/access-config.php
            - ./PMSF/config.php:/var/www/html/config/config.php
        depends_on:
            - rocket-db
        networks:
            - default
        ports:
            - "80:80"

Download the three required files from the PMSF repository:

.. code-block:: bash

  mkdir PMSF && \
  cd PMSF && \
  wget https://raw.githubusercontent.com/pmsf/PMSF/master/Dockerfile && \
  wget -O config.php https://raw.githubusercontent.com/pmsf/PMSF/master/config/example.config.php && \
  wget -O access-config.php https://raw.githubusercontent.com/pmsf/PMSF/master/config/example.access-config.php

PMSF will run on port :code:`80`. Consider using some sort of reverse proxy!

Make sure to re-build the container after updating PMSF: :code:`docker-compose build pmsf`.

.. note::

  For more informations and a best practice example, check out the docker-compose used `here <https://github.com/Breee/pogo-map-package>`_


Using Traefik 2 as router
-------------------------

If you use Docker, we recommend to use Traefik 2 as router. It is easy to configure, easy to use and it handles alot of things for you,
like SSL certificates, service discovery, load balancing.
We will not explain, how you deploy a Traefik on your server, but we give you a production ready example for your docker-compose.yml,
In this example, we assume:

- your Traefik is connected to a docker-network `proxy`,
- your domain is `example.com` and
- you use a config similar to this:

.. code-block:: yaml

  api:
    dashboard: true

  providers:
    docker:
      endpoint: "unix:///var/run/docker.sock"
      exposedByDefault: false
      network: proxy


  entryPoints:
    web:
      address: :80
      http:
        redirections:
          entryPoint:
            to: websecure
            scheme: https

    websecure:
      address: :443
      http:
        tls:
          certResolver: letsEncResolver


  certificatesResolvers:
    letsEncResolver:
      acme:
        email: bree@example.com
        storage: acme.json
        httpChallenge:
          entryPoint: web

We define the labels as follows:

.. code-block:: yaml

  version: '2.4'
  services:
    mad:
      container_name: pokemon_mad
      image: mapadroid/map-a-droid
      init: true
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
        - proxy
      labels:
        - "traefik.enable=true"
        - "traefik.http.middlewares.redirect-to-https.redirectscheme.scheme=https"
        - "traefik.http.routers.madmin.rule=Host(`madmin.example.com`)"
        - "traefik.http.routers.madmin.service=madmin"
        - "traefik.http.services.madmin.loadbalancer.server.port=5000"
        - "traefik.http.routers.pogodroid.rule=Host(`pogodroid.example.com`)"
        - "traefik.http.routers.pogodroid.service=pogodroid"
        - "traefik.http.services.pogodroid.loadbalancer.server.port=8000"
        - "traefik.http.routers.rgc.rule=Host(`rgc.example.com`)"
        - "traefik.http.routers.rgc.service=rgc"
        - "traefik.http.services.rgc.loadbalancer.server.port=8080"

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

  networks:
    proxy:
      external: true

Using these labels, traefik now will:
  - route `https://madmin.example.com` to port 5000 (MADmin Flask app).
  - route `https://pogodroid.example.com` to port 8000 (Pogodroid listener).
  - route `https://rgc.example.com` to port 8080 (RGC listener).

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

Further steps
-------------

Review and implement anything related to the `security section <./security>`_
