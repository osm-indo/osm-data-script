import os
import sys

polypath = 'poly/'
poly_files = []

#list all poly files in the poly directory using os.listdir
for entry in os.listdir(polypath):
    if os.path.isfile(os.path.join(polypath, entry)) and not entry.startswith('.'):
        stripext = os.path.splitext(entry)[0]
        poly_files.append(stripext)

print "Detected poly files :", str(poly_files)[1:-1]

#check if pbf and stat folder exist, otherwise create it
if not os.path.exists('pbf'):
    os.makedirs('pbf')

if not os.path.exists('stat'):
    os.makedirs('stat')

# downloading pbf data in geofabrik
downloadpbf = "wget -N http://download.geofabrik.de/asia/indonesia-latest.osm.pbf"
os.system(downloadpbf)

for poly in poly_files:

    # clipping data into pbf data
    clip2province = "osmconvert indonesia-latest.osm.pbf -B=poly/{0}.poly -o=pbf/{0}.pbf".format(poly)
    os.system(clip2province)

    # give read permission to pbf data
    permission = "chmod +r pbf/{0}.pbf".format(poly)
    os.system(permission)

    # filtering osm data based on building tag
    filterbuilding = "osmosis --rb pbf/{0}.pbf --tf accept-ways building=* --tf reject-nodes --tf reject-relations --wb pbf/{0}_building.pbf".format(poly)
    os.system(filterbuilding)

    # count the building data and put it on stat file
    osmstats = "osmconvert pbf/{0}_building.pbf --out-statistics > stat/{0}.stat".format(poly)
    os.system(osmstats)
