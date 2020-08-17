Examples
--------

Getting all auth
^^^^^^^^^^^^^^^^

Using default sort field

.. code-block:: bash

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


Using custom sort field

.. code-block:: bash

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


Pulling all information resource information and hiding the resource fields

.. code-block:: bash

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


Creating a walker
^^^^^^^^^^^^^^^^^

.. code-block:: bash

  curl -v -H 'X-Beautify: 1' -H 'X-Append: 1' -X POST -H 'Content-Type: application/json' -d '{"setup":["/api/walkerarea/10"], "walkername": "test"}' http://localhost:5000/api/walker
  > POST /api/walker HTTP/1.1
  > Host: localhost:5000
  > User-Agent: curl/7.65.3
  > Accept: */*
  > X-Beautify: 1
  > X-Append: 1
  > Content-Type: application/json
  > Content-Length: 54
  >
  * upload completely sent off: 54 out of 54 bytes
  * Mark bundle as not supporting multiuse
  * HTTP 1.0, assume close after body
  < HTTP/1.0 201 CREATED
  < Content-Type: application/json
  < Content-Length: 63
  < Location: http://localhost:5000/api/walker/6
  < X-Uri: /api/walker/6
  < X-Status: Successfully created the object
  < Access-Control-Allow-Origin: *
  < Access-Control-Allow-Headers: Content-Type,Authorization
  < Access-Control-Allow-Methods: GET,PUT,POST,DELETE,OPTIONS
  < Server: Werkzeug/0.16.0 Python/3.7.5rc1
  < Date: Thu, 31 Oct 2019 00:13:51 GMT
  <
  {
      "walkername": "test",
      "setup": [
          "10"
      ]
  }
  * Closing connection 0


Adding a walkerarea to a walker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

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
