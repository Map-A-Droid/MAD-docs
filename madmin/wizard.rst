================
Wizard
================

The wizard performs two major functions, download the latest supported versions of packages (PoGo, RGC, PD) and install
the correct support packages through RGC and Smart Jobs.

Package Management
-------------------

The wizard performs package management by checking the sources for new supported versions and notifying there are
updated available via a download icon. The wizard does not run automatically and requires a click on the wizard hat
within MADmin -> Setings -> MADmin Packages. The picture below depicts two PokemonGO versions having available updates
while rgc and PD are up-to-date. To update the packages you can click on the cloud download button or the wizard hat.

.. image:: /_static/wizard/available_packages.png

Smart Downloads
^^^^^^^^^^^^^^^^
The wizard will perform smart-updates for PokemonGO.  For the package to update it must be supported by MAD (via
addresses.json).  If the package is not supported it will not be downloaded.  This prevents MAD from having unsupported
versions of PokemonGO that cannot be used for with PogoDroid.

Smart Jobs
^^^^^^^^^^^
A smart job executes the same as a normal job but with a few additional steps. It will check the architecture of the
device to determine what package needs to be installed on the system. After that it will determine the currently
installed version. If the MAD version is thee same or old it will not install the package. If MAD contains a newer
package it will install the current package on the device


Manual Uploads
^^^^^^^^^^^^^^^
The wizard allows manual uploads to update packages. Prior to upload it validates the package is correct (it performs
this operation by looking at the package name inside the APK) and attempting to validate the package architecture. This
prevents any invalid uploads that could cause devices to think they updated properly due to a mis-matched package.

Reload / Refresh Wizard
------------------------
The reload option allows multi-instance systems to refresh the currently downloaded package. Systems that use a shared
database can click this once the package is downloaded on one system.  For systems that use the filesystem storage
option they must share the same directory for the packages.