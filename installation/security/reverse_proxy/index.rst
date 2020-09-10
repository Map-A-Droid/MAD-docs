-----------------
.. _sec_revprox:

Reverse Proxy
-------------

If you are securing your MAD setup with SSL proxies, you can change the IPs from the default listeners (MADmin, RGC and PogoDroid) to localhost. MAD opens on :code:`0.0.0.0` by default which means every network interface. But since we are using a webserver proxy, those ports don't need to be exposed on a different interface than localhost (if the proxy is running locally):

.. code-block:: bash

  ws_ip: localhost
  mitmreceiver_ip: localhost
  madmin_ip: localhost

The current proxies have configuration examples:

.. toctree::
  :glob:
  :maxdepth: 1

  *