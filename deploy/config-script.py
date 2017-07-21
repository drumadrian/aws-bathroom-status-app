import boto3
import json  #I'm sure I'll need it at some point.  :-) 
import os
from importlib.machinery import SourceFileLoader
# bathroom_config_lib = SourceFileLoader("bathroom_config_lib", "/home/ec2-user/aws-bathroom-status-app/deploy/bathroom_config_lib.py").load_module()

#deleteme
#For local desktop testing 
bathroom_config_lib = SourceFileLoader("bathroom_config_lib", "/Users/adrian/Desktop/myhomeforcode/aws-bathroom-status-app/deploy/bathroom_config_lib.py").load_module()



################################################################################
#   References:
#       https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
#       http://docs.aws.amazon.com/lambda/latest/dg/nodejs-create-deployment-pkg.html
#       http://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
#       https://boto3.readthedocs.io/en/latest/reference/services/cloudformation.html#CloudFormation.Client.list_exports
################################################################################



################################################################################
#   Global Config Settings
################################################################################
DEBUG = True
DRY_RUN_SCRIPT_TEST = False
DEFAULT_GIT_REPO_URL = "git@github.com:drumadrian/aws-bathroom-status-app.git"
USE_AWS_S3_CONFIG_SCRIPT_TO_INITIALIZE = False
#deleteme
# LOCAL_CONFIG_FILE_PATH = "/home/ec2-user/aws-bathroom-status-app/deploy/default-config-data.json"
LOCAL_CONFIG_FILE_PATH = "/Users/adrian/Desktop/myhomeforcode/aws-bathroom-status-app/deploy/default-config-data.json"

################################################################################




################################################################################
#   ToDo:
      # Allow config script to use AWS S3 for variables
      # Add unit testing code to use the 'DEFAULT_GIT_REPO_URL' flag
      # Use AWS Lambda environment variable to reference config file when setup script 
      #     is moved from EC2 to lambda
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

    bathroom_config_lib.create_zip_file_for_get_status()
    bathroom_config_lib.create_zip_file_for_set_status()
    bathroom_config_lib.create_zip_file_for_sync_dyanomo_and_s3()
    bathroom_config_lib.create_zip_file_for_alexa_function()
    print("COMPLETED:  create_zip_files_for_lambda()")
    


def get_system_config_file(runtime_context):  
    if runtime_context == "":
        if DEBUG:
            print("Running in: EC2 Instance mode. Do not fetch file from S3!")
            local_config = bathroom_config_lib.get_local_system_config_file(LOCAL_CONFIG_FILE_PATH)
            return local_config
        else:
            print("Running in: AWS Lambda mode.  Fetch config file from S3!")
            S3_config = get_S3_system_config_file()
            return S3_config
    print("COMPLETED:  get_system_config_file()")


def get_cloudformation_outputs(context_a):

    cf_stackId = bathroom_config_lib.get_cloudformation_stackId(context_a)
    
    cf_client = boto3.client('cloudformation')
    cf_response = cf_client.list_exports()

    cf_outputs_a = ""
    for export_data in cf_response['Exports']:
        if DEBUG:
            print("\nexport_data['ExportingStackId']={}".format(export_data['ExportingStackId']))
            print("cf_stackId={}".format(cf_stackId))

        if export_data['ExportingStackId'] == cf_stackId:
            cf_outputs_a = export_data

    if DEBUG:
        print("\n\n cf_outputs_a={}".format(cf_outputs_a))
    return cf_outputs_a

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
        print("event={}".format(event))
        print("context={}".format(context))



    # clone_git_repo()                                  (ToDo)
    ##create_zip_files_for_lambda() 
    system_config = get_system_config_file(context)  
    cf_outputs = get_cloudformation_outputs(context)
    update_lambda_functions_code()
    # turn_on_versioning_for_buckets()                  (moved into CloudFormation)
    add_tags_to_assets()
    # attach_policies_to_roles()                        (moved into CloudFormation)
    update_api_from_swagger()
    setup_lambda_trigger_for_config()
    setup_dns_for_s3_website()
    setup_dns_for_api()
    deploy_api_gateway_api() 
    publish_config_data_to_system_admin()
    update_date_and_time_in_configuration()             #also put updated config file in s3





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
 






