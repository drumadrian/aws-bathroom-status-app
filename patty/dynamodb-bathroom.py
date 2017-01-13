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

# DynamoDB table name (What is a collection of bathrooms called?)
table_name = "study-guru-bathrooms"

# AWS Client - Raw Low Level client
client = boto3.client('dynamodb')

# DynamoDB resource - High Level (Object Oriented)
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
            # table was not found, create the table
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
                        'KeyType': 'HASH'                           #AWS calls this a Partition Key
                    },
                    {
                        'AttributeName': 'gender',
                        'KeyType': 'RANGE'                          #AWS calls this a Sort Key
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
    Puts the payload from the script into a DynamoDB table

    :param: gender: M or F
    :type: summary_date: string
    :param: stall: the stall number
    :type: summary_type: int
    :param: status: 0=occupied, 1=vacant
    :type: summary_generated: int
    :param: bathroom: the bathroom identifier (bathrooms contain stalls)
    :type: summary_generated: string
    :param: timestamp: the time that the stall was last marked occupied or vacant
    :type: summary_generated: int
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
        print("Error occurred while adding data to the new DynamoDB table")
        print("Error occurred:", err)
        sys.exit()

def lambda_handler(event, context):
    """
    Create the DynamoDB table, load the initial Payload data,

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