import boto3
from boto3.dynamodb.conditions import Key
import sys
import datetime
import os



#ToDo:  Update this file to use boto3(the AWS Python SDK to provision and setup the DynamoDB)

#This Comment was made to be pushed and trigger Travis CI
#Try to trigger a build again 



# timezone changes
os.environ['TZ'] = 'America/Los_Angeles'

# today's date
today=datetime.date(2016, 9, 3)

# DynamoDB table name
table_name = "solar_data"

# AWS Client
client = boto3.client('dynamodb')

# DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

# Initial Bathroom App Entry for each bathroom payload
SOLAR_DATA_PAYLOAD = {
    "stall_number": 19050353,
    "stall_gender": 25639,
    "stall_status": 1380632400,
    "bathroom_number": 3322,
    "time_of_last_status": 1380632791,
    "name": 31
}

def createDynamoDBTable():
    """
    Checks if the DynamoDB table exists. Otherwise, it will create
    a table and wait for it to complete creation before continuing
    with the rest of the script.
    """
    try:
        # skip creating table if it already exists
        response = client.describe_table(
            TableName=table_name
        )
        print "Table %s found" % (table_name)
    except:
        print "Table %s not found...creating now" % (table_name)
        try:
            # table was not found create
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
                # wait until the table is finished being created before continuing
                waiter = client.get_waiter('table_exists')
                waiter.wait(
                    TableName=table_name
                )
                print "Table %s created" % (table_name)
            except Exception as err:
                print ("Error creating table")
                sys.exit()
        except Exception as err:
            print("Error occurred:", err)
            sys.exit()


def getSolarData():
    """
    Connect to solar provider and get the data about the
    energy generated by the solar panels.
    :return: data from solar panels
    :rtype: json
    """
    try:
        return SOLAR_DATA_PAYLOAD

    except Exception as err:
        print("Error occurred:", err)
        sys.exit()


def addDynamoDBData(summary_date, summary_type, summary_generated):
    """
    Puts the payload from the solar panels into a DynamoDB

    :param: summary_date: date data in the format: YYYY, YYYY-MM, YYYY-MM-DD
    :type: summary_date: string
    :param: summary_type: the date is one of: Year, Month, Day
    :type: summary_type: string
    :param: summary_generated: how much energy was generated for the type that Year/Month/Day
    :type: summary_generated: float
    """
    try:
        # add the data to the dynamodb
        response = table.put_item(
            Item={
                'date': summary_date,
                'type': summary_type,
                'generated': summary_generated
            }
        )
        # print response
        print "Added %s %s data to DynamoDB" % (summary_date, summary_type)

    except Exception as err:
        print("Error occurred:", err)
        sys.exit()


def addDay(solar_data):
    """
    Gets the day data from the solar data payload and sends it to the database.

    :param solar_data: data about the energy generated by the solar panels
    :type solar_data: json
    """
    summary_type = "day"
    energy_today = (str)((int)(solar_data['energy_today']) * .001)
    summary_date = (str)(solar_data['summary_date'])

    addDynamoDBData(summary_date, summary_type, energy_today)


def addMonth():
    """
    Get the month data from the current day just entered in the database
    OR you can send the solar_data payload and get the month data from there.
    Gets the current month total from the DynamoDB.
    Calculates the new current month total and sends it to the database.

    :param solar_data: data about the energy generated by the solar panels
    :type solar_data: json
    """
    print "add month"
    summary_type = "month"
    total_month = 0
    this_month = today.strftime("%Y-%m")

    try:
        # get all the values in the table for the current year & month
        record_exist = table.query(
            KeyConditionExpression=Key('type').eq('day') & Key('date').begins_with(this_month)
        )
        print record_exist
        if record_exist['Count'] != 0:
            for items in record_exist['Items']:
                total_month += (float)(items['generated'])

        addDynamoDBData(this_month, summary_type, (str)(total_month))

    except Exception as err:
        print("Error occurred:", err)
        sys.exit()


def addYear():
    """
    Get the year data from the current month just entered in the database
    Gets the current year total from the DynamoDB.
    Calculates the new current year total and sends it to the database.

    :param solar_data: data about the energy generated by the solar panels
    :type solar_data: json
    """
    summary_type = "year"
    total_year = 0
    this_year = today.strftime("%Y")
    try:
        # get all the values in the table for the current year
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
    """
    Create the DynamoDB table, get the solar data, add the day, month and year totals and store in DynamoDB.

    :param event: The payload sent to the lambda functions endpoint
    :type event: dict|list|str|int|float|NoneType
    :param context: Runtime information
    :type context: LambdaContext
    """
    # run the program
    print "BEGIN: solar_data lambda run"
    createDynamoDBTable()
    solar_data = getSolarData()
    addDay(solar_data)
    addMonth()
    addYear()
    print "STOPPED: solar_data lambda run"
    return "Solar Data DynamoDB Table Complete"