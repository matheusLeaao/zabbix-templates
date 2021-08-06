#!/usr/bin/python

import boto3
import json
import sys

ec2_regions = sys.argv[1:]

services = []

for region in ec2_regions:
    session = boto3.Session(region_name=region)
    #session = boto3.Session(aws_access_key_id='',aws_secret_access_key='',region_name=region)
    conn = session.resource('ec2')
    instances = conn.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
      if instance.state["Name"] == "running":
         name = instance.id
         for t in instance.tags:
           if t['Key'] == 'Name':
             name = t['Value']
         services.append({"{#REGION}": region, "{#INSTANCEID}": instance.id,"{#PRIVATEIP}": instance.private_ip_address,"{#INSTANCETYPE}": instance.instance_type,"{#INSTANCENAME}": name})

raw = {"data": services}

print(json.dumps(raw))
