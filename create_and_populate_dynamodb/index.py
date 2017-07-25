import boto3
from boto3.dynamodb.conditions import Key, Attr
import sys
import datetime
import os



def createDynamoDBTable(table_name):
    """
    Checks if the DynamoDB table exists. Otherwise, it will create
    a table and wait for it to complete creation before continuing
    with the rest of the script.
    Adrian Alternative database fields:  Bathroom ID, Stall ID, Gender, bstatus, Time of Last bstatus, Stall Name
    """

    # AWS Client - Raw Low Level client
    client = boto3.client('dynamodb')

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
                    {
                        'AttributeName': 'unique_id',
                        'AttributeType': 'S'
                    },
                    # {
                    #     'AttributeName': 'gender',
                    #     'AttributeType': 'S'
                    # },
                    # {
                    #     'AttributeName': 'building',
                    #     'AttributeType': 'S'
                    # },
                    # {
                    #     'AttributeName': 'floor',
                    #     'AttributeType': 'S'
                    # },
                    # {
                    #     'AttributeName': 'bathroom',
                    #     'AttributeType': 'N'
                    # },
                    # {
                    #     'AttributeName': 'bstatus',
                    #     'AttributeType': 'N'
                    # },
                    # {
                    #     'AttributeName': 'timestamp',
                    #     'AttributeType': 'S'
                    # }
                ],
                KeySchema=[
                    {
                        'AttributeName': 'unique_id',                #concatenation_of_stall_bathroom_and_building
                        'KeyType': 'HASH'                           #AWS calls this a Partition Key
                    },
                    # {
                    #     'AttributeName': 'gender',
                    #     'KeyType': 'RANGE'                          #AWS calls this a Sort Key
                    # }
                ],
                # LocalSecondaryIndexes=[
                #     {
                #         'IndexName': 'stall_bstatus',
                #         'KeySchema': [
                #             {
                #                 'AttributeName': 'stall',
                #                 'KeyType': 'HASH'
                #             },
                #             {
                #                 'AttributeName': 'bstatus',
                #                 'KeyType': 'RANGE'
                #             }
                #         ],
                #         'Projection':{
                #             'ProjectionType': 'ALL'
                #         },
                #     },
                #     {
                #         'IndexName': 'stall_bathroom',
                #         'KeySchema': [
                #             {
                #                 'AttributeName': 'stall',
                #                 'KeyType': 'HASH'
                #             },
                #             {
                #                 'AttributeName': 'bathroom',
                #                 'KeyType': 'RANGE'
                #             }
                #         ],
                #         'Projection':{
                #             'ProjectionType': 'ALL'
                #         },
                #     }
                # ],
                # GlobalSecondaryIndexes=[
                #     {
                #         'IndexName': 'global_testing',
                #         'KeySchema': [
                #             {
                #                 'AttributeName': 'bathroom',
                #                 'KeyType': 'HASH'
                #             },
                #             {
                #                 'AttributeName': 'timestamp',
                #                 'KeyType': 'RANGE'
                #             }
                #         ],
                #         'Projection':{
                #             'ProjectionType': 'ALL'
                #         },
                #         'ProvisionedThroughput': {
                #             'ReadCapacityUnits': 1,
                #             'WriteCapacityUnits': 1
                #         }
                #     }
                # ],
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


def addDynamoDBData(table, unique_id, gender, stall, bstatus, bathroom, timestamp):
    """
    Puts the payload from the script into a DynamoDB table

    :param gender: M or F
    :type summary_date: string
    :param stall: the stall number
    :type summary_type: int
    :param bstatus: 0=occupied, 1=vacant
    :type summary_generated: int
    :param bathroom: the bathroom identifier (bathrooms contain stalls)
    :type summary_generated: string
    :param timestamp: the time that the stall was last marked occupied or vacant
    :type summary_generated: int
    """
    try:
        # add the data to the dynamodb
        response = table.put_item(
            Item={
                'gender': gender,
                'unique_id': unique_id,
                'stall': stall,
                'bstatus': bstatus,
                'bathroom': bathroom,
                'timestamp': timestamp
            }

        )
        # print response
        print "Added {0} {1} {2} {3} data to DynamoDB".format(gender, str(stall), str(bstatus), str(bathroom))

    except Exception as err:
        print("Error occurred while adding data to the new DynamoDB table")
        print("Error occurred:", err)
        sys.exit()

