============
Introduction
============

URI
===

The API will be available at :code:`/api` (no trailing slash).

Implemented data types
======================

The following data-types have been implemented and can be used for Content-Type or Accept headers

- application/json


Using the API
=============

For all resource roots, GET functionality has been implemented. Please refer to the section Global GET Parameters to view available options.
For all sub-components, the following operations have been implemented.


* :code:`DELETE`: Attempt to delete the resource. It will fail if it is a dependency for another object.
* :code:`GET`: retrieve data.
* :code:`PATCH`: update the resource but only modify the fields that have been sent.

  * If you wish to append values to a list, use the header :code:`X-Append: 1`. If this is not present, it will replace the list.
* :code:`POST`: create a new resource. Response content will contain the newly-created object.
* :code:`PUT`: replace the existing object with the new one being sent.


If an error occurs, refer to the returned headers to find the issue.

Global Headers
--------------

The following global headers can be used when calling the API

* Content-Type (str): incoming data format. Default is application/json
* Accept (str): outgoing data format. Default is application/json
* X-Beautify (integer): Display the returned data in a human-readable format

 * 1: Format the response body.
 * All other options: no formatting

Global GET Parameters
---------------------

The following parameters are available for all root resources

* fetch_all (int): Fetch all data related to the object versus the display field

 * 1: Fetch all data
 * All other options: only return the uri / display field

* display_field (str): Default sort field. If fetch_all is not 1, this field will be returned as the value for the key pair
* hide_resource (int): Hide any filter information related to the resource and only return the results

 * 1: Hide any filtering information
 * All other options: return all information


Searching via the API is done through the GET parameters. If no search logic is specified it will default to equals. To
perform a search for a field include <field_name>.<operation>=search. The following operations are implemented:

 * eq: The field must be equal to the value. This is the default search if none is specified.
    To query all devices that use the device pool /api/walker/5      
    :code:`/api/device?walker.eq=/api/walker/5`

    To query all devices that use the MAC address 06:81:91:10:2d:c8
    :code:`/api/device?origin.mac_address.eq=06:81:91:10:2d:c8`

 * like: Performs a similar search.
    To query all origins that begin with tx9s
    :code:`/api/device?origin.like=tx9s`

Response Headers
----------------

The following headers can be returned for all resources:

* Location (str): Returned during a successful POST operation. States the URI of the newly created resource
* X-Status (str): Human-readable result of the command
* X-Uri (str): Returned during a successful POST operation. States the URI of the newly created resource

Status Codes
------------

* 200: Successfully found and returned the data
* 201: Successfully created a new resource
* 204: The resource has been successfully updated or replaced
* 400: A required header was missing. Refer to the body of the response to determine the issue
* 404: The resource ID was not found
* 412: A dependency failed validation. Refer to the body for a list of failed dependencies (list of objects containing uri / display_name).
* 422: An error occured while creating the resource. Refer to the body for the errors


`MAD APKs <apks>`_
------------------
MAD APKs allows an administrator to store APKs in the MAD Database to be used for the API or SmartJobs. Available endpoints are available on the MAD APK Page

`Origin Hopper <origin_hopper>`_
--------------------------------
Origin Hopper allows for rapid deployment of new devices into a MAD environment. It will generate an origin and create the device within MAD. This functionality is only available through the PogoDroid / MITM Receiver port.

`Area <resources/area>`_
------------------------

URI: :code:`/api/area`

The following is unique about areas:

* A valid mode must be specified. If a mode is not specified or is not valid, 412 will be returned
* Dependencies:

 * walkerarea

`Authentication <resources/auth>`_
----------------------------------

URI: :code:`/api/auth`

There is no special handling for authentication

`Devices <resources/device>`_
-----------------------------

URI: :code:`/api/device`

There is no special handling for devices

`DevicePools <resources/devicesetting>`_
----------------------------------------

URI: :code:`/api/devicesetting`

The following is unique about device pools:

* Dependencies:

 * device

`MonLists <resources/monivlist>`_
---------------------------------

URI: :code:`/api/monivlist`

The following is unique about Mon Lists:

* Dependencies:

 * areas

`Walkers <resources/walker>`_
-----------------------------

URI: :code:`/api/walker`

The following is unique about Mon Lists:

* Removing a walker will check and remove any walkerareas assigned to the walker that are no longer in use
* Dependencies:

 * device

`WalkerArea <resources/walkerarea>`_
------------------------------------

URI: :code:`/api/walkerarea`

The following is unique about Mon Lists:

* Dependencies:

 * walker
