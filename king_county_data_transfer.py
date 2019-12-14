#This script is to be used to download address and parcel data from King county to be used by Northshore's GIS staff. The file is only for there area.
import requests 
r = requests.get('https://gisdata.kingcounty.gov/arcgis/rest/services/OpenDataPortal/property__parcel_address_area/MapServer/1722/query?where=1%3D1&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&resultOffset=&resultRecordCount=&f=pjson')
#The request URL is a pre Query URL that used GIS rest service to take only the area that Northshore wants to make the file smaller.
n = 3 #for lopp
print(r.headers) #to check status code and header info.
#below is a check to see if i have a full request and if not it will run a time loop to delay the script while the download is complete.
while r.status_code != 200 and n > 0:
    import time
    time.sleep(2)
    n = n - 1
    print(n)
#This loop checks to make sure there is a good response if not it will print to screen the errors and status code and log them to a response file in the local directory.
if r.status_code == 200: 
        print("Response good")
else:  # not 200 or 202 and not 204
    print(f'Not sucessful call with status code {r.status_code} {r.text}') 
    print(r.json()) 
    with open('response.txt', 'a') as localfile:  
        localfile.write(r.text)
        exit()

#Below takes a good data that was requested and saves it to a zip file. For gis use.
with open ('kc_gis_data.zip', 'wb') as f: 
    f.write(r.content)
print("Downloaded File")  
