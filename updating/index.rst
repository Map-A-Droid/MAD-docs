.. _sec_updating:

Updating 
========

MAD
---

To update an existing MAD install, first stop MAD (this varies depending on how you run MAD), and then update the git repository.

.. code-block:: bash

  git pull

Then start MAD again.


Devices
-------

There are a lot of ways to update an APK on an Android device, probably the most easy way is to use the :ref:`MADmin Wizard <sec_madmin_wizard>`. 

Good alternatives are:

- ADB (:code:`adb install -r app.apk`)
- Simple MADmin job (Jobs --> Create APK install job)
- Shell scripts like `update_mad.sh <https://github.com/Map-A-Droid/MAD-ATV/blob/master/update_mad.sh>`_
