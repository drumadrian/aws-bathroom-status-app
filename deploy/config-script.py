import boto3
import json  #I'm sure I'll need it at some point.  :-) 
import os
import subprocess

from importlib.machinery import SourceFileLoader
bathroom_config_lib = SourceFileLoader("bathroom_config_lib", "/home/ec2-user/aws-bathroom-status-app/deploy/bathroom_config_lib.py").load_module()

#For local desktop testing 
# bathroom_config_lib = SourceFileLoader("bathroom_config_lib", "/Users/adrian/Desktop/myhomeforcode/aws-bathroom-status-app/deploy/bathroom_config_lib.py").load_module()



################################################################################
#   References:
#       https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
#       http://docs.aws.amazon.com/lambda/latest/dg/nodejs-create-deployment-pkg.html
#       http://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
#       https://boto3.readthedocs.io/en/latest/reference/services/cloudformation.html#CloudFormation.Client.list_exports
#       http://boto3.readthedocs.io/en/latest/reference/services/lambda.html#Lambda.Client.update_function_code
################################################################################



################################################################################
#   Global Config Settings
################################################################################
DEBUG = True
DRY_RUN_SCRIPT_TEST = False
DEFAULT_GIT_REPO_URL = "git@github.com:drumadrian/aws-bathroom-status-app.git"
USE_AWS_S3_CONFIG_SCRIPT_TO_INITIALIZE = False
LOCAL_CONFIG_FILE_PATH = "/home/ec2-user/aws-bathroom-status-app/deploy/default-config-data.json"
# LOCAL_CONFIG_FILE_PATH = "/Users/adrian/Desktop/myhomeforcode/aws-bathroom-status-app/deploy/default-config-data.json"
PATH_TO_ZIP_FILE_FOLDER = "/home/ec2-user/outputs/"


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















def create_zip_files_for_lambda(system_config_a): 

    bathroom_config_lib.create_zip_file_for_get_status(PATH_TO_ZIP_FILE_FOLDER)
    bathroom_config_lib.create_zip_file_for_set_status(PATH_TO_ZIP_FILE_FOLDER)
    bathroom_config_lib.create_zip_file_for_sync_dyanomo_and_s3(PATH_TO_ZIP_FILE_FOLDER)
    bathroom_config_lib.create_zip_file_for_alexa_function(PATH_TO_ZIP_FILE_FOLDER)
    print("COMPLETED:  create_zip_files_for_lambda()")
    


def put_zip_files_in_S3_bucket(cf_outputs, context_b):
    if context_b == "":
        bucket_name = cf_outputs['cfoutputs3awsbathroomappfiles']
        # "aws s3 sync /home/ec2-user/outputs/ s3://thebathroomapp20-s3awsbathroomappfiles-1fulzqxu4j0m8"
        put_zip_files_in_S3_bucket_command = "aws s3 sync /home/ec2-user/outputs/ s3://{}".format(bucket_name)
        os.system(put_zip_files_in_S3_bucket_command)
        if DEBUG:
            print("Running in: EC2 Instance mode. Do not fetch file from S3!")
            print("\nbucket_name = {}\n".format(bucket_name))
            
    else:
        if DEBUG:
            print("Running in: AWS Lambda mode.  Fetch config file from S3!")
        print("Lambda mode:  Not yet implemented \n")

    print("COMPLETED:  s3_sync_output_files()")


def get_system_config_file(runtime_context, cf_outputs_c):  
    if runtime_context == "":
        if DEBUG:
            print("Running in: EC2 Instance mode. Do not fetch file from S3!")
        local_config = bathroom_config_lib.get_local_system_config_file(LOCAL_CONFIG_FILE_PATH)
        return local_config
    else:
        if DEBUG:
            print("Running in: AWS Lambda mode.  Fetch config file from S3!")
        S3_config = get_S3_system_config_file(cf_outputs_c)
        return S3_config


    print("COMPLETED:  get_system_config_file()")


def get_cloudformation_outputs(context_a):

    cf_stackId = bathroom_config_lib.get_cloudformation_stackId(context_a)
    
    cf_client = boto3.client('cloudformation', region_name='us-west-2')
    cf_response = cf_client.list_exports()

    cf_outputs_a = {}
    for exported_Item in cf_response['Exports']:
        if exported_Item['ExportingStackId'] == cf_stackId:
            cf_outputs_a[exported_Item['Name']] = exported_Item['Value']

        if DEBUG:
            print("\exported_Item['ExportingStackId']={}".format(exported_Item['ExportingStackId']))
            print("cf_stackId={}".format(cf_stackId))
            print("\exported_Item['Name']={}".format(exported_Item['Name']))
            print("\exported_Item['Value']={}".format(exported_Item['Value']))


    if DEBUG:
        print("\n\n cf_outputs_a={}\n\n".format(cf_outputs_a))
    return cf_outputs_a

def update_lambda_functions_code(cf_outputs_b):
    bathroom_config_lib.update_lambda_function_for_get_status(PATH_TO_ZIP_FILE_FOLDER, cf_outputs_b)
    bathroom_config_lib.update_lambda_function_for_set_status(PATH_TO_ZIP_FILE_FOLDER, cf_outputs_b)
    bathroom_config_lib.update_lambda_function_for_sync_dyanomo_and_s3(PATH_TO_ZIP_FILE_FOLDER, cf_outputs_b)
    bathroom_config_lib.update_lambda_function_for_alexa_function(PATH_TO_ZIP_FILE_FOLDER, cf_outputs_b)

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
    cf_outputs = get_cloudformation_outputs(context)

    system_config = get_system_config_file(context, cf_outputs)  

    create_zip_files_for_lambda(system_config) 
    
    put_zip_files_in_S3_bucket(cf_outputs, context)

    update_lambda_functions_code(cf_outputs)
    



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
 






