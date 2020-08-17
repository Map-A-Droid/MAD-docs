# APKs
MAD can store APKs in the database and allow an end-user / client to download them when requested.  This information is available via MADmin and PogoDroid.  Both sections require the following headers to be present:
 - Origin
 - Authentication (if configured on the MAD server)

The following APK Types are available:
 - pogo, com.nianticlabs.pokemongo, 0
 - rgc, de.grennith.rgc.remotegpscontroller, 1
 - pogodroid, com.mad.pogodroid, 2

The following Architectures are available:
 - noarch, 0
 - armeabi-v7a, 1
 - arm64-v8a, 2

## APK Definition
When requesting info for an APK the following data will be returned:
 - arch_disp: Friendly-Name for the architecture of the APK
 - file_id: File ID database reference
 - filename: Filename that will be saved (unless changed).  Default format is `<apk_type_friendly_name>_<apk_architecture>_<version>.apk`
 - mimetype: MIME-Type of the file (should always be 'application/vnd.android.package-archive')
 - size: Size in bytes of the file
 - usage_disp: Friendly-Name of the apk type
 - version: Version of the APK

## Endpoints
### GET
#### All APK Information
Returns all information available for any downloaded APK.
* MADmin: `/api/mad_apk`
* PD: Not Available
* Return Information: {apk_type:{architecture:{APK Definition}}, architecture:{APK Definition}, ..}

#### APK Type Information
Returns all information available for the given APK.  This will include all information for all architectures
* MADmin: `/api/mad_apk/<apk_type>`
* PD: `/mad_apk/<apk_type>`
* Return Information: {architecture:{}}, architecture:{}, ..}

#### APK / Architecture Information
Returns all information for the given APK / Architecture.  If architecture is not specified it will attempt to return the data for noarch.
* MADmin: `/api/mad_apk/<apk_type>/<apk_arch>`
* PD: `mad_apk/<apk_type>/<apk_arch>`
* Return Information:  {APK Definition}

#### APK Download
Download the currently downloaded version stored in the database.  If architecture is not specified it will attempt to use noarch.
* MADmin: `/api/mad_apk/<apk_type>/<apk_arch>/download`
* PD: `mad_apk/<apk_type>/<apk_arch>/download`
* Return Information:  Downloads the APK

### POST
#### Upload an APK
Upload a new APK into the MAD database.  Both fields must be specified
* MADmin: `/api/mad_apk/<apk_type>/<apk_arch>`
* PD: Not Available

### Delete
#### Remove an APK
Delete an APK from the MAD databasee.  Both fields must be specified
* MADmin: `/api/mad_apk/<apk_type>/<apk_arch>`
* PD: Not Available
