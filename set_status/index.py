import boto3
import logging
import json
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('bathroom-app')

dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('study-guru-bathrooms')
dynamodb_table_name = os.environ['dynamodb_table_name']
table = dynamodb.Table(dynamodb_table_name)



def set_occupied(unique_id):
    try:
        response = table.update_item(
            Key={
                'unique_id': unique_id
            },
            UpdateExpression="set bstatus = :r",
            ExpressionAttributeValues={
                                          ':r': '1'
                                      },
            ConditionExpression='(attribute_exists(unique_id))',
            ReturnValues="UPDATED_NEW"
        )
        logger.info("UpdateItem succeeded:")
        logger.info(json.dumps(response, indent=4))
    except Exception as e:
        raise Exception('set_occupied error: {0}'.format(e))


def set_vacant(unique_id):
    """
    Create the DynamoDB table, load the initial Payload data,

    :param unique_id: The unique_id of the column to update in dynamo
    :type unique_id: str
    """
    try:
        response = table.update_item(
            Key={
                'unique_id': unique_id
            },
            UpdateExpression="set bstatus = :r",
            ExpressionAttributeValues={
                ':r': '0'
            },
            ConditionExpression='(attribute_exists(unique_id))',
            ReturnValues="UPDATED_NEW"
        )
        logger.info("UpdateItem succeeded:")
        logger.info(json.dumps(response, indent=4))
    except Exception as e:
        raise Exception('set_vacant error: {0}'.format(e))


def handler(event, context):
    """
    Create the DynamoDB table, load the initial Payload data,

    :param event: The payload sent to the lambda functions endpoint
    :type event: dict|list|str|int|float|NoneType
    :param context: Runtime information
    :type context: LambdaContext
    """
    # run the program
    logger.info("BEGIN: lambda run")


    #TODO:  If parameters are empty return a 400 error 

    # # variables when using Lambda Proxy and HTTP body parameters
    # user_request = event['request']
    # gender = event['gender']
    # stall = event['stall']
    # bathroom_number = event['bathroom']
    # unique_id = '{0}{1}{2}'.format(gender, stall, bathroom_number)

    # if user_request == 'set_occupied':
    #     logger.info('Setting {0} bathroom {1} stall {2} to occupied status.'.format(gender, bathroom_number, stall))
    #     set_occupied(unique_id)
    # elif user_request == 'set_vacant':
    #     logger.info('Setting {0} bathroom {1} stall {2} to vacant status.'.format(gender, bathroom_number, stall))
    #     set_vacant(unique_id)
    # else:
    #     error_message = 'Invalid request'
    #     logger.error(error_message)
    #     raise Exception(error_message)
    # logger.info("STOPPED: lambda run")
    # return "Setting bathroom status {0} complete".format(user_request)


    print("event[bstatus]={}".format(event['bstatus']) )
    print( "event type={}".format(type(event['bstatus'])) )
    print("event={}".format(event))
    print("table={}".format(table))

    requested_status = int(event['bstatus'])

    if requested_status == 1:
        user_request = 'set_occupied'
        set_occupied(event['unique_id'])
    elif requested_status == 0:
        set_vacant(event['unique_id'])
        user_request = 'set_vacent'
    else:
        error_message = 'Invalid request - the variable requested_status was not set to either 0 or 1'
        logger.error(error_message)
        # raise Exception(error_message)
        return "Setting bathroom status using event={0} failed".format(event)

    logger.info("STOPPED: lambda run")
    return "Setting bathroom status {0} complete".format(user_request)

#####################################################################################
#  Code below is for Desktop testing 
#####################################################################################

if __name__ == "__main__":

    # #Test events 
    # event =
    # {
    #   "request": "set_vacant",
    #   "bathroom": 2,
    #   "gender": "F",
    #   "stall": 10
    # }

    event = dict()
    event['unique_id'] = 'F102'
    event['bstatus'] = 1


    context = ""
    handler(event, context)
 








