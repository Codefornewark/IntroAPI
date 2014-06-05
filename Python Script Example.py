import requests
import pprint
from xml.etree import ElementTree
import os
import time
import datetime

f_z = open("C:/Users/sethw_000/Desktop/workfiles/Zoning_Applications.csv","w")
f_v = open("C:/Users/sethw_000/Desktop/workfiles/Vacants.csv","w")


authurl = 'https://cityofnewark.quickbase.com/db/main?act=API_Authenticate&username=sethwainer@gmail.com&password=50lakeshore&hours=24'

response = requests.get(authurl) #if proxies needed, add "proxies=proxies"
root = ElementTree.fromstring(response.content)
ticket = root[3].text

zoning_url = 'https://cityofnewark.quickbase.com/db/bieyv3sup?act=API_GenResultsTable&ticket='+ticket+'&apptoken=kftdqmds6d4zp9pn77edb3z9d4&query={%2715%27.LT.%2701-01-2015%27}AND{%2715%27.GT.%2701-01-2006%27}&clist=8.48.18.15&options=csv'
vacant_url = 'https://cityofnewark.quickbase.com/db/bhx9b5r2a?act=API_GenResultsTable&ticket='+ticket+'&apptoken=ca8k3wkce9gt5udycfrsgdpsngpd&clist=63.64.14.15.36.65.107.108&options=csv'

zoningresponse = requests.get(zoning_url) #, proxies=proxies)
vacantresponse = requests.get(vacant_url) #, proxies=proxies)

f_z.write(zoningresponse.content)
f_v.write(vacantresponse.content)

f_z = open("C:/Users/sethw_000/Desktop/workfiles/Zoning_Applications.csv")	
f_v = open("C:/Users/sethw_000/Desktop/workfiles/Vacants.csv")

	
wf = open(os.path.join("C:/Users/sethw_000/Desktop/workfiles", "Vacants_"+str(datetime.date.today())+".csv"),"w")
for line in f_v:
    newline = line.strip('\r\n')
    wf.write(newline)
    wf.write('\n')
	
wz = open(os.path.join("C:/Users/sethw_000/Desktop/workfiles", "Zoning_Applications_"+str(datetime.date.today())+".csv"),"w")
for line in f_z:
    newline = line.strip('\r\n')
    wz.write(newline)
    wz.write('\n')

	
r= requests.post('http://data.codefornewark.org/api/action/resource_update',
              data={
				"package_id":"vacant-properties",
				"id":"dc3d80c5-a71d-4349-9bb4-cf2b7b5e0d99",
				"name":"Vacant Properties",
				"format":"csv",
				"last_modified":datetime.datetime.today().strftime('%Y-%m-%dT%H:%M')
				},
			  
              headers={"X-CKAN-API-Key": "xxxxxxxxxxx"},
              files=[('upload', file('C:/Users/sethw_000/Desktop/workfiles/Vacants_'+str(datetime.date.today())+'.csv'))],
			  #proxies=proxies
			  )
			  
rr= requests.post('http://data.codefornewark.org/api/action/resource_update',
              data={
				"package_id":"zoning-permit-applications",
				"id":"65ac7313-6570-4bf7-b771-811a69839f07",
				"name":"zoning permit applications",
				"format":"csv",
				"last_modified":datetime.datetime.today().strftime('%Y-%m-%dT%H:%M')
				},
			  
              headers={"X-CKAN-API-Key": "xxxxxxxxxxxx"},
              files=[('upload', file('C:/Users/sethw_000/Desktop/workfiles/Zoning_Applications_'+str(datetime.date.today())+'.csv'))],
			  #proxies=proxies
			  )












