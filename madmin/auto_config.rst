.. _sec_auto_conf:

Auto-Configuration
===================

Auto-Configuration supports (mostly) automatic configuration / provisioning of devices after flashing. Currently the
only implementation of this is 64bit MAD-ATV ROMs. The supported device list can be found `here <https://github.com/Map-A-Droid/MAD-device-list>`_.

Requirements
-------------
There are several requirements that must be met prior to using auto-configuration.

.. TODO use refs vs links
.. TODO document MITM endpoints for autoconfig

- One or more `walkers </madmin/settings.html#Walker>`_ must be configured
- PogoDroid must be configured
- RemoteGPSController must be configured
- Packages must be available in the `Wizard </madmin/wizard.html>`_
- The device must support the MITM endpoints

.. image:: ../_static/autoconfig/example_error.png

Package Configuration
----------------------
PogoDroid and RemoteGPSController are required to be configured prior to the auto-configuration process. This is
accomplished by editing the configuration files located in System -> Auto-Config -> PogoDroid Configuration /
RemoteGPSController Configuration. The defaults are populated with ATV recommended defaults.

Automated Provisioning
-----------------------
If the requirements have been met the device is ready to be auto-provisioned. If there are any requirements that are
missing the session cannot be accepted in MADmin. After the device makes the initial session registration it can be
accepted in two different ways.

* Automatic origin assignment

  * Generate an origin via origin_hopper
  * If :code:`autoconfig_no_auth` is not set a google login must be available

* Manual Assignment

  * Pick an origin from all configured devices
  * Logins are not required regardless of the setting :code:`autoconfig_no_auth`

Default Configuration
^^^^^^^^^^^^^^^^^^^^^^
While each implementation may require a different configuration for intially creating the session, a default configuration
file can be automatically generated from MADmin for use with MADROM. This file needs to be placed on the USB stick prior
to powering on the ATV for the automatic configuration to occur.

Logging
^^^^^^^^^
Messages are logged through the auto-configuration process and viewable in MADmin by click on the history icon. The
default behavior of calling the auto configuration endpoints will produce a log. Devices can implement additional logging
to give a better indication of the progress of the device. An example log can be found below

.. image:: ../_static/autoconfig/autoconfig_log.png