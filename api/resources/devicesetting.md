# Devicesetting

The following definition is available for Device Pool resources
## Fields
| Field Name | Type  | Required  | Description   |
| --         | --    | --        | --            |
|devicepool|String|True|Name for the global device settings|

## Settings
| Field Name | Type  | Required  | Description   |
| --         | --    | --        | --            |
|cool_down_sleep|Boolean|False|More cooldown after teleport|
|delay_after_hatch|Decimal|False|Delay in minutes to wait before moving to the location of a hatched egg. Raidbosses do not necessarily appear immediately. (Default: 3.5)|
|mitm_wait_timeout|Decimal|False|Timeout for waiting for data after setting/reaching a location. (Default: 45)|
|post_pogo_start_delay|Decimal|False|Delay in seconds to wait after starting pogo. (Default: 60.0)|
|post_screenshot_delay|Decimal|False|The delay in seconds to wait after taking a screenshot to copy it and start the next (Default: 1)|
|post_teleport_delay|Decimal|False|Delay in seconds after a teleport. (Default: 4.0)|
|post_turn_screen_on_delay|Decimal|False|Delay in seconds after a screenshot has been taken and about to be saved. (Default: 0.2)|
|post_walk_delay|Decimal|False|Delay in seconds after reaching destination with the speed given. (Default: 2.0)|
|reboot|Boolean|False|Reboot device if reboot_thresh is reached (Default: false)|
|reboot_thresh|Integer|False|Restart Phone after restart Pogo N times. (Default: 3)|
|restart_pogo|Integer|False|Restart Pogo every N location-changes. (Default: 80. - 0 for never)|
|restart_thresh|Integer|False|Restart Pogo after reaching MITM Timeout N times. (Default: 5)|
|route_calc_algorithm|String|False|Method of calculation for routes. (Default optimized)|
|screenshot_quality|Integer|False|Quality of screenshot (Default: 80)|
|screenshot_type|String|True|Type of screenshot (Default: jpeg)|
|screenshot_x_offset|Integer|False|Adjust the x-axis click offset on phones with softbars and/or black upper bars. (+ right - left / Default: 0)|
|screenshot_y_offset|Integer|False|Adjust the y-axis click offset on phones with softbars and/or black upper bars. (+ down - up / Default: 0)|
|startcoords_of_walker|String|False|Start Coords of Walker (Default: None) (Format: 123.45,67.89)|
|vps_delay|Decimal|False|Set click delay for pokestop walker (VPS -> local phone) (Default: 0)|
|walk_after_teleport_distance|Decimal|False|Walk n seconds after teleport for getting data|