# this tools provides geolocation using maxmind geolite2 service
import sys
import geoip2.database
import pandas as pd

iplist = pd.read_csv("iplist.txt",header=None)
#ipaddress=sys.argv[1]
# periodically update the GeoLite2-City ip, specify the exact directory
reader = geoip2.database.Reader('GeoLite2-City_20210914/GeoLite2-City.mmdb')
# dataframe 
for index, record in iplist.iterrows():
	
	if "#" in record[0]:
		continue
	else:
		response = reader.city(record[0])
		
		#print(response.country)
		print(record[0],response.country.names["en"],response.country.iso_code,sep=",")
