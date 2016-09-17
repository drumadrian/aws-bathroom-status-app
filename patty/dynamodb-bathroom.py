import boto3
from boto3.dynamodb.conditions import Key, Attr
import sys
import datetime
import os

# timezone changes
os.environ['TZ'] = 'America/Los_Angeles'

# today's date
# today = date.today()
today=datetime.date(2016, 9, 3)
# DynamoDB table name
table_name = "study-guru-bathroom"

# AWS Client
client = boto3.client('dynamodb')

# DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

# payload
PAYLOAD = [
    {
    "gender": 'M',
    "stall": 1,
    "status": 0,
    "bathroom": 'A',
    "timestamp": '1245678930'
    },
    {
    "gender": 'M',
    "stall": 2,
    "status": 0,
    "bathroom": 'A',
    "timestamp": '1245678920'
    },
    {
    "gender": 'M',
    "stall": 3,
    "status": 0,
    "bathroom": 'A',
    "timestamp": '1245678910'
    },
    {
    "gender": 'M',
    "stall": 1,
    "status": 0,
    "bathroom": 'B',
    "timestamp": '1245678909'
    },
    {
    "gender": 'M',
    "stall": 2,
    "status": 1,
    "bathroom": 'B',
    "timestamp": '1245678908'
    },
    {
    "gender": 'M',
    "stall": 3,
    "status": 1,
    "bathroom": 'B',
    "timestamp": '1245678907'
    },
    {
    "gender": 'F',
    "stall": 1,
    "status": 0,
    "bathroom": 'A',
    "timestamp": '1245678906'
    },
    {
    "gender": 'F',
    "stall": 2,
    "status": 1,
    "bathroom": 'A',
    "timestamp": '1245678905'
    },
    {
    "gender": 'F',
    "stall": 3,
    "status": 0,
    "bathroom": 'A',
    "timestamp": '1245678904'
    },
    {
    "gender": 'F',
    "stall": 1,
    "status": 1,
    "bathroom": 'B',
    "timestamp": '1245678903'
    },
    {
    "gender": 'F',
    "stall": 2,
    "status": 0,
    "bathroom": 'B',
    "timestamp": '1245678902'
    },
    {
    "gender": 'F',
    "stall": 3,
    "status": 1,
    "bathroom": 'B',
    "timestamp": '1245678901'
    }
]

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
                    # {
                    #     'AttributeName': 'building',
                    #     'AttributeType': 'S'
                    # },
                    # {
                    #     'AttributeName': 'floor',
                    #     'AttributeType': 'S'
                    # },
                    {
                        'AttributeName': 'bathroom',
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': 'gender',
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': 'stall',
                        'AttributeType': 'N'
                    },
                    {
                        'AttributeName': 'status',
                        'AttributeType': 'N'
                    },
                    {
                        'AttributeName': 'timestamp',
                        'AttributeType': 'S'
                    }
                ],
                KeySchema=[
                    {
                        'AttributeName': 'stall',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'gender',
                        'KeyType': 'RANGE'
                    }
                ],
                LocalSecondaryIndexes=[
                    {
                        'IndexName': 'stall_status',
                        'KeySchema': [
                            {
                                'AttributeName': 'stall',
                                'KeyType': 'HASH'
                            },
                            {
                                'AttributeName': 'status',
                                'KeyType': 'RANGE'
                            }
                        ],
                        'Projection':{
                            'ProjectionType': 'ALL'
                        },
                    },
                    {
                        'IndexName': 'stall_bathroom',
                        'KeySchema': [
                            {
                                'AttributeName': 'stall',
                                'KeyType': 'HASH'
                            },
                            {
                                'AttributeName': 'bathroom',
                                'KeyType': 'RANGE'
                            }
                        ],
                        'Projection':{
                            'ProjectionType': 'ALL'
                        },
                    }
                ],
                GlobalSecondaryIndexes=[
                    {
                        'IndexName': 'global_testing',
                        'KeySchema': [
                            {
                                'AttributeName': 'bathroom',
                                'KeyType': 'HASH'
                            },
                            {
                                'AttributeName': 'timestamp',
                                'KeyType': 'RANGE'
                            }
                        ],
                        'Projection':{
                            'ProjectionType': 'ALL'
                        },
                        'ProvisionedThroughput': {
                            'ReadCapacityUnits': 1,
                            'WriteCapacityUnits': 1
                        }
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


def addDynamoDBData(gender, stall, status, bathroom, timestamp):
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
                'gender': gender,
                'stall': stall,
                'status': status,
                'bathroom': bathroom,
                'timestamp': timestamp
            }

        )
        # print response
        print "Added {0} {1} {2} {3} data to DynamoDB".format(gender, str(stall), str(status), bathroom)

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
    print "BEGIN: lambda run"
    createDynamoDBTable()
    for value in PAYLOAD:
        addDynamoDBData(value['gender'], value['stall'], value['status'], value['bathroom'], value['timestamp'])
    print "STOPPED: lambda run"
    return "DynamoDB Table Complete"