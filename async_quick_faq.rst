.. _sec_asyncfaq:


ASYN Migration Quick FAQ
=====

First steps
----

Backup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are updating from ``legacy/master`` to ``async`` please create a backup of your current working MAD setup. Backup of database, backup of files, backup of nginx/apache2 settings - etc. Have a backup, backup is important, full backup - the more the better. Backup, yes. Backup.

async/architecture changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you running more than **15 (your mileage may vary) devices** you probably need to run some extra MITM Receivers. If you are not near this number you can skip reading this point here - as you will just use single ``start.py`` and everything will be easier. 
MAD is now split into 4 parts:
 - ``start_core.py`` this is main part of MAD that handles websockets/login flow/routes/madmin etc.
 - ``start_mitmreceiver.py`` this is part of MAD that process data received from PD and puts that in MySQL/database. This is the heaviest (CPU usage) part of MAD as it runs 24/7 and do a lot. 
 - ``start_mitmapper.py`` this is helper part
 - ``start_statshandler.py`` this is just stats part
There is also:
 - ``start.py`` that starts everything above in one single process, but that also means it's limited to 1 vCPU/core so if you throw too many devices at that it will struggle to keep up.

There will be some examples how to run `Multiply MITM RECEIVERS`_.

config.ini changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are some outdated settings like ``weather``, ``madmin_login``, ``madmin_password`` that need to be deleted. There is new setting called ``apk_storage_interface`` that need to be set to ``db`` or ``fs`` in ``config.ini``. You can read the description in ``config.ini.example``. Also please set ``mitmmapper_type: redis``. Remember that commented out lines (``#`` first in that line) are commented out and it will not use those.

Software needed before
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **at least** ``python3.9`` - most modern systems have that in repository (`apt install python3.9` for example) or for older one you can most likely install it from external repositories like `deadsnakes <https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/#installing-python-39-on-ubuntu-with-apt>`_. Before going to install anything check what is your current python version installed - it could be already there - try running ``python3.9 --version`` and ``python3 --version``. Remember to install ``python3[.9]-dev python3[.9]-venv python3[.9]-opencv`` packages.
- redis-server installed (``apt install redis``) - it's required now, this does not any configuration by default, just install.
- `venv, python-venv, virtualenv` - use venv, not local packages, not global packages, use venv, really, it makes life easier for everyone. TODO_LINK_HERE_TO_MANUAL_INSTALL_MAD_DOCS_VENV
- ``tesseract``, database ``MariaDB/MySQL`` is still there and if you are just updating you should have all of this.
- list of packages needed for Debian 11 clean install - do NOT blindly-copy paste this - this is just for reference ``python3-dev python3-venv mariadb-server redis mariadb-client build-essential git default-libmysqlclient-dev python3-opencv tesseract-ocr``
 
Migration
----

Migration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are some (a lot!) of changes between versions and migrations are sometimes funky - please take a look at `Common problems`_ if you hit any error/problem. All the ports and endpoints (ws:// http://) stays the same.

- Step 1: Create Backup. Backup - first point in this Quick FAQ.
- Step 2: There are breaking `PogoAuth changes`_ so before running migration make sure there is only one (currently logged in on device) account mapped to single device in MADMin **Pogo Auth** section.
- Step 3: Stop current legacy/master MAD.
- Step 4: You don't want to waste 30 minutes on MAD/MySQL changing the ``pokemon`` and ``pokemon_display`` tables because you have 17851758 / 6 months of mons history there! Clear those up: ``TRUNCATE`` or ``DELETE FROM`` if you don't do it already automagically.
- Step 5: Remove ``update_log.json`` file from MAD master/legacy main directory.
- Step 6: Run ``git checkout async`` from MAD master/legacy main directory.
- Step 7: Run ``git status`` from MAD master/legacy main directory, it should show:
::

	On branch async
	Your branch is up to date with 'origin/async'.
- Step 8: Adjust config.ini (`config.ini changes`_)
- Step 9: Install new requirmements in python3.9 (`virtualenv </en/async/installation/manual/#virtual-environment>`_)
- Step 10: Start ``start.py`` via python3.9 venv manually (not crontab, systemd, supervisor or any type of script) - just for first time to see if there are any errors/problems and to make sure you will see everything.
- Step 11: If everything working go to **Pogo Auth** in MADmin and edit level of your accounts to real level (so 30+)
- Step 12: Password protect MADMin if not running via VPN/LAN `MADmin password/login`_
- Step 13: Update PD and RGC on all devices - ``async`` have dedicated version of those programs. You can do it via Wizzard/MADMin Packages (if ATV), Jobs, manually - whatever you like more. `Links to apks <https://github.com/Map-A-Droid/MAD/blob/async/mapadroid/utils/global_variables.py#L6>`_


Multiply MITM RECEIVERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you run more than **15** devices you probably need this. In ``master/legacy`` you started more instances - in ``async`` you start more mitm receivers that process data within the same instance.
Few examples how this works: `<https://github.com/Map-A-Droid/MAD/blob/async/asyncio_readme.md>`_ or `<https://github.com/spammer23/MAD/blob/async_quest_layers/async_SimpleSetup.md>`_

This part is little more tricky as you need to start muliply mitm receivers and distribute data to those. In a nutshell you should put load balancer/proxy and make that connect to your mitm receivers. Links above should show you how to handle most common setups (apache2/nginx), but feel free to ask on Discord if you having any problems/questions regarding this.



PogoAuth changes
----
Due to latest N behavior changes (BSOD / maintenance screen) and limiting number of mon encounters per account within some <time period> there is now a need for changing accounts on devices. MAD can fully handle PTC accounts and semi-handle Google accounts.
PogoAuth section is now a list/repository of all accounts you have. MAD uses this list to automagically select valid (non banned/non maintenance/non cooldown) accounts. You need to have proper account levels there - if you are just migrating it was imported with levels 0/1 and MAD won't login into those accounts when running `mon_mitm/iv_mitm/raids_mitm` - those need higher (30/8) levels. Please adjust those levels manually via MADMin or SQL query.

PTC only
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you running PTC only then you make sure levels in **Pogo Auth** settings are set to 30+. You also need to remember about PTC login limits so (beta-testing) ``enable_login_tracking`` in ``config.ini`` could be an option or running bunch of proxies to have different IPs there.

Google only
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

MAD (atm) does not handle directly login into Google Accounts so you either had them logged in earlier via autoconfig or you did it manually. It's like that mostly because Google is picky with security and there is a lot of different things that can go wrong if you decided to login multply account within short period of time - some extra checks, temp bans etc. Because of those limitations MAD now need to know **which account is on which device** so on top of having your accounts listed in **Pogo Auth** (with correct level!) you also need to tell MAD how to map does - go to MADmin Settings -> Devices and fill the ``ggl_login_mail`` with correct accounts. You don't do it via **Pogo Auth** section, you do it via ``ggl_login_mail`` in specific Device settings. Yes, you can have multiply accounts in ``ggl_login_mail``, but those **need** to be already logged in on device. Remember about setting correct levels on those accounts.


Mixed (PTC and Google)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

MAD will first try to use Google accounts mapped via ``ggl_login_mail`` and then use PTC accounts if those Google one are on maintenance. Please read both bullet points above :-)


Minimum Level
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All accounts in **Pogo Auth** section need to have correct level set up. MAD need accounts level 30+ for Quests/Mons so it won't even try to login into lower level accounts. Remember to set level manually if you migrated or set it correctly when adding new accounts. MAD **will** log into lower levels account if it's running **Levelup Quest Mode** and update/increase levels.


Maintenance/Flag/Hourglass
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Accounts hit by BSOD / maintenance screen have current timestamp saved into database and they are deemed **not valid to use** for next 24 hours - this is for how long (most of the times, Niantic) accounts are not usuable at all. There are some icons you can hover/click in **Pogo Auth** section to give you an idea when it happen/what is the status.



MADmin password/login
----

Old system using ``madmin_password`` and ``madmin_login`` is gone - you should remove those entries from ``config.ini``. You can now password-protect MADmin via built-in auth levels or externally via nginx/apache2. 
Both systems have pros and cons, so you should decide on one, there is no "better" system, but personally because I don't share my MADMin or don't have a public quest page I prefer the nginx/apache2 proxy.

- Using MAD built-in auth system:
If you decided to use built-in MAD system you need to add new user via MADMin Settings -> Auth with ``MADMIN_ADMIN`` permissions and enable/uncomment ``madmin_enable_auth`` in ``config.ini``. Restart MAD and it's all done.

- Using nginx/apache2 proxy:
You need to use standard Basic Authentication for nginx/apache2. Example config for nginx is included in https://github.com/Map-A-Droid/MAD/blob/async/configs/examples/nginx/foo.conf#L56
::

        auth_basic "Restricted";
        # Please to use basic auth...
        auth_basic_user_file /etc/nginx/.htpasswd_mad;


For apache2 it's very similar:
::

    <Proxy *>
        Order deny,allow
        Allow from all
        Authtype Basic
        Authname "Password Required"
        AuthUserFile /etc/apache2/.htpasswd_mad
        Require valid-user
    </Proxy>

To create .htpasswd_mad file you use ``htpasswd`` program (from ``apache2-utils`` system repository package) via
::

   [sudo] htpasswd  -c /etc/apache2/.htpasswd_mad USERNAME_HERE
   [sudo] htpasswd  -c /etc/nginx/.htpasswd_mad USERNAME_HERE
it will ask for password twice and then create a file for you.

Remember to restart nginx/apache2 after changes.


Common problems
----

I can't find X in config.ini, I am missing settings, where is madmin_enable_auth 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please open ``config.ini.example`` to see everything it's there and then copy-paste specific section/settings to ``config.ini`.
``git pull` cannot overwrite **yours** config.ini because it would be a total mess and you would need to restore that file every update.


init mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**init mode settings?** - init mode have a dedicated type now - just create new area using **Init scanner ``init``mode.
You can specify what **type** you are interested - ``forts`` will jump every ~500 meters and add all pokestops/gyms to database and hardly any spawnpoints as those are visibly only within ~50 meters. ``mons`` will jump every ~50 meters and add a lot of more spawnpoints, but it will have a lot of more jumps/stops/position on route.

unrecognized argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**unrecognized argument** when starting MAD ``start.py: error: unrecognized arguments: --madmin_user= --weather`` it means that this arguments (``madmin_user``, ``weather``) is need to be deleted from new ``config.ini`` as it is not supported anymore.

ortools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**ortools** ortools speedup route calculation but it's not ``requierments.txt`` by default so you just need to install it in your **venv**

Wizzard/APK problems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you get **[W] Unable to save/upload apk: (pymysql.err.InterfaceError) (0, 'Not connected')** in logs while trying to Wizzard PD/POGO you most likely need to update MySQL/MariaDB settings in /etc/mysql/mariadb.conf.d/50-server.conf for max_allowed_packet to something like 256M, restart MySQL/MariaDB after that.
