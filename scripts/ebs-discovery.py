#!/usr/bin/python
 
import sys
import datetime
import boto3
import json 

try:
    nregion = sys.argv[1]
 
except:
    print "Example: ebs-discovery.py REGION"
    sys.exit(1)

ebs = boto3.client('cloudwatch', region_name=nregion)

r = ebs.list_metrics(Namespace='AWS/EBS', MetricName='BurstBalance')


services = []

for metric in r['Metrics']:
    for dim in metric['Dimensions']:
        services.append({"{#VOLID}": dim['Value']})

raw = {"data": services}
print(json.dumps(raw))

#print(r['Metrics'][0]['Dimensions'][0]['Value'])

