import boto3
import logging
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('bathroom-app')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('study-guru-bathrooms')


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
        raise Exception('set_occupied error yo: {0}'.format(e))


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
        raise Exception('set_vacant error yo: {0}'.format(e))


def lambda_handler(event, context):
    """
    Create the DynamoDB table, load the initial Payload data,

    :param event: The payload sent to the lambda functions endpoint
    :type event: dict|list|str|int|float|NoneType
    :param context: Runtime information
    :type context: LambdaContext
    """
    # run the program
    logger.info("BEGIN: lambda run")

    # variables
    user_request = event['request']
    gender = event['gender']
    stall = event['stall']
    bathroom_number = event['bathroom']
    unique_id = '{0}{1}{2}'.format(gender, stall, bathroom_number)

    if user_request == 'set_occupied':
        logger.info('Setting {0} bathroom {1} stall {2} to occupied status.'.format(gender, bathroom_number, stall))
        set_occupied(unique_id)
    elif user_request == 'set_vacant':
        logger.info('Setting {0} bathroom {1} stall {2} to vacant status.'.format(gender, bathroom_number, stall))
        set_vacant(unique_id)
    else:
        error_message = 'Invalid request'
        logger.error(error_message)
        raise Exception(error_message)
    logger.info("STOPPED: lambda run")
    return "Setting bathroom status {0} complete".format(user_request)