def populate_database(initial_database_PAYLOAD, table_name):
    # AWS Client - Raw Low Level client
    # client = boto3.client('dynamodb')

    # DynamoDB resource - High Level (Object Oriented)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    for value in initial_database_PAYLOAD:
        unique_id = "{0}{1}{2}".format(value['gender'], value['stall'] , value['bathroom'])
        addDynamoDBData(table, unique_id, value['gender'], value['stall'], value['bstatus'], value['bathroom'], value['timestamp'])



##################################################
    # LAMBDA HANDLER FUNCTION 
##################################################
def handler(event, context):
    """
    Create the DynamoDB table, load the initial Payload data,

    :param event: The payload sent to the lambda functions endpoint
    :type event: dict|list|str|int|float|NoneType
    :param context: Runtime information
    :type context: LambdaContext
    """
    # run the program
    print "BEGIN: handler()"

    #########################   
    # START Refactored Code  
    #########################

    # timezone changes
    os.environ['TZ'] = 'America/Los_Angeles'

    # today's date
    # today = date.today()
    # today=datetime.date(2016, 9, 3)

    # DEFAULT DynamoDB table name (What is a collection of bathrooms called?)
    DEFAULT_table_name = "study-guru-bathrooms-default-name"

    # AWS Client - Raw Low Level client
    client = boto3.client('dynamodb')

    # DynamoDB resource - High Level (Object Oriented)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(DEFAULT_table_name)

    # payload
    PAYLOAD = [
        {
            "stall": 1,
            "gender": 'M',
            "bstatus": 0,
            "bathroom": 1,
            "timestamp": '1245678930'
        },
        {
            "stall": 2,
            "gender": 'M',
            "bstatus": 0,
            "bathroom": 1,
            "timestamp": '1245678920'
        },
        {
            "stall": 3,
            "gender": 'M',
            "bstatus": 0,
            "bathroom": 1,
            "timestamp": '1245678910'
        },
        {
            "stall": 4,
            "gender": 'M',
            "bstatus": 0,
            "bathroom": 2,
            "timestamp": '1245678909'
        },
        {
            "stall": 5,
            "gender": 'M',
            "bstatus": 1,
            "bathroom": 2,
            "timestamp": '1245678908'
        },
        {
            "stall": 6,
            "gender": 'M',
            "bstatus": 1,
            "bathroom": 2,
            "timestamp": '1245678907'
        },
        {
            "stall": 7,
            "gender": 'F',
            "bstatus": 0,
            "bathroom": 1,
            "timestamp": '1245678906'
        },
        {
            "stall": 8,
            "gender": 'F',
            "bstatus": 1,
            "bathroom": 1,
            "timestamp": '1245678905'
        },
        {
            "stall": 9,
            "gender": 'F',
            "bstatus": 0,
            "bathroom": 1,
            "timestamp": '1245678904'
        },
        {
            "stall": 10,
            "gender": 'F',
            "bstatus": 1,
            "bathroom": 2,
            "timestamp": '1245678903'
        },
        {
            "stall": 11,
            "gender": 'F',
            "bstatus": 0,
            "bathroom": 2,
            "timestamp": '1245678902'
        },
        {
            "stall": 12,
            "gender": 'F',
            "bstatus": 1,
            "bathroom": 2,
            "timestamp": '1245678901'
        }
    ]

    #########################
    # END Refactored Code  
    #########################




    if 'dynamodb_table_name' in os.environ:
        table_name = os.environ['dynamodb_table_name']
    else:
        table_name = DEFAULT_table_name
        createDynamoDBTable(table_name)

    populate_database(PAYLOAD, table_name)

    print "END: lambda run"
    return "DynamoDB Table Complete"



##################################################
# Used for desktop testing (outside of AWS Lambda)
##################################################

if __name__ == "__main__":
    # sys.exit(main())

    event=""

    # Populate context object to emulate execution environment in AWS Lambda
    context={
            'context_data': 'config_DATABASE_NAME',
            'context_data2': 'config_DATABASE_NAME',
            'context_data3': 'config_DATABASE_NAME'
            }





    print'\n BEGIN LOCAL (non-Lambda) EXECUTION \n'
    sys.exit(handler(event,context))




