
# from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr



###
 #  This code was generated by SwaggerHub from the following API:
 # 
 #  https://swaggerhub.com/api/drumadrian/bathroom-app-get-status/1.1
 #  
 #  The content of this file will never be modified after initial
 #  generation--adding or changing parameters will not be reflected
 #  here.  You can regenerate this with the latest definition by
 #  deleting the lambda and allowing SwaggerHub to recreate it
 ###

def lambda_handler(event, context):
	# string: (required)  pass DynamoDB Primary partition key to get an entry
	unique_id = event.get('unique-id')
	# unique_id2 = event['unique-id']


	# print 'event={}'.format(event)

	print("context={}").format(context)

	print("unique_id={}").format(unique_id)
	# print "unique_id2={}".format(unique_id2)


	dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="https://dynamodb.us-west-2.amazonaws.com")

	table = dynamodb.Table('study-guru-bathrooms')

	print("All bathrooms")

	response = table.query(
	    KeyConditionExpression=Key('timestamp').gt(0)
	)

	for i in response['Items']:
		print("unique_id={} : bstatus={}").format(i['unique_id'], i['bstatus'])


	return response


#END 
  # return 'created by SwaggerHub'


myevent={'unique-id':2}
mycontext={'unique-id':2}

lambda_handler(myevent, mycontext)