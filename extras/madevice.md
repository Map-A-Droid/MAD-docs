## MADevice

[View MADevice](https://github.com/georgeherby/MADevice)

### What is MADevice
MADevice is a service that will alert you when a phone may be having an issue. It can be used if you just want to check the status of numerous phones accross many MAD instances from within Discord without having to load numerous MADmin windows. The following two sections detail each feature available.

#### No Data Alert
When running MADevice, it will check the last received time for data from PoGoDroid and then if the time is more than 20 minutes (or the configured duration) in the past, it will post a message to the channel set by webhook in servers.json
![](../_static/madevice/alert.png)

#### On-Demand Status (`!status`)
If you type `!status` in the channel set by `status_channel_id` in `servers.json`, you get an on-demand update across all servers (set in servers.json) and posted into Discord rather than opening up multiple browsers to see the data.

![](../_static/madevice/status.png)

### Installation
For up-to-date installation steps visit MADevice's [README](https://github.com/georgeherby/MADevice).
