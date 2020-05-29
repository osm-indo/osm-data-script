import os
import sys

poly_files = ['Aceh', 'SumateraUtara', 'SumateraBarat', 'Riau', 'KepulauanRiau', 'Jambi', 'KepulauanBangkaBelitung',
              'Bengkulu', 'SumateraSelatan', 'Lampung', 'Banten', 'JawaBarat', 'Jakarta',
              'JawaTengah', 'JawaTimur', 'Yogyakarta', 'KalimantanBarat', 'KalimantanTengah',
              'KalimantanTimur', 'KalimantanSelatan', 'KalimantanUtara', 'Bali', 'NTB', 'NTT', 'Maluku',
              'MalukuUtara', 'SulawesiUtara', 'Gorontalo', 'SulawesiTengah', 'SulawesiBarat', 'SulawesiSelatan',
              'SulawesiTenggara', 'Papua', 'PapuaBarat']


for poly in poly_files:    
    # downloading pbf data in geofabrik
    downloadpbf = "wget -N http://download.geofabrik.de/asia/indonesia-latest.osm.pbf"
    os.system(downloadpbf)
    
    # clipping data into pbf data
    clip2province = "/usr/sbin/osmconvert indonesia-latest.osm.pbf -B=/var/www/html/data/poly/{0}.poly -o=pbf/{0}.pbf".format(poly)
    os.system(clip2province)

    # Get permission pbf data
    permission = "chmod +r pbf/*"
    os.system(permission)

    # filtering osm data based on building
    filterbuilding = "bin/osmosis --read-pbf pbf/{0}.pbf --tf accept-ways building=* --tf reject-nodes --tf reject-relations --write-pbf pbf/{0}_building.pbf".format(poly)
    os.system(filterbuilding)

    # showing osm data statistic
    osmstats = "/usr/sbin/osmconvert pbf/{0}_building.pbf --out-statistics > stat/{0}.stat".format(poly)
    os.system(osmstats)
