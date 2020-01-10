# Devices

## API Definition

The following definition is available for Device resources

Field Name | Type | Required | Default | Description
-- | -- | -- | -- | --
adbname|String|False|None|ADB devicename
origin|String|True|None|Name of device (from RGC settings)
pool|URI-/api/devicepool|False|None|Configpool for this area
walker|URI-/api/walker|True|None|Walker of this area

### Settings

Field Name | Type | Required | Default | Description
-- | -- | -- | -- | --
account_rotation|Boolean|False|False|Rotate accounts (f.e. to prevent long cool downs) - Only for PTC
clear_game_data|Boolean|False|False|Clear game data if logins fail multiple times
cool_down_sleep|Boolean|False|False|Add extra cooldown after teleport
delay_after_hatch|Decimal|False|3.5|Delay in minutes to wait before moving to the location of a hatched egg. Raidbosses do not necessarily appear immediately.
ggl_login_mail|String|False|None|Declare a login address or domain from device (Empty = first @gmail.com entry).  Use \| to set more the one account (address\|address)
inventory_clear_item_amount_tap_duration|Decimal|False|3.0|Number of seconds to tap the + button when clearing an inventory item
inventory_clear_rounds|Integer|False|10|Number of rounds to clear the inventory
injection_thresh_reboot|Integer|False|20|Reboot (if enabled) device after not injecting for X times in a row
logintype|String|False|google|Select login type for automatic login. If using Google make sure that account already exists on device
mitm_wait_timeout|Decimal|False|45|Timeout in seconds while waiting for data after setting/reaching a location.
post_pogo_start_delay|Decimal|False|60.0|Delay in seconds to wait after starting pogo
post_screenshot_delay|Decimal|False|1.0|The delay in seconds to wait after taking a screenshot to copy it and start the next
post_teleport_delay|Decimal|False|7.0|Delay in seconds after teleport
post_turn_screen_on_delay|Decimal|False|See Description|Delay in seconds after a screenshot has been taken and about to be saved (Default: 2.0 / 7.0 - Task Dependent)
post_walk_delay|Decimal|False|7.0|Delay in seconds after reaching destination with the speed given
ptc_login|String|False|None|PTC User/Password (Format username,password).  Use \| to set more the one account (username,password\|username,password)
reboot|Boolean|False|False|Reboot device if reboot_thresh is reached
reboot_thresh|Integer|False|3|Restart device after restart Pogo N times. This value is doubled when init is active
restart_pogo|Integer|False|0|Restart Pogo every N location-changes.  Use 0 for never
restart_thresh|Integer|False|5|Restart Pogo after reaching MITM Timeout N times. This value is doubled when init is active
rotate_on_lvl_30|Boolean|False|False|Rotate accounts if player level >= 30 (for leveling mode)
rotation_waittime|Decimal|False|300|Rotate accounts if wait time is longer than x seconds after teleport.  Requires account_rotation to be enabled
screendetection|Boolean|False|False|Use this argument if there are login/logout problems with this device or you want to levelup accounts
screenshot_quality|Integer|False|80|Quality of screenshot 
screenshot_type|String|True|jpeg|Type of screenshot
screenshot_x_offset|Integer|False|0|Adjust the x-axis click offset on devices with softbars and/or black upper bars. (+ right - left)
screenshot_y_offset|Integer|False|0|Adjust the y-axis click offset on devices with softbars and/or black upper bars. (+ down - up)
startcoords_of_walker|String|False|None|Start Coords of Walker (Default: None) (Format: 123.45,67.89)
vps_delay|Decimal|False|0|Set click delay for pokestop walker (VPS -> local device)
walk_after_teleport_distance|Decimal|False|None|Walk in meters to walk after teleport. Might help loading data

## JSON RPC
The following RPC implementations are available

### Pause / Unpause device
This will recalculate the route with the given area options.  Once it has successfully recalculated the route all devices will be disconnected and reconnected
call: device_state
args:
    active: Integer representing the state of the device.  If the state is 0 it will pause the device by disconnecting the device and not allowing it to reconnect.  Any other value will clear the connection block. 