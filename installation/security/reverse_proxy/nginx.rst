.. _sec_nginx:

NGINX
^^^^^^^^^^^^^^^

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

.. _sec_nginx_ssl:

SSL
""""""""""""""""""""

Every proxy endpoint will be encrypted with SSL, make sure to adjust the path:

.. code-block:: bash

  ssl_certificate /etc/letsencrypt/live/example.com/cert.pem;
  ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

.. _sec_nginx_madmin:

MADmin
""""""""""""""""""""""

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

.. _sec_nginx_rgc:

RGC
"""""""""""""""""""

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


.. _sec_nginx_pd:

PogoDroid
""""""""""""""""""

PogoDroid URL: :code:`https://example.com/pd` (note the extra S in the protocol).

.. code-block:: bash

  location /pd {
    proxy_pass http://localhost:8000/;
    proxy_set_header X-Real-IP  $remote_addr;
    proxy_set_header X-Forwarded-For $remote_addr;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-Proto $scheme;
  }
