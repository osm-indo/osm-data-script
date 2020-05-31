import os
import sys

poly_files = ['Aceh', 'SumateraUtara', 'SumateraBarat', 'Riau', 'KepulauanRiau', 'Jambi', 'KepulauanBangkaBelitung',
              'Bengkulu', 'SumateraSelatan', 'Lampung', 'Banten', 'JawaBarat', 'Jakarta',
              'JawaTengah', 'JawaTimur', 'Yogyakarta', 'KalimantanBarat', 'KalimantanTengah',
              'KalimantanTimur', 'KalimantanSelatan', 'KalimantanUtara', 'Bali', 'NTB', 'NTT', 'Maluku',
              'MalukuUtara', 'SulawesiUtara', 'Gorontalo', 'SulawesiTengah', 'SulawesiBarat', 'SulawesiSelatan',
              'SulawesiTenggara', 'Papua', 'PapuaBarat']

#check if pbf and stat folder exist, otherwise create it
if not os.path.exists('pbf'):
    os.makedirs('pbf')

if not os.path.exists('stat`'):
    os.makedirs('stat')

# downloading pbf data in geofabrik
downloadpbf = "wget -N http://download.geofabrik.de/asia/indonesia-latest.osm.pbf"
os.system(downloadpbf)

for poly in poly_files:

    # clipping data into pbf data
    clip2province = "osmconvert indonesia-latest.osm.pbf -B=data/poly/{0}.poly -o=pbf/{0}.pbf".format(poly)
    os.system(clip2province)

    # Get permission pbf data in server
    permission = "chmod +r pbf/*"
    os.system(permission)

    # filtering osm data based on building
    filterbuilding = "osmosis --read-pbf pbf/{0}.pbf --tf accept-ways building=* --tf reject-nodes --tf reject-relations --write-pbf pbf/{0}_building.pbf".format(poly)
    os.system(filterbuilding)

    # showing osm data statistic
    osmstats = "osmconvert pbf/{0}_building.pbf --out-statistics > stat/{0}.stat".format(poly)
    os.system(osmstats)
