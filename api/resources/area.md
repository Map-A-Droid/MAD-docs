# Areas

## API Definition

The following modes are available in the API:

 - [idle](#idle)
 - [iv_mitm](#iv_mitm)
 - [mon_mitm](#mon_mitm)
 - [pokestops](#pokestops)
 - [raids_mitm](#raids_mitm)

### idle

Field Name | Type | Required | Default | Description
-- | -- | -- | -- | --
geofence_included|URI-/api/geofence|True|None|Including geofence for scanarea
name|String|True|None|Name of area
routecalc|URI-/api/routecalc|False|Auto-Generated|Routecalc to be used by MAD.  Leave blank unless you are reusing an existing routecalc

### iv_mitm

Field Name | Type | Required | Default | Description
-- | -- | -- | -- | --
geofence_excluded|URI-/api/geofence|False|None|Excluding geofence for scanarea
geofence_included|URI-/api/geofence|True|None|Including geofence for scanarea
name|String|True|None|Name of area
routecalc|URI-/api/routecalc|False|Auto-Generated|Routecalc to be used by MAD.  Leave blank unless you are reusing an existing routecalc

#### Settings

Field Name | Type | Required | Default | Description
-- | -- | -- | -- | --
delay_after_prio_event|Integer|False|Empty|Offset to be added to events such as spawns or raid starts. E.g. if you want to scan gyms at least a minute after an egg has hatched, set it to 60.  Empty = Disable PrioQ
max_distance|Decimal|False|0|Max. distance of walking - otherwise teleport to new location
min_time_left_seconds|Integer|False|None|Ignore mons with less spawn time in seconds
mon_ids_iv|URI-/api/monivlist|False|None|IV List Resource
priority_queue_clustering_timedelta|Decimal|False|300|Cluster events within the given timedelta in seconds. The latest event in time within a timedelta will be used to scan the clustered events
remove_from_queue_backlog|Boolean|False|0|Remove any events from priority queue that have been due for scanning before NOW - given time in seconds
speed|Decimal|False|0|Speed of player in kmh
starve_route|Boolean|False|False|Disable round-robin of route vs. priority queue events. If True, your route may not be completed in time and e.g. only spawns will be scanned

### mon_mitm

Field Name | Type | Required | Default | Description
-- | -- | -- | -- | --
coords_spawns_known|Boolean|False|False|Scan all spawnpoints or just ones with unknown endtimes
geofence_excluded|URI-/api/geofence|False|None|Excluding geofence for scanarea
geofence_included|URI-/api/geofence|True|None|Including geofence for scanarea
init|Boolean|False|False|Set this open True, if you scan the area for gyms / spawnpoints the first time
name|String|True|Name of area
routecalc|URI-/api/routecalc|False|Auto-Generated|Routecalc to be used by MAD.  Leave blank unless you are reusing an existing routecalc

#### Settings

Field Name | Type | Required | Default | Description
-- | -- | -- | -- | --
delay_after_prio_event|Integer|False|Offset to be added to events such as spawns or raid starts. E.g. if you want to scan gyms at least a minute after an egg has hatched, set it to 60.  Empty = Disable PrioQ (Default: empty)
init_mode_rounds|Integer|False|Rounds in Init Mode. (Default: 1)
max_distance|Decimal|False|Max. distance of walking - If the distance between points is greater than this value the worker will teleport (Default: 0)
min_time_left_seconds|Integer|False|Ignore mons with less spawntime in seconds
mon_ids_iv|URI-/api/monivlist|False|IV List Resource
priority_queue_clustering_timedelta|Decimal|False|Cluster events within the given timedelta in seconds. The latest event in time within a timedelta will be used to scan the clustered events (Default: 300)
remove_from_queue_backlog|Decimal|False|Remove any events in priority queue that have been due for scanning before NOW - given time in seconds (Default: 0)
speed|Decimal|False|0|Speed of player in kmh
starve_route|Boolean|False|False|Disable round-robin of route vs. priority queue events. If True, your route may not be completed in time and e.g. only spawns will be scanned

### pokestops

Field Name | Type | Required | Default | Description
-- | -- | -- | -- | --
geofence_excluded|URI-/api/geofence|False|None|Excluding geofence for scanarea
geofence_included|URI-/api/geofence|True|None|Including geofence for scanarea
init|Boolean|False|False|Set this open True, if you scan the area for gyms / spawnpoints the first time
level|Boolean|False|False|Level up an account mode
name|String|True|None|Name of area
route_calc_algorithm|String|False|optimized|Method of calculation for routes. Allowed values (optimized, quick)
routecalc|URI-/api/routecalc|False|Auto-Generated|Routecalc to be used by MAD.  Leave blank unless you are reusing an existing routecalc

#### Settings

Field Name | Type | Required | Default | Description
-- | -- | -- | -- | --
cleanup_every_spin|Boolean|False|False|Cleanup quest inventory every after every stop
ignore_spinned_stops|Boolean|False|True|Do not spin stops already made in the past (for levelmode)
max_distance|Decimal|False|0|Max. distance of walking - otherwise teleport to new location
speed|Decimal|False|0|Speed of player in kmh

### raids_mitm

Field Name | Type | Required | Default | Description
-- | -- | -- | -- | --
geofence_excluded|URI-/api/geofence|False|None|Excluding geofence for scanarea
geofence_included|URI-/api/geofence|True|None|Including geofence for scanarea
including_stops|Boolean|True|Calculate route including stops to catch invasions.
init|Boolean|False|False|Set this open True, if you scan the area for gyms / spawnpoints the first time
name|String|True|Name of area
routecalc|URI-/api/routecalc|False|Auto-Generated|Routecalc to be used by MAD.  Leave blank unless you are reusing an existing routecalc

#### Settings

Field Name | Type | Required | Default | Description
-- | -- | -- | -- | --
delay_after_prio_event|Integer|False|Empty|Offset to be added to events such as spawns or raid starts. E.g. if you want to scan gyms at least a minute after an egg has hatched, set it to 60.  Empty = Disable PrioQ
init_mode_rounds|Integer|False|1|Rounds in Init Mode
max_distance|Decimal|False|0|Max. distance of walking - otherwise teleport to new location
mon_ids_iv|URI-/api/monivlist|False|None|IV List Resource
priority_queue_clustering_timedelta|Decimal|False|600|Cluster events within the given timedelta in seconds. The latest event in time within a timedelta will be used to scan the clustered events
remove_from_queue_backlog|Decimal|False|0|Remove any events in priority queue that have been due for scanning before NOW - given time in seconds
speed|Decimal|False|0|Speed of player in kmh
starve_route|Boolean|False|False|Disable round-robin of route vs. priority queue events. If True, your route may not be completed in time and e.g. only spawns will be scanned

## JSON RPC
The following RPC implementations are available

### Route Recalculation
This will recalculate the route with the given area options.  Once it has successfully recalculated the route all devices will be disconnected and reconnected
- call: recalculate
- args
  - No required args