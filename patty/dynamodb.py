import boto3
from boto3.dynamodb.conditions import Key, Attr
import sys
import urllib2
from urllib2 import Request, urlopen, URLError, HTTPError, build_opener
import json
import time
from datetime import date, datetime
import string
import os, time

#timezone changes
os.environ['TZ'] = 'America/Los_Angeles'

#global variables
enphase_api_key = ""
enphase_userid = "" #https://developer.enphase.com/docs/quickstart.html
enphase_api_url = "https://api.enphaseenergy.com/api/v2"
enphase_system_id = ""

today = date.today()

table_name = "smylee_solar"
client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

#############creates and checks the dynamodbtable exists
def createDynamoDBTable():
	try:
		#skip creating table if it already exists
		response = client.describe_table(
			TableName=table_name
		)
		print "Table %s found"%(table_name)
	except:
		print "Table %s not found...creating now"%(table_name)
		try:
			#table was not found create
			response = client.create_table(
				TableName=table_name,
				AttributeDefinitions=[
					{
						'AttributeName': 'date',
						'AttributeType': 'S'
					},
					{
						'AttributeName': 'type',
						'AttributeType': 'S'
					},
				],
				KeySchema=[
					{
						'AttributeName': 'type',
						'KeyType': 'HASH'
					},
					{
						'AttributeName': 'date',
						'KeyType': 'RANGE'
					}
				],
				ProvisionedThroughput={
					'ReadCapacityUnits': 1,
					'WriteCapacityUnits': 1
				}
			)
			try:
				#wait until the table is finished being created before continuing
				waiter = client.get_waiter('table_exists')
				waiter.wait(
					TableName=table_name
				)
				print "Table %s created"%(table_name)
			except Exception as err:
				print ("Error creating table")
				sys.exit()
		except Exception as err:
			print("Error occurred:", err)
			sys.exit()


#############connect to enphase and get the data
def getEnphaseSolar():
	try:
		api_url = "%s/systems/%s/summary?summary_date=%s&key=%s&user_id=%s"%(enphase_api_url, enphase_system_id, today, enphase_api_key, enphase_userid)
		req = urllib2.Request(api_url)
		response = urlopen(req)
		solar_data = json.loads(response.read())

		return solar_data

	except Exception as err:
		print("Error occurred:", err)
		sys.exit()


#############adds values to dynamodb
def addDynamoDBData(summary_date, summary_type, summary_generated):
	try:
		#add the data to the dynamodb
		response = table.put_item(
			Item={
				'date': summary_date,
				'type': summary_type,
				'generated': summary_generated
			}
		)
		# return response
		print "Added %s %s data to DynamoDB"%(summary_date, summary_type)

	except Exception as err:
		print("Error occurred:", err)
		sys.exit()


#############add the day value
def addDay(solar_data):

	summary_type = "day"
	energy_today = (str)((int)(solar_data['energy_today']) * .001)
	summary_date = (str)(solar_data['summary_date'])

	addDynamoDBData(summary_date, summary_type, energy_today)

#############add the month value
def addMonth():

	summary_type = "month"
	total_month = 0
	this_month = today.strftime("%Y-%m")

	try:
		#get all the values in the table for the current year & month
		record_exist = table.query(
			KeyConditionExpression=Key('type').eq('day') & Key('date').begins_with(this_month)
		)

		if record_exist['Count'] != 0:
			for items in record_exist['Items']:
				total_month += (float)(items['generated'])

			addDynamoDBData(this_month, summary_type, (str)(total_month))		

	except Exception as err:
		print("Error occurred:", err)
		sys.exit()

#############add the year value
def addYear():

	summary_type = "year"
	total_year = 0
	this_year = today.strftime("%Y")
	try:
		#get all the values in the table for the current year
		record_exist = table.query(
			KeyConditionExpression=Key('type').eq('month') & Key('date').begins_with(this_year)
		)

		if record_exist['Count'] != 0:
			for items in record_exist['Items']:
				total_year += (float)(items['generated'])
			
			addDynamoDBData(this_year, summary_type, (str)(total_year))			

	except Exception as err:
		print("Error occurred:", err)
		sys.exit()


def lambda_handler(event, context):
	#run the program
	createDynamoDBTable()
	solar_data = getEnphaseSolar()
	addDay(solar_data)
	addMonth()
	addYear()