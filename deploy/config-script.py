import boto3
import json  #I'm sure I'll need it at some point.  :-) 






################################################################################
#   Global Config Settings
################################################################################
DEBUG = True
DEFAULT_GIT_REPO_URL = "git@github.com:drumadrian/aws-bathroom-status-app.git"
USE_AWS_S3_CONFIG_SCRIPT_TO_INITIALIZE = False
################################################################################




################################################################################
#   ToDo:
      # Allow config script to use AWS S3 for variables
################################################################################




################################################################################
#   Outline
################################################################################

# Clone Git repo
# Create zip File for Lambda functions 
# Get system config file from AWS S3  
# Update Lambda functions with new code 
# Turn on versioning for needed AWS S3 bucket
# Add asset tags to resources if needed
# Attach Policies to Roles if needed
# Create API using swagger file
# Setup Lambda trigger for AWS S3 config file
# Update date/time configuration data file in AWS S3 bucket
# Setup DNS for S3 website bucket
# Setup DNS for API
# Setup trigger on Config S3 bucket for config update Lambda function to sync setting into DynomoDB
# Deploy AWS API Gateway API 
# Publish config date to AWS SNS Topic for the system admin















def lambda_handler(event, context):

    if DEBUG:
        print "event={}".format(event)
        print "context={}".format(context)


    return "lambda_handler() complete"





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

    # Create offline testing context variable 
    context = ""
    lambda_handler(event, context)
 






