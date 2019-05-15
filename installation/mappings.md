## MADmin
MADmin is a webfrontend to administrate MAD. Start it with `-wm` as a commandline parameter or add `with_madmin` to your config.ini

To just start MADmin and not the scanner itself, run:
```bash
python3 configmode.py
```
By default, MADmin will run on your localhost on port 5000, open `http://localhost:5000/` to access it.

### Mapping Editor
The Mapping Editor is the place to add devices, devicesetting-pools, walker, areas and auth methods. Some objects rely on eachother so the best practice is to add an area first, define an walker and assign the phone to the walker afterwards.

#### Devices
To add an device, just fill out the required fields. The Origin is used to identify the phone. It must be the exact same as in your RGC and (if you use it) Pogodroid settings.

Configpool and adbname are not necessary. 

Edit the settings of the device after adding it.

#### Devicesettings
If you are running multiple devices for example, from the same model, it might be useful to manage thier settings with a devicepool. Settings made to a devicepool will be applied to every phone in that pool.

The usage it very simple, fill in a name for the pool and edit the settings like it is a single phone.
