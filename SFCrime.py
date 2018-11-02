import json
import requests
from sodapy import Socrata
import operator
import numpy as np
import location
#import pandas as pd
#import dateutil

unique_list = []
master_report = {}
unique_incidents = []

"""myCoords = get_location()
myLatitude = myCoords[0]
myLongitude = myCoords[1]
"""

def unique(incidentReport):
  for x in incidentReport:
    if x[0] not in unique_list:
      unique_list.append(x[0])
  return(unique_list)

def uniqueIncident(results):
  for x in results:
    if x['incident_description'] not in unique_incidents:
      unique_incidents.append(x['incident_description'])
  return unique_incidents


"""def assignToUnique(unique_list,incidentReport):
  for x in unique_list:
    for y in incidentReport:
      if x in y[0]:
"""


def assignCrime(unique_list,incidentReport):
	for x in unique_list:
		master_report.setdefault(x,[])
		for p in incidentReport:
			if x in p[0]:
				master_report[x].append(p[1:])
	return master_report


def makeIncidentReport(counter,neighborhood,incident_category,time,intersection):
    incidentData = neighborhood,incident_category,time,intersection
    for x in incidentData:
      incidentReport.append(incidentData)
      
"""      
def breakdownIncidentReport(incidentReport,neighborhood):
  for
"""

api_token = ##
secret_token = ##
endpoint = 'https://data.sfgov.org/resource/nwbb-fxkq.json'

client = Socrata("data.sfgov.org",
                  api_token,
                  username="alec.saucedo@gmail.com",
                  password="Mydogsophie25!")
                  

results = client.get("nwbb-fxkq", limit=2000)
counter = 0
incidentReport = []

for k in results:
  neighborhood = k['police_district']
  incident_category = k['incident_description']
  time = k['incident_datetime']
  if 'intersection' in k:
  	intersection = k['intersection']
  if 'Suspicious Act Towards Female' == incident_category:
    counter += 1
    makeIncidentReport(counter,neighborhood,incident_category,time,intersection)
  elif 'Sex' in incident_category:
    counter += 1
    makeIncidentReport(counter,neighborhood,incident_category,time,intersection)
  elif 'Harrassment' in incident_category:
    counter += 1
    makeIncident(counter,neighborhood,incident_category,time,intersection)
  elif 'Assault' in incident_category:
    counter += 1
    makeIncidentReport(counter,neighborhood,incident_category,time,intersection)
  elif 'Theft' in incident_category:
    counter += 1
    makeIncidentReport(counter,neighborhood,incident_category,time,intersection)
  #print(neighborhood, incident_category)"""""
print(counter)
incidentReport.sort(key=operator.itemgetter(2))
print(incidentReport)
print(unique(incidentReport))
print(uniqueIncident(results))
assignCrime(unique_list,incidentReport)
print(master_report)
#print(pd.incidentReport.groupby(neighborhood))
