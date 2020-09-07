.. _sec_madmin_settings:

Area
======
An area defines the scanning type and location that will occur. For more information on scanning types can be found
`here </faq#what-s-the-difference-betwen-these-scanning-modes>`_.

Dependencies:

 * Geofence
 * IV List


Auth
=====
An auth defines credentials used for devices to talk to RGC / MITM. While not required it is highly recommended to use
for hardening the system.


Device
=======
A device is how an android device associated with MAD. This is accomplished through the Origin field and states what
properties it should inherit when performing its required tasks.

Dependencies:

 * PoGo Auth
 * Shared Settings
 * Walker


Geofence
=========
A geofence contains the constrains in which an area is responsible for mapping. Geofences can overlap without any issues
but that does lead to the overlap being scanned twice. When creating a geofence you can specify multiple areas within the
fence by using the identifier tag.

A geofence with a single unnamed polygon

::

  38.892068305429156,-77.0394802093506
  38.89540845718734,-77.03945875167848
  38.89544185791166,-77.03368663787843
  38.89225201785808,-77.03372955322267

A geofence with a single named polygon

::

  [the ellipse]
  38.892068305429156,-77.0394802093506
  38.89540845718734,-77.03945875167848
  38.89544185791166,-77.03368663787843
  38.89225201785808,-77.03372955322267


A geofence with a two named polygons

::

  [the ellipse]
  38.892068305429156,-77.0394802093506
  38.89540845718734,-77.03945875167848
  38.89544185791166,-77.03368663787843
  38.89225201785808,-77.03372955322267
  [whitehouse]
  38.898072115622966,-77.0379674434662
  38.897036724213834,-77.0379674434662
  38.896865549179935,-77.03502774238588
  38.89828921190713,-77.03500628471376


IV List
========
An IV list defines the pokemon and order you will encounter mons. The higher on the list the higher priority they have
to be encountered. MAD will encounter two per jump which is why setting the priority of the pokemon is important.

Pogo Auth
==========
A PoGo Auth defines a way to login to Pokemon Go. The auth is assigned to the device and used during
:ref:`Auto-Configuration / Provisioning <sec_auto_conf>` of devices.

Shared Setting
================
A Shared Setting is a additional configuration that can be applied to a one or more devices. These values are
overwritten if set on the device configuration page.

Walker
========
A walker defines a group of areas on when they will run. This allows a device to perform multiple different scanning
types. For example, a device can scan quests between 0200 - 0400 then switch to scanning pokemon.
