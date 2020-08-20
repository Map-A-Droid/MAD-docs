=================
MAD job processor
=================

MAD has an internal cronjob-like job processing mechanism. With this mechanism, you can run jobs manually or schedule them.

Features:

* Install or update apps on your devices
* Run any command on your devices

Create new job
==============

Create a `personal_commands` folder in MAD's root directory. Save custom jobs as .json file. MAD must be restarted for new jobs to appear.

Example Job to read the game's version:

.. code-block:: json

  {
    "Readout Pogo Version":
    [
      {
        "TYPE": "jobType.PASSTHROUGH",
        "SYNTAX": "dumpsys package com.nianticlabs.pokemongo | grep versionName",
        "FIELDNAME": "POGO_Version",
        "WAITTIME": 5
      }
    ]
  }

* :code:`Readout Pogo Version`: Name of job that will appear in MADmin
* :code:`TYPE: jobType.PASSTHROUGH`: Type of job. See :ref:`Job types` for a list of supported jobs
* :code:`SYNTAX: dumpsys package com.nianticlabs.pokemongo | grep versionName`: Shell command
* :code:`FIELDNAME: POGO_Version`: Field name for returning Value
* :code:`WAITTIME: 5`: Wait 5 minutes before starting the job

You can chain multiple jobs together. See :ref:`Nested jobs`.

APK installation job
====================

MAD can create a job to install an APK on your devices just by uploading the app via MADmin.

Use :code:`upload_path` in config.ini to define the software folder for these APKs (Default: :code:`upload/` in MAD root folder)

:menuselection:`MADmin --> Jobs --> Upload File`

.. image:: /_static/jobs/MADmin_File_Upload.png

Select APK and Upload it.

Job types
=========

MAD supports the following job types:

* :code:`jobType.INSTALLATION`: Install APK on device
* :code:`jobType.REBOOT`: Reboot device
* :code:`jobType.RESTART`: Restart Pogo
* :code:`jobType.STOP`: Stop Pogo
* :code:`jobType.START`: Start Pogo
* :code:`jobType.PASSTHROUGH`: Send command to device

Automatic Jobs
==============

You can configure MAD to launch jobs based on certain timings.

Create file "autocommands.json" in your configured :code:`file_path/` directory. You can set the path via config.ini.

Example content:

.. code-block:: json

  [
    {
      "redo": true,
      "algotype": "loop",
      "algovalue": 10,
      "startwithinit": true,
      "origins": "tv1",
      "job": "Readout Pogo Version",
      "redoonerror": true
    },
    {
      "redo": true,
      "algotype": "daily",
      "algovalue": "21:00",
      "startwithinit": true,
      "origins": "tv5|tv6|tv7",
      "job": "Readout RGC Version",
      "redoonerror": false
    }
  ]

Description:

* :code:`redo`: :code:`true` will reschedule jobs after finish. :code:`false` will set this jobs to run only once
* :code:`algotype`: :code:`daily` runs this job once a day. :code:`loop` will looü the job every x minutes
* :code:`algovalue`: depends on algotype. :code: `daily` sets time like "21:30" (24h format). :code:`loop` sets loop time in minutes (120 = every 2 hours)
* :code:`startwithinit`: :code:`true` will start the job after MAD start. :code:`false` starts the job according to schedule
* :code:`origins`: Single or list of devices (separated by :code:`|`)
* :code:`job`: Name of the job
* :code:`redoonerror`: Reschedule jobs after getting an error

MADmin API endpoint for jobs
============================

Madmin provides a read-only endpoint via :code:`GET /jobstatus` to read all processed jobs' return value.

Example:

.. code-block:: json

  {
     "my_device_name": {
        "POGODROID_Version": "[versionName=1.1.3.0]",
        "POGO_Version": "[versionName=0.153.2]",
        "RGC_Version": "[versionName=1.9.3, versionName=1.8.34]"
     }
  }

Nested jobs
===========

You are able to combine more jobs to one nested or chained job. Nested jobs are processed from top to bottom.

Example:

MAD starts the top most job and will schedule the memory usage readout with a delay of 3 minutes. Eventually, the game will start.

.. code-block:: json

  {
    "Stop/Start Pogo and readout Memory Usage":
    [
      {
        "TYPE": "jobType.STOP",
        "SYNTAX": "STOP Pogo"
      },
      {
        "TYPE": "jobType.PASSTHROUGH",
        "SYNTAX": "dumpsys meminfo | egrep -w 'Total RAM|Free RAM|Used RAM'",
        "FIELDNAME": "MEMORY_USAGE",
        "WAITTIME": 3
      },
      {
        "TYPE": "jobType.START",
        "SYNTAX": "START Pogo"
      }
    ]
  }


.. hint::
  If one of the jobs results in an error, following jobs will be canceled.

.. image:: /_static/jobs/MADmin_nested_jobs_monitor.png
  :width: 100%

Discord integration
===================

MAD is able to submit a job's state to Discord.

.. code-block:: none

  job_dt_wh                    # Send job status to discord (Default: False)
  job_dt_wh_url:               # Discord Webhook URL for job messages
  job_dt_send_type:            # Kind of Job Messages to send - separated by pipe | (Default: SUCCESS|FAILURE|NOCONNECT|TERMINATED)

* :code:`job_dt_wh`: Enable Discord support
* :code:`job_dt_wh_url`: Discord webhook URL
* :code:`job_dt_send_type`: Define the kind of submission (separated by :code:`|`) (Default: SUCCESS|FAILURE|NOCONNECT|TERMINATED)

Examples:

.. image:: /_static/jobs/Jobs_DT_job1.png
.. image:: /_static/jobs/Jobs_DT_job2.png
.. image:: /_static/jobs/Jobs_DT_job3.png
