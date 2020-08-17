## Origin Hopper
The Origin Hopper / Generator was designed to allow for rapid deployment of devices.  It utilizes the PogoDroid port as it is already configured for the MAD rom.

### Headers
The following headers can be used when making requests to the origin hopper:
 - Authorization (required):  Authorization configured on the Auths page.  If there are no configured auths this is not a required field.
 - OriginBase (required): Prefix for the origin.  If you wanted OriginDefault<1-n> you would use OriginDefault.
 - walker (optional): Walker ID to assign to the device
 - pool (optional): Pool ID to assign to the device

### Endpoint
There is only one endpoint for the origin hopper / generator, `/origin_generator`.  Due to this being generator a GET action performed with the correct headers will create the origin.  The body will return the new origin to used with MAD.  Once created you will see the device in MADmin and can make any required configuration changes.  If the device fails to create a 400 or 404 will be returned with the reason.