# -*- coding: utf-8 -*-
from __future__ import print_function # Python 2/3 compatibility

import random
import datetime
import boto3

dynamodb = boto3.resource('dynamodb', region_name='cn-north-1')

table = dynamodb.Table("dynamo-demo")

while 'true':
    id = str(random.randint(1, 10000))

    start_time = datetime.datetime.now()
    response = table.put_item(
       Item={
           'id': id,
           'value': "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
       }
    )
    end_time = datetime.datetime.now()

    delay = str(round((end_time - start_time).microseconds/1000))

    print("PutItem "+id+" succeeded in "+delay+" ms")

