.. _sec_faq_async:

ASYNC FAQ
===

First steps
-------

Backup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are updating from `legacy/master` to `async` please create a backup of your current working MAD setup. Backup of database, backup of files, backup of nginx/apache2 settings - etc. Have a backup, backup is important, full backup - the more the better. Backup, yes. Backup.

async/architecture changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you running more than **15 (your mileage may vary) devices** you probably need to run some extra MITM Receivers. If you are not near this number you can skip reading this point here - as you will just use single `start.py` and everything will be easier. 
MAD is now split into 4 parts:
- `start_core.py` this is main part of MAD that handles websockets/login flow/routes/madmin etc.
- `start_mitmreceiver.py` this is part of MAD that process data received from PD and puts that in MySQL/database. This is the heaviest (CPU usage) part of MAD as it runs 24/7 and do a lot. 
- `start_mitmapper.py` this is helper part
- `start_statshandler.py` this is just stats part
There is also:
- `start.py` that starts everything above in one single process, but that also means it's limited to 1 vCPU/core so if you throw too many devices at that it will struggle to keep up.

There will be some examples how to run extra MITM Receivers below. TODO_LINK_TO_MULTI_MITM_RECEIVERS

config.ini changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
There are some outdated settings like `weather`, `madmin_login`, `madmin_password` that need to be deleted. There is new setting called `apk_storage_interface` that need to be set to `db` or `fs` in `config.ini`. You can read the description in `config.ini.example`. Also please set `mitmmapper_type: redis`. Remember that commented out lines (`#` first in that line) are commented out and it will not use those.

If you end with something like that when starting MAD: `start.py: error: unrecognized arguments: --madmin_user= --weather` it means that this arguments (`madmin_user`, `weather`) is need to be deleted from new config.ini as it is not supported anymore.

Software needed before
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 - ***at least*** `python3.9` - most modern systems have that in repository (`apt install python3.9` for example) or for older one you can most likely install it from external repositories like [ deadsnakes ](https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/#installing-python-39-on-ubuntu-with-apt). Before going to install anything check what is your current python version installed - it could be already there - try running `python3.9 --version` and `python3 --version`. Remember to install `python3[.9]-dev python3[.9]-venv python3[.9]-opencv`
 - redis-server installed (`apt install redis`) - it's required now, this does not any configuration by default, just install.
 - `venv, python-venv, virtualenv` - use venv, not local packages, not global packages, use venv, really, it makes life easier for everyone. TODO_LINK_HERE_TO_MANUAL_INSTALL_MAD_DOCS_VENV
 - `tesseract`, database `MariaDB/MySQL` is still there and if you are just updating you should have all of this.
 - list of packages needed for Debian 11 clean install - do NOT blindly-copy paste this - this is just for reference `python3-dev python3-venv mariadb-server redis mariadb-client build-essential git default-libmysqlclient-dev python3-opencv tesseract-ocr`
 
Migration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
There are some (a lot!) of changes between versions and migrations are sometimes funky - please take a look at TODO_LINK_TO_COMMON_PROBLEMS bottom of this page if you hit any error problem.
 - Step 1: Create Backup. Backup - first point in this Quick FAQ.
 - Step 2: There are breaking changes to `PoGo Auth` section so before running migration make sure there is only one (currently logged in on device) account mapped to single device. (TODO_LINK_TO_POGOAUTH_CHANGES)
 - Step 3: Stop current `legacy/master` MAD.
 - Step 4: You don't want to waste 30 minutes on MAD/MySQL changing the `pokemon` and `pokemon_display` tables because you have 17851758 / 6 months of mons history there! Clear those up: `TRUNCATE` or `DELETE FROM` if you don't do it already automagically.
 - Step 5: Remove `update_log.json` file from MAD `master/legacy` main directory.
 - Step 6: Run `git checkout async` from MAD `master/legacy` main directory.
 - Step 7: Run `git status` from MAD `master/legacy` main directory, it should show:
 ```
On branch async
Your branch is up to date with 'origin/async'.
```
 - Step 8: Adjust `config.ini` (config.ini changes above)
 - Step 9: Install new requirmements in python3.9 venv TODO_LINK_HERE_TO_MANUAL_INSTALL_MAD_DOCS_VENV
 - Step 9: Start `start.py` via python3.9 venv manually (not crontab, systemd, supervisor or any type of script) - just for first time to see if there are any errors/problems and to make sure you will see everything.

