# Scripts

Here is a collection of useful scripts found in the `scripts/` directory.

## Spawnpoint Importer (import_allspawns.sh)

If you used to scan before and happen to still have your spawnpoints in your Monocle or Rocketmap database then you can use this script to import them to MAD. You must have the trs_spawn table already in your database and you must have filled out the Database portion of the MAD config file!

It's also possible to import spawnpoints from a RDM database.

## Intel Importer (intelimport.sh)

If you ran the MITM method for the first time, you will probably notice that all gyms are missing names and pictures. If you want to add this information, you can use this script. First of all, you'll need a CSV Export from the  [Ingress Intel Map](https://intel.ingress.com/intel). Install [IITC](https://iitc.me/) and the `IntelCsvExporterMADedition.js` from the scripts directory. Make sure to scrape all the necessary portals in your area and export the CSV file to your server. The second step is to run the script with the csv file as the first parameter.  
Example: `./intelimport.sh export.csv`.

## Databasesetup (databasesetup.py)

This script will take care of the database schema installation automatically so for example there is no need to install a whole Rocketmap frontend to just use the schema. Make sure to fill in the database credentials in the MAD `config.ini`, create an empty database and grant all permissions to the database user before running this script.

## Migrate to Rocketmap (migrate_to_rocketmap.sh)

This script will migrate your data from a RDM or Monocle database to a Rocketmap database. Before you run this you should run [OSM-rocketmap](https://github.com/cecpk/OSM-Rocketmap) or `databasesetup.py` and let it configure its database. After it has built its empty database you can run this script. If you were using Monocle with MAD spawnpoints do not change, so I dump that table from your monocle db and import it to your rocketmap db for you. If you have old spawnpoint info from before MAD then you want to use import_allspawns.sh as well. This script does not import things like controlling team/mons, or ex status, because MAD will fill this in after 1 scan.

If you were already scanning in MAD using your Monocle database, be sure to remove version.json so MAD will update your new rocketmap schema.

## Update Stops and Gyms (update_stopsgyms.sh)

This script will find and delete gyms that have changed to pokestops and pokestops that have changed to gyms.
