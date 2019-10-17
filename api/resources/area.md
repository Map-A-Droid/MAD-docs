The following modes are available in the API:
 - [idle](#idle)
 - [iv_mitm](#iv_mitm)
 - [mon_mitm](#mon_mitm)
 - [pokestops](#pokestops)
 - [raids_mitm](#raids_mitm)

# idle
## Fields
| Field Name | Type  | Required  | Description   |
| --         | --    | --        | --            |
|geofence_included|String|True|Including geofence for scanarea|
|name|String|True|Name of area|
|routecalc|String|True|Name of routefile|

# iv_mitm
## Fields
| Field Name | Type  | Required  | Description   |
| --         | --    | --        | --            |
|geofence_excluded|String|False|Excluding geofence for scanarea|
|geofence_included|String|True|Including geofence for scanarea|
|name|String|True|Name of area|
|routecalc|String|True|Name of routefile. MAD will automatically append '.calc' to this name.|

## Settings
| Field Name | Type  | Required  | Description   |
| --         | --    | --        | --            |
|delay_after_prio_event|Integer|False|Offset to be added to events such as spawns or raid starts. E.g. if you want to scan gyms at least a minute after an egg has hatched, set it to 60 (Default: empty)<br>Empty = Disable PrioQ|
|max_distance|Decimal|False|Max. distance of walking - otherwise teleport to new location|
|min_time_left_seconds|Integer|False|Ignore mons with less spawntime in seconds|
|mon_ids_iv|String|False|IV List Resource|
|priority_queue_clustering_timedelta|Decimal|False|Cluster events within the given timedelta in seconds. The latest event in time within a timedelta will be used to scan the clustered events (Default: 300)|
|remove_from_queue_backlog|Boolean|False|Remove any events from priority queue that have been due for scanning before NOW - given time in seconds (Default: 0)|
|speed|Decimal|False|Speed of player in kmh|
|starve_route|Boolean|False|Disable round-robin of route vs. priority queue events. If True,    your route may not be completed in time and e.g. only spawns will be scanned|

# mon_mitm
## Fields
| Field Name | Type  | Required  | Description   |
| --         | --    | --        | --            |
|coords_spawns_known|Boolean|True|Scan all spawnpoints or just ones with unknown endtimes|
|geofence_excluded|String|False|Excluding geofence for scanarea|
|geofence_included|String|True|Including geofence for scanarea|
|init|Boolean|True|Set this open True, if you scan the area for gyms / spawnpoints the first time|
|name|String|True|Name of area|
|routecalc|String|True|Name of routefile|

## Settings
| Field Name | Type  | Required  | Description   |
| --         | --    | --        | --            |
|delay_after_prio_event|Integer|False|Offset to be added to events such as spawns or raid starts. E.g. if you want to scan gyms at least a minute after an egg has hatched, set it to 60 (Default: empty)<br>Empty = Disable PrioQ|
|init_mode_rounds|Integer|False|Rounds in Init Mode. (Default: 1)|
|max_distance|Decimal|False|Max. distance of walking - otherwise teleport to new location|
|min_time_left_seconds|Integer|False|Ignore mons with less spawntime in seconds|
|mon_ids_iv|String|False|IV List Resource|
|priority_queue_clustering_timedelta|Decimal|False|Cluster events within the given timedelta in seconds. The latest event in time within a timedelta will be used to scan the clustered events (Default: 0)|
|remove_from_queue_backlog|Decimal|False|Remove any events in priority queue that have been due for scanning before NOW - given time in seconds (Default: 0)|
|speed|Decimal|False|Speed of player in kmh|
|starve_route|Boolean|False|Disable round-robin of route vs. priority queue events. If True,    your route may not be completed in time and e.g. only spawns will be scanned|

# pokestops
## Fields
| Field Name | Type  | Required  | Description   |
| --         | --    | --        | --            |
|geofence_excluded|String|False|Excluding geofence for scanarea|
|geofence_included|String|True|Including geofence for scanarea|
|init|Boolean|True|Set this open True, if you scan the area for gyms / spawnpoints the first time|
|level|Boolean|True|Level up an account mode|
|name|String|True|Name of area|
|route_calc_algorithm|String|False|Method of calculation for routes. (Default optimized)|
|routecalc|String|True|Name of routefile|

## Settings
| Field Name | Type  | Required  | Description   |
| --         | --    | --        | --            |
|cleanup_every_spin|Boolean|False|Cleanup quest inventory every spinned stop|
|ignore_spinned_stops|Boolean|False|Do not spinn stops already made in the past (for levelmode)|
|max_distance|Decimal|False|Max. distance of walking - otherwise teleport to new location|
|speed|Decimal|False|Speed of player in kmh|

# raids_mitm
## Fields
| Field Name | Type  | Required  | Description   |
| --         | --    | --        | --            |
|geofence_excluded|String|False|Excluding geofence for scanarea|
|geofence_included|String|True|Including geofence for scanarea|
|including_stops|Boolean|True|Calculate route including stops to catch invasions.|
|init|Boolean|True|Set this open True, if you scan the area for gyms / spawnpoints the first time|
|name|String|True|Name of area|
|routecalc|String|True|Name of routefile|

## Settings
| Field Name | Type  | Required  | Description   |
| --         | --    | --        | --            |
|delay_after_prio_event|Integer|False|Offset to be added to events such as spawns or raid starts. E.g. if you want to scan gyms at least a minute after an egg has hatched, set it to 60 (Default: empty)<br>Empty = Disable PrioQ|
|init_mode_rounds|Integer|False|Rounds in Init Mode. (Default: 1)|
|max_distance|Decimal|False|Max. distance of walking - otherwise teleport to new location|
|mon_ids_iv|String|False|IV List Resource|
|priority_queue_clustering_timedelta|Decimal|False|Cluster events within the given timedelta in seconds. The latest event in time within a timedelta will be used to scan the clustered events (Default: 0)|
|remove_from_queue_backlog|Decimal|False|Remove any events in priority queue that have been due for scanning before NOW - given time in seconds (Default: 0)|
|speed|Decimal|False|Speed of player in kmh|
|starve_route|Boolean|False|Disable round-robin of route vs. priority queue events. If True,    your route may not be completed in time and e.g. only spawns will be scanned|
