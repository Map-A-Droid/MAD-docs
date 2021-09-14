.. _sec_apache2:

Apache2
^^^^^^^^^^^^^^^^

For our examples we will use the following:

- MAD runs on localhost
- :code:`madmin_port` is port 5000
- :code:`ws_port` is 8080
- :code:`mitmreceiver_port` is 8000
- We wish to access MADmin at :code:`madmin.example.com`
- We wish to proxy the RGC traffic to :code:`rgc.example.com`
- We wish to proxy the PogoDroid traffic to :code:`pd.example.com`
- The FQDN (Domain) we are using is :code:`example.com`
- SSL Certificate is located at :code:`/etc/letsencrypt/live/example.com/cert.pem`
- SSL Certificate Key is located at :code:`/etc/letsencrypt/live/example.com/privkey.pem`

Make sure that the module :code:`proxy` and :code:`rewrite` is installed and enabled (:code:`a2enmod proxy proxy_http`).

 Keep in mind to configure the DNS settings correctly to make the three subdomains work.

.. _sec_apache2_madmin:

MADmin
"""""""""""""""""""""""

MADmin URL: :code:`https://madmin.example.com`

.. code-block:: bash

  <VirtualHost *:443>

      ProxyPreserveHost On
      ProxyRequests Off

      ServerName madmin.example.com
      ProxyPass / http://localhost:5000/
      ProxyPassReverse / http://localhost:5000/

      SSLEngine on
      SSLCertificateKeyFile /etc/letsencrypt/live/example.com/privkey.pem
      SSLCertificateFile /etc/letsencrypt/live/example.com/fullchain.pem

      ErrorLog ${APACHE_LOG_DIR}/madmin_error.log
      CustomLog ${APACHE_LOG_DIR}/madmin_access.log combined
  </VirtualHost>

.. _sec_apache2_rgc:

RGC
"""""""""""""""""""""

Please install the websocket apache module: :code:`a2enmod proxy_wstunnel`

RGC URL: :code:`wss://rgc.example.com`

.. code-block:: bash

  <VirtualHost *:443>
      ServerName rgc.example.com

      ProxyPass / ws://127.0.0.1:8080/
      ProxyPassReverse / ws://127.0.0.1:8080/

      SSLEngine on
      SSLCertificateKeyFile /etc/letsencrypt/live/example.com/privkey.pem
      SSLCertificateFile /etc/letsencrypt/live/example.com/fullchain.pem

      ErrorLog ${APACHE_LOG_DIR}/rgc_error.log
      CustomLog ${APACHE_LOG_DIR}/rgc_access.log combined
  </VirtualHost>

.. _sec_apache2_pd:

PogoDroid
""""""""""""""""""""

PogoDroid URL: :code:`https://pd.example.com`

.. code-block:: bash

  <VirtualHost *:443>
      ServerName pd.example.com

      ProxyPass / http://127.0.0.1:8000/
      ProxyPassReverse / http://127.0.0.1:8000/

      SSLEngine on
      SSLCertificateKeyFile /etc/letsencrypt/live/example.com/privkey.pem
      SSLCertificateFile /etc/letsencrypt/live/example.com/fullchain.pem

      ErrorLog ${APACHE_LOG_DIR}/pd_error.log
      CustomLog ${APACHE_LOG_DIR}/pd_access.log combined
  </VirtualHost>
