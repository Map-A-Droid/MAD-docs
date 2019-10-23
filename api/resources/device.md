# Device

The following definition is available for Device resources
## Fields
| Field Name | Type  | Required  | Description   |
| --         | --    | --        | --            |
|adbname|String|False|ADB devicename|
|origin|String|True|Name of device (from RGC settings)|
|pool|String|False|Configpool for this area|
|walker|String|True|Walker of this area|

## Settings
| Field Name | Type  | Required  | Description   |
| --         | --    | --        | --            |
|account_rotation|Boolean|False|Rotate accounts (f.e. to prevent long cool downs) - Only for PTC|
|clear_game_data|Boolean|False|Clear game data if logins fail multiple times|
|cool_down_sleep|Boolean|False|Add extra cooldown after teleport|
|delay_after_hatch|Decimal|False|Delay in minutes to wait before moving to the location of a hatched egg. Raidbosses do not necessarily appear immediately. (Default: 3.5)|
|ggl_login_mail|String|False|Declare a login address or domain from phone (Empty = first @gmail.com entry)<br>Use \| to set more the one account (address\|address)|
|logintype|String|False|Select login type for automatic login. If using Google make sure that account already exists on device.|
|mitm_wait_timeout|Decimal|False|Timeout in seconds while waiting for data after setting/reaching a location. (Default: 45)|
|post_pogo_start_delay|Decimal|False|Delay in seconds to wait after starting pogo. (Default: 60.0)|
|post_screenshot_delay|Decimal|False|The delay in seconds to wait after taking a screenshot to copy it and start the next (Default: 1)|
|post_teleport_delay|Decimal|False|Delay in seconds after teleport. (Default: 4.0)|
|post_turn_screen_on_delay|Decimal|False|Delay in seconds after a screenshot has been taken and about to be saved. (Default: 0.2)|
|post_walk_delay|Decimal|False|Delay in seconds after reaching destination. (Default: 2.0)|
|ptc_login|String|False|PTC User/Password (Format username,password)<br>Use \| to set more the one account (username,password\|username,password)|
|reboot|Boolean|False|Reboot device if reboot_thresh is reached (Default: false)|
|reboot_thresh|Integer|False|Restart Phone after restart Pogo N times. (Default: 3)|
|restart_pogo|Decimal|False|Restart Pogo every N location-changes. (Default: 80. - 0 for never)|
|restart_thresh|Integer|False|Restart Pogo after reaching MITM Timeout N times. (Default: 5)|
|rotate_on_lvl_30|Boolean|False|Rotate accounts if player level >= 30 (for leveling mode)|
|rotation_waittime|Decimal|False|Rotate accounts if wait time is longer than x seconds after teleport (Default: 300 - requires account_rotation to be enabled)|
|route_calc_algorithm|String|False|Method of calculation for routes. (Default: optimized)|
|screendetection|Boolean|False|Use this argument if there are login/logout problems with this device or you want to levelup accounts|
|screenshot_quality|Integer|False|Quality of screenshot (Default: 80)|
|screenshot_type|String|True|Type of screenshot (Default: jpeg)|
|screenshot_x_offset|Integer|False|Adjust the x-axis click offset on phones with softbars and/or black upper bars. (+ right - left / Default: 0)|
|screenshot_y_offset|Integer|False|Adjust the y-axis click offset on phones with softbars and/or black upper bars. (+ down - up / Default: 0)|
|startcoords_of_walker|String|False|Start Coords of Walker (Default: None) (Format: 123.45,67.89)|
|vps_delay|Decimal|False|Set click delay for pokestop walker (VPS -> local phone) (Default: 0)|
|walk_after_teleport_distance|Decimal|False|Walk in meters to walk after teleport. Might help loading data (Default: None)|