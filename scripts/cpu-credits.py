#!/usr/bin/python3
import boto3
import datetime
import sys
import pdb

idhost = sys.argv[1]
region = sys.argv[2]

end = datetime.datetime.utcnow()
start = end - datetime.timedelta(minutes=10)

#cloudwatch = boto3.client('cloudwatch',aws_access_key_id='',aws_secret_access_key='',region_name=region)
cloudwatch = boto3.client('cloudwatch',region_name=region)

response = cloudwatch.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='CPUCreditBalance',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': idhost
        },
    ],
    StartTime=start,
    EndTime=end,
    Period=300,
    Statistics=['Average'],
    Unit='Count'
)

if  len(response['Datapoints']) > 0:
    credit = (response['Datapoints'][0]['Average'])
    print(credit)
else:
    print(-1)

