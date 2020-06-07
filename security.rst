========
Security
========

There are several ways to improve a MAD setup in terms of security.

The three ports used by MAD (defaults are 5000 for MADmin, 8080 for RGC and 8000 for PogoDroid) are running on every network interface by default. That means that every IP address or domain pointing to your server will listen on those ports. The connections are unencrypted and readable by everyone that can access them between you and your server. But luckely, every connnection can be SSL encrypted with a reverse proxy.

NGINX and Apache2 are the most common used Proxies. You decide which one to use, both can do the same things when it comes to MAD.

MADmin
======

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
Apache does a lot already automatically, but make sure that the module :code:`proxy` and :code:`rewrite` is installed and enabled (:code:`a2enmod proxy proxy_http`). This following config shows a setup where every http request will be redirected to https. And the https vhost is forwading the request to MADmin.

If no SSL is needed, paste the two lines starting with `Proxy` to the first code block and delete 443 vhost block plus the rewrite block in the first block.

.. code-block:: bash

  <VirtualHost *:80>

          ProxyPreserveHost On
          ProxyRequests Off
          ServerName madmin.example.com

          ErrorLog ${APACHE_LOG_DIR}/madmin_error.log
          CustomLog ${APACHE_LOG_DIR}/madmin_access.log combined

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


RGC
===

RGC is using a websocket connection to MAD. Websockets can be encrypted as well via NGINX or Apache2. 

Make sure to change the Websocket URI in the RGC settings to :code:`wss://rgc.example.com/` (note the extra S in the protocol).

NGINX
-----

((Please someone tell me, i barely use NGINX lol))

Apache2
-------

Please install the websocket apache module: :code:`a2enmod proxy_wstunnel`

.. code-block:: bash

  <VirtualHost *:443>
      ServerName rgc.example.com

      ProxyPass / ws://127.0.0.1:8080/
      ProxyPassReverse / ws://127.0.0.1:8080/

      SSLEngine on
      SSLCertificateKeyFile /etc/ssl_key.pem
      SSLCertificateFile /etc/ssl_cert.crt

      ErrorLog ${APACHE_LOG_DIR}/rgc_error.log
      CustomLog ${APACHE_LOG_DIR}/rgc_access.log combined
  </VirtualHost>


PogoDroid
===

PogoDroid is using a HTTP(S) connection to MAD. So its just like a normal Reverse Proxy like for MADmin for example. 

Make sure to change the POST destination settings in the PogoDroid settings to :code:`https://pd.example.com/` (note the extra S in the protocol).

NGINX
-----

((Please someone tell me, i barely use NGINX lol))

Apache2
-------

.. code-block:: bash

  <VirtualHost *:443>
      ServerName pd.example.com

      ProxyPass / http://127.0.0.1:8000/
      ProxyPassReverse / http://127.0.0.1:8000/

      SSLEngine on
      SSLCertificateKeyFile /etc/ssl_key.pem
      SSLCertificateFile /etc/ssl_cert.crt

      ErrorLog ${APACHE_LOG_DIR}/pd_error.log
      CustomLog ${APACHE_LOG_DIR}/pd_access.log combined
  </VirtualHost>
