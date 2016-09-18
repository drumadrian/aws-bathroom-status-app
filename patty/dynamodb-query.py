import boto3
from boto3.dynamodb.conditions import Key, Attr
import sys
import json
import time
from datetime import date, datetime
import string
import os, time

#timezone changes
os.environ['TZ'] = 'America/Los_Angeles'

#global variables
today = date.today()

table_name = "study-guru-bathroom"
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

#############get filtered data
def getFilter(gender, stall):

	try:
		#get the latest value for the day specified
		record_exist = table.query(
			KeyConditionExpression=Key('gender').eq(gender) & Key('stall').eq(stall)
		)
		output = []
		for items in record_exist['Items']:
			output.append({ 'gender1': items['gender'], 'stall': items['stall'] })
		# return output

		#get the latest value for the day specified
		record_exist = table.query(
			IndexName='global_testing',
			KeyConditionExpression=Key('bathroom').eq('B')
		)
		# output = []
		for items in record_exist['Items']:
			output.append({ 'gender2': items['gender'], 'stall': items['stall'] })
		# return output

		#get the latest value for the day specified
		record_exist = table.query(
			IndexName='local_testing',
			KeyConditionExpression=Key('stall').eq(1) & Key('status').eq(1)
		)
		# output = []
		for items in record_exist['Items']:
			output.append({ 'gender3': items['gender'], 'stall': items['stall'] })

		return output

	except Exception as err:
		print("Error occurred:", err)
		sys.exit()

def lambda_handler(event, context):
	output = []
	output = getFilter('M', 1)
	print output

# event = json.loads('{ "getType": "day", "filter": "2016-07-03" }')
# event = json.loads('{ "getType": "day", "filter": "2016-07" }')
# event = json.loads('{ "getType": "month", "filter": "2016" }')
# event = json.loads('{ "getType": "year", "filter": "2016" }')
# event = json.loads('{ "getType": "year", "filter": "2016" }')
# event = json.loads('{ "getType": "all" }')
# lambda_handler(event, context)