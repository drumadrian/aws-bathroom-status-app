import boto3
import logging
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('bathroom-app')


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

    print "event={}".format(event)
    print "context={}".format(context)

    return "Setting bathroom status {0} complete".format(user_request)

