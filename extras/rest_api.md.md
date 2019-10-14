# API
A restful API has been created for interacting with MADmin settings.  This will standardize how MADmin and users will interact with the data to allow for a more consistent workflow between the two.

# URI
The API will be available at /api (no trailing slash).

# Implemented data types
The following data-types have been implemented and can be used for Content-Type or Accept headers
  - application/json

# Using the API
For all resource roots, GET functionality has been implemented.  Please refer to the section Global GET Parameters to view available options.
For all sub-components, GET, PATCH, POST, and PUT have been implemented.
  - GET: retrieve data
  - PATCH: update the resource but only modify the fields that have been sent
   - If you wish to append values to a list, use the header 'X-Append: 1'.  If this is not present, it will replace the list.
  - POST: create a new resource
  - PUT: replace the existing object with the new one being sent

If an error occurs, refer to the returned headers to find the issue.

## Global Headers
The following global headers can be used when calling the API
  - Content-type (str): incoming data format.  Default is application/json
  - Accept (str): outgoing data format.  Default is application/json
  - X-Beautify (integer): Display the returned data in a human-readable format
   - 1: Format the response body
   - All other options: no formatting

## Global GET Parameters
The following parameters are available for all root resources
  - fetch_all (int): Fetch all data related to the object versus the display field
    - 1:  Fetch all data
    - All other options: only return the uri / display field
  - display_field (str): Default sort field.  If fetch_all is not 1, this field will be returned as the value for the key pair
  - hide_resource (int): Hide any filter information related to the resource and only return the results
    - 1:  Hide any filtering information
    - All other options: return all information

## Response Headers
The following headers can be returned for all resources:
  - Location (str): Returned during a successful POST operation.  States the URI of the newly created resource
  - X-Status (str): Human-readable result of the command
  - X-Uri (str): Returned during a successful POST operation.  States the URI of the newly created resource


## Status Codes
  - 200: Successfully found and returned the data
  - 201: Successfully created a new resource
  - 204: The resource has been successfully updated or replaced
  - 400: A required header was missing.  Refer to the body of the response to determine the issue
  - 404: The resource ID was not found
  - 412: A dependency failed validation.  Refer to the body for a list of failed dependencies (list of objects containing uri / display_name).
  - 422: An error occured while creating the resource.  Refer to the body for the errors

## Resources
The following resources have been implemented to the API:
  - Areas (/api/area)
  - Authentication (/api/auth)
  - Devices (/api/device)
  - Device Pools (/api/devicesetting)
  - Mon Lists (/api/monivlist)
  - Walkers (/api/walker)
  - Walker Area (/api/walkerarea)

### Area
The following is unique about areas:
  - A valid mode must be specified.  If a mode is not specified or is not valid, 412 will be returned
  - Dependencies
    - walkerarea

### Authentication
There is no special handling for authentication

### Devices
There is no special handling for devices

### Device Pools
The following is unique about device pools:
  - Dependencies
    - device

### Mon Lists
The following is unique about Mon Lists:
  - Dependencies
    - areas

### Walkers
The following is unique about Mon Lists:
  - Removing a walker will check and remove any walkerareas assigned to the walker that are no longer in use
  - Dependencies
    - device

### Walker Area
The following is unique about Mon Lists:
  - Dependencies
    - walker

## Examples
### Getting all auth
#### Using default sort field
```
curl -H 'X-Beautify: 1' http://localhost:5000/api/auth
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET /api/auth HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.58.0
> Accept: */*
> X-Beautify: 1
>
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 458
< Access-Control-Allow-Origin: *
< Access-Control-Allow-Headers: Content-Type,Authorization
< Access-Control-Allow-Methods: GET,PUT,POST,DELETE,OPTIONS
< Server: Werkzeug/0.15.6 Python/3.6.8
< Date: Mon, 14 Oct 2019 18:12:32 GMT
<
{
    "resource": {
        "fields": [
            {
                "name": "username",
                "descr": "Username of device",
                "required": true
            },
            {
                "name": "password",
                "descr": "Password of device",
                "required": true
            }
        ],
        "settings": []
    },
    "results": {
        "/api/auth/1": "cec",
        "/api/auth/0": "grennith"
    }
}
* Closing connection 0
```

