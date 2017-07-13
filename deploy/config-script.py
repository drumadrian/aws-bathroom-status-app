import boto3
import json  #I'm sure I'll need it at some point.  :-) 
import os





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
# Create zip Files for Lambda functions 
# Get system config file from AWS S3  
# Update Lambda functions with new code 
# Turn on versioning for needed AWS S3 bucket   (moved into CloudFormation)
# Add asset tags to resources if needed
# Attach Policies to Roles if needed            (moved into CloudFormation)
# Updated API using swagger file
# Setup Lambda trigger for AWS S3 config file
# Update date/time configuration data file in AWS S3 bucket
# Setup DNS for S3 website bucket
# Setup DNS for API
# Deploy AWS API Gateway API 
# Publish config data to AWS SNS Topic for the system admin















def create_zip_files_for_lambda(): 
    print("COMPLETED:  create_zip_files_for_lambda()")

def get_system_config_file():  
    print("COMPLETED:  get_system_config_file()")

def update_lambda_functions_code():
    print("COMPLETED:  update_lambda_functions_code()")

def add_tags_to_assets():
    print("COMPLETED:  add_tags_to_assets()")

def update_api_from_swagger():
    print("COMPLETED:  update_api_from_swagger()")

def setup_lambda_trigger_for_config():
    print("COMPLETED:  setup_lambda_trigger_for_config()")

def update_date_and_time_in_configuration():
    print("COMPLETED:  update_date_and_time_in_configuration()")

def setup_dns_for_s3_website():
    print("COMPLETED:  setup_dns_for_s3_website()")

def setup_dns_for_api():
    print("COMPLETED:  setup_dns_for_api()")

def deploy_api_gateway_api():
    print("COMPLETED:  deploy_api_gateway_api()")

def publish_config_data_to_system_admin():
    print("COMPLETED:  publish_config_data_to_system_admin()")


























def lambda_handler(event, context):

    if DEBUG:
        print "event={}".format(event)
        print "context={}".format(context)



    # clone_git_repo()
    create_zip_files_for_lambda() 
    get_system_config_file()  
    update_lambda_functions_code()
    # turn_on_versioning_for_buckets()                  (moved into CloudFormation)
    add_tags_to_assets()
    # attach_policies_to_roles()                        (moved into CloudFormation)
    update_api_from_swagger()
    setup_lambda_trigger_for_config()
    update_date_and_time_in_configuration()
    setup_dns_for_s3_website()
    setup_dns_for_api()
    deploy_api_gateway_api() 
    publish_config_data_to_system_admin()





    return "  lambda_handler() COMPLETE  "





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


    print("######### Starting config-script.py #########")

    event = dict()
    event['unique_id'] = 'F102'
    event['bstatus'] = 1

    # Create offline testing context variable 
    context = ""
    result = lambda_handler(event, context)

    print(result)
    print("######### COMPLETED config-script.py #########")
 






