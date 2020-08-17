========
Security
========

There are several ways to improve a MAD setup in terms of security.

The three ports used by MAD (defaults are 5000 for MADmin, 8080 for RGC and 8000 for PogoDroid) are running on every network interface by default. That means that every IP address or domain pointing to your server will listen on those ports. Those connections are unencrypted and readable by everyone that can access them between you and your server. But luckily, every connection can be SSL encrypted with a reverse proxy.

`NGINX <http://nginx.org/en/docs/beginners_guide.html>`_ and `Apache2 <https://gridscale.io/en/community/tutorials/apache-server-reverse-proxy-ubuntu/>`_ are the most common used webservers that can proxy. You decide which one to use, both can do the same things when it comes to MAD.

It's advised to use proper SSL certificates and not sign them by yourself. Let's Encrypt is a great option for that. Read about `certbot here <https://certbot.eff.org>`_ to find out how to use it.

NGINX
=====

For our examples we will use the following:

- MAD runs on localhost
- :code:`madmin_port` is port 5000
- :code:`ws_port` is 8080
- :code:`mitmreceiver_port` is 8000
- We wish to access MADmin at :code:`example.com/madmin`
- We wish to proxy the RGC traffic to :code:`example.com/rgc`
- We wish to proxy the PogoDroid traffic to :code:`example.com/pd`
- The FQDN (Domain) we are using is :code:`example.com`
- SSL Certificate is located at :code:`/etc/letsencrypt/live/example.com/cert.pem`
- SSL Certificate Key is located at :code:`/etc/letsencrypt/live/example.com/privkey.pem`

SSL
---

Every proxy endpoint will be encrypted with SSL, make sure to adjust the path:

.. code-block:: bash

  ssl_certificate /etc/letsencrypt/live/example.com/cert.pem;
  ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

MADmin
------

The reverse proxy relies on the header, :code:`X-Script-Name`, to inform MADmin on how to construct the URIs.

MADmin URL: :code:`https://example.com/madmin`

.. code-block:: bash

  location ~ /madmin(.*)$ {
      proxy_set_header X-Real-IP  $remote_addr;
      proxy_set_header X-Forwarded-For $remote_addr;
      proxy_set_header X-Forwarded-Proto https;
      proxy_set_header X-Script-Name /madmin;
      proxy_set_header Host $host;
      proxy_pass http://localhost:5000$1$is_args$args;
      client_max_body_size 200M;
  }


RGC
---

RGC URL: :code:`wss://example.com/rgc` (note the extra S in the protocol).

.. code-block:: bash

  location /rgc {
    proxy_pass http://localhost:8080;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

    # WebSocket support
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
  }


PogoDroid
---------

PogoDroid URL: :code:`https://example.com/pd` (note the extra S in the protocol).

.. code-block:: bash

  location /pd {
    proxy_pass http://localhost:8000/;
    proxy_set_header X-Real-IP  $remote_addr;
    proxy_set_header X-Forwarded-For $remote_addr;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-Proto $scheme;
  }


Apache2
=======

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

MADmin
------

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

RGC
---

Please install the websocket apache module: :code:`a2enmod proxy_wstunnel`

RGC URL: :code:`https://rgc.example.com`

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

PogoDroid
---------

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


Further Steps
=============

If you have successfully secured your MAD setup with SSL proxies, you can now change the IPs from the three ports (MADmin, RGC and PogoDroid) to localhost. MAD opens up those ports by default on :code:`0.0.0.0` which means every network interface. But since we are using a webserver proxy, those ports don't need to be exposed on a different interface than localhost:

.. code-block:: bash

  ws_ip: localhost
  mitmreceiver_ip: localhost
  madmin_ip: localhost

General Security Advice
========================

Here is some security advice that is not only related to MAD but to servers and software hosting in general.

- Don't run MAD inside a webhosted directory like :code:`/var/www/html`.
- MAD does not need root privileges to run. Start it as a normal user. The only programs that need root are your webserver and your database.
- Don't use the same or similar passwords. A `password manager <https://keepass.info/>`_ can be useful for that.

Firewall
--------

It's always a good idea to open as few ports as possible. In MADs case that's only 22 for SSH (even that is not 100% necessary in some cases), 80 and 443 for a Webserver if you are proxying everything. Read more about :code:`iptables` `here <https://www.hostinger.com/tutorials/iptables-tutorial>`_.

SSH Authentication
------------------

Follow this `guide <https://www.howtogeek.com/443156/the-best-ways-to-secure-your-ssh-server/>`_ and install `fail2ban <https://www.techrepublic.com/article/how-to-install-fail2ban-on-ubuntu-server-18-04/>`_.
