========
MADevice
========

`View MADevice on GitHub <https://github.com/georgeherby/MADevice>`_

What is MADevice
----------------

MADevice is a service that will alert you when a device may be having an issue. It can be used if you just want to check the status of numerous devices (phones and Android TVs) across many MAD instances from within Discord without having to load numerous MADmin windows. The following two sections detail each feature available.

No Data Alert
-------------

When running MADevice, it will check the last received time for data from PoGoDroid and then if the time is more than 20 minutes (or the configured duration) in the past, it will post a message to the channel set by webhook in servers.json

.. image:: https://raw.githubusercontent.com/georgeherby/MADevice/master/images/alert.png

On-Demand Status (!status)
--------------------------

If you type :code:`!status` in the channel set by :code:`status_channel_id` in :code:`servers.json`, you get an on-demand update across all servers (set in servers.json) and posted into Discord rather than opening up multiple browsers to see the data.

.. image:: https://raw.githubusercontent.com/georgeherby/MADevice/master/images/status.png

Installation
------------
For up-to-date installation steps visit MADevice's `README <https://github.com/georgeherby/MADevice>`_
