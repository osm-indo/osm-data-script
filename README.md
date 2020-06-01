# osm-data-script
This script was developed to address a problem where a country level PBF is still too big to download or analysed. Thus, the purpose of the script is to clip OSM PBF data by sub national admin boundaries (in .poly format). The example result of this script can be accessed at the OSM Indonesia Data ([English](https://openstreetmap.id/en/data-openstreetmap-indonesia/) | [Indonesia](https://https://openstreetmap.id/data-openstreetmap-indonesia/)) page.

An additional Osmosis command performed to count how many buildings within each clipped PBF file to provide overview of how many buildings have been mapped per province. The simple graph of the result can be accessed at Building Statistic Report ([English](https://openstreetmap.id/data/osmstatsbar_en.html) | [Indonesia](https://openstreetmap.id/data/osmstatsbar_id.html)) page.

It is recommended to run the command in cron jobs to automate the process periodically.

## Requirements
- [Osmosis](https://wiki.openstreetmap.org/wiki/Osmosis), to filter the building tag inside the PBF file
- [Osmconvert](https://wiki.openstreetmap.org/wiki/Osmconvert), to chop the PBF file and count the buildings inside the PBF
- Poly files (put it all under `poly` folder), the script will automatically split based on the content of this directory. Surely it will only work if the sub-national boundary still within country boundary.

## Start the script
`$ python scriptosm.py <geofabrik-country-url-link>`

### Example
`$ python scriptosm.py https://download.geofabrik.de/asia/indonesia-latest.osm.pbf`