#### Using custom sort field
```
curl -v -H 'X-Beautify: 1' http://localhost:5000/api/auth?display_field=password
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET /api/auth?display_field=password HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.58.0
> Accept: */*
> X-Beautify: 1
>
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 459
< Access-Control-Allow-Origin: *
< Access-Control-Allow-Headers: Content-Type,Authorization
< Access-Control-Allow-Methods: GET,PUT,POST,DELETE,OPTIONS
< Server: Werkzeug/0.15.6 Python/3.6.8
< Date: Mon, 14 Oct 2019 18:13:58 GMT
<
{
    "resource": {
        "fields": [
            {
                "name": "username",
                "descr": "Username of device",
                "required": true
            },
            {
                "name": "password",
                "descr": "Password of device",
                "required": true
            }
        ],
        "settings": []
    },
    "results": {
        "/api/auth/0": "12345",
        "/api/auth/1": "test123"
    }
* Closing connection 0
}
```

#### Pulling all information resource information and hiding the resource fields
```
curl -v -H 'X-Beautify: 1' 'http://localhost:5000/api/walker?hide_resource=1&fetch_all=1'
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET /api/walker?hide_resource=1&fetch_all=1 HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.58.0
> Accept: */*
> X-Beautify: 1
>
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 691
< Access-Control-Allow-Origin: *
< Access-Control-Allow-Headers: Content-Type,Authorization
< Access-Control-Allow-Methods: GET,PUT,POST,DELETE,OPTIONS
< Server: Werkzeug/0.15.6 Python/3.6.8
< Date: Mon, 14 Oct 2019 18:21:08 GMT
<
{
    "/api/walker/2": {
        "setup": [
            "/api/walkerarea/8",
            "/api/walkerarea/9",
            "/api/walkerarea/10",
            "/api/walkerarea/10"
        ],
        "walkername": "iv_checker"
    },
    "/api/walker/0": {
        "setup": [
            "/api/walkerarea/0",
            "/api/walkerarea/1",
            "/api/walkerarea/2"
        ],
        "walkername": "quest_example"
    },
    "/api/walker/1": {
        "setup": [
            "/api/walkerarea/3",
            "/api/walkerarea/4",
            "/api/walkerarea/5",
            "/api/walkerarea/6",
            "/api/walkerarea/7"
        ],
        "walkername": "raid_mon_example"
    }
}
* Closing connection 0
```

### Creating a walker
```
curl -v -H 'X-Beautify: 1' -H 'X-Append: 1' -X POST -H 'Content-Type: application/json' -d '{"setup":["/api/walkerarea/10"], "walkername": "test"}' http://localhost:5000/api/walker
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying ::1...
* TCP_NODELAY set
* connect to ::1 port 5000 failed: Connection refused
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> POST /api/walker HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.58.0
> Accept: */*
> X-Beautify: 1
> X-Append: 1
> Content-Type: application/json
> Content-Length: 54
>
* upload completely sent off: 54 out of 54 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 16
< Location: http://localhost:5000/api/walker/10
< X-Uri: /api/walker/10
< X-Status: Successfully created the object
< Access-Control-Allow-Origin: *
< Access-Control-Allow-Headers: Content-Type,Authorization
< Access-Control-Allow-Methods: GET,PUT,POST,DELETE,OPTIONS
< Server: Werkzeug/0.15.6 Python/3.6.8
< Date: Mon, 14 Oct 2019 18:40:39 GMT
<
"/api/walker/10"
* Closing connection 0
```

### Adding a walkerarea to a walker
```
curl -v -H 'X-Beautify: 1' -H 'X-Append: 1' -X PATCH -H 'Content-Type: application/json' -d '{"setup":["/api/walkerarea/10"]}' http://localhost:5000/api/walker/2
* Connected to localhost (127.0.0.1) port 5000 (#0)
> PATCH /api/walker/2 HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.58.0
> Accept: */*
> X-Beautify: 1
> X-Append: 1
> Content-Type: application/json
> Content-Length: 32
>
* upload completely sent off: 32 out of 32 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 204 NO CONTENT
< Content-Type: application/json
< X-Status: Successfully updated the object
< Access-Control-Allow-Origin: *
< Access-Control-Allow-Headers: Content-Type,Authorization
< Access-Control-Allow-Methods: GET,PUT,POST,DELETE,OPTIONS
< Server: Werkzeug/0.15.6 Python/3.6.8
< Date: Mon, 14 Oct 2019 18:09:01 GMT
<
* Closing connection 0
```
