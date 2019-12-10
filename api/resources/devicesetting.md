# API Definition

The following definition is available for Device Pool resources

Field Name | Type | Required | Default | Description
-- | -- | -- | -- | --
devicepool|String|True|None|Name for the global device settings

## Settings

Field Name | Type | Required | Default | Description
-- | -- | -- | -- | --
cool_down_sleep|Boolean|False|False|Add extra cooldown after teleport
delay_after_hatch|Decimal|False|3.5|Delay in minutes to wait before moving to the location of a hatched egg. Raidbosses do not necessarily appear immediately.
inventory_clear_item_amount_tap_duration|Decimal|False|3.0|Number of seconds to tap the + button when clearing an inventory item
inventory_clear_rounds|Integer|False|10|Number of rounds to clear the inventory
injection_thresh_reboot|Integer|False|20|Reboot (if enabled) device after not injecting for X times in a row
mitm_wait_timeout|Decimal|False|45|Timeout in seconds while waiting for data after setting/reaching a location
post_pogo_start_delay|Decimal|False|60|Delay in seconds to wait after starting pogo
post_screenshot_delay|Decimal|False|1|The delay in seconds to wait after taking a screenshot to copy it and start the next
post_teleport_delay|Decimal|False|7.0|Delay in seconds after a teleport.
post_turn_screen_on_delay|Decimal|False|See Description|Delay in seconds after a screenshot has been taken and about to be saved (Default: 2.0 / 7.0 - Task Dependent)
post_walk_delay|Decimal|False|7.0|Delay in seconds after reaching destination with the speed given
reboot|Boolean|False|False|Reboot device if reboot_thresh is reached.  This value is doubled when init is active
reboot_thresh|Integer|False|3|Restart device after restart Pogo N times. This value is doubled when init is active
restart_pogo|Integer|False|0|Restart Pogo every N location-changes.  Use 0 for never
restart_thresh|Integer|False|5|Restart Pogo after reaching MITM Timeout N times. This value is doubled when init is active
screendetection|Boolean|False|False|Use this argument if there are login/logout problems with this device or you want to levelup accounts
screenshot_quality|Integer|False|80|Quality of screenshot 
screenshot_type|String|True|jpeg|Type of screenshot
screenshot_x_offset|Integer|False|0|Adjust the x-axis click offset on devices with softbars and/or black upper bars. (+ right - left)
screenshot_y_offset|Integer|False|0|Adjust the y-axis click offset on devices with softbars and/or black upper bars. (+ down - up)
startcoords_of_walker|String|False|None|Start Coords of Walker (Default: None) (Format: 123.45,67.89)
vps_delay|Decimal|False|0|Set click delay for pokestop walker (VPS -> local device)
walk_after_teleport_distance|Decimal|False|None|Walk in meters to walk after teleport. Might help loading data
