import boto3
import json  #I'm sure I'll need it at some point.  :-) 
import os
import subprocess
import datetime

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
#       http://boto3.readthedocs.io/en/latest/reference/services/apigateway.html#APIGateway.Client.put_rest_api
#       https://stackoverflow.com/questions/17053099/how-to-print-current-date-on-python3
################################################################################



################################################################################
#   Global Config Settings
################################################################################
DEBUG = True
DRY_RUN_SCRIPT_TEST = False
DEFAULT_GIT_REPO_URL = "git@github.com:drumadrian/aws-bathroom-status-app.git"
USE_AWS_S3_CONFIG_SCRIPT_TO_INITIALIZE = False
LOCAL_CONFIG_FILE_PATH = "/home/ec2-user/aws-bathroom-status-app/deploy/default-config-data.json"
LOCAL_SWAGGER_FILE_PATH_FILE_PATH = "/home/ec2-user/aws-bathroom-status-app/swagger/swagger.json"
PATH_TO_ZIP_FILE_FOLDER = "/home/ec2-user/outputs/"
DEFAULT_REGION = "us-west-2"

# deleteme
# LOCAL_CONFIG_FILE_PATH = "/Users/adrian/Desktop/myhomeforcode/aws-bathroom-status-app/deploy/default-config-data.json"


################################################################################




################################################################################
#   ToDo:
      # Allow config script to use AWS S3 for variables
      # Add unit testing code to use the 'DEFAULT_GIT_REPO_URL' flag
      # Use AWS Lambda environment variable to reference config file when setup script 
      #     is moved from EC2 to lambda
################################################################################




################################################################################
#   Initial Outline
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
    bathroom_config_lib.create_zip_file_for_populate_dynamoDB_lambda_function(PATH_TO_ZIP_FILE_FOLDER)
    print("COMPLETED:  create_zip_files_for_lambda()")
    


def put_zip_files_in_S3_bucket(cf_outputs, context_b):
    if context_b == "":
        bucket_name = cf_outputs['cfoutputs3awsbathroomappfiles']
        # "aws s3 sync /home/ec2-user/outputs/ s3://thebathroomapp20-s3awsbathroomappfiles-1fulzqxu4j0m8"
        put_zip_files_in_S3_bucket_command = "aws s3 sync {} s3://{}".format(PATH_TO_ZIP_FILE_FOLDER, bucket_name)
        os.system(put_zip_files_in_S3_bucket_command)
        if DEBUG:
            print("Running in: EC2 Instance mode. Do not fetch file from S3!")
            print("\nbucket_name = {}\n".format(bucket_name))
            print("\nput_zip_files_in_S3_bucket_command = {}\n".format(put_zip_files_in_S3_bucket_command))
            
    else:
        if DEBUG:
            print("Running in: AWS Lambda mode.  Fetch config file from S3!")
        print("Lambda mode:  Not yet implemented \n")

    print("COMPLETED:  put_zip_files_in_S3_bucket()")


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
    bathroom_config_lib.update_lambda_function_for_populate_dynamoDB_lambda_function(PATH_TO_ZIP_FILE_FOLDER, cf_outputs_b)

    print("COMPLETED:  update_lambda_functions_code()")


def invoke_populate_dynamoDB_lambda_function(context_d, cf_outputs_d, system_config_d):
    function_arn = cf_outputs_d['cfoutputsbathroomappcreatepopulatedynamodblambdafunction']
    lambda_client = boto3.client('lambda', region_name='us-west-2')

    response = lambda_client.invoke(
        FunctionName=function_arn,
        InvocationType='RequestResponse',
        LogType='None',
        # ClientContext='string',
        Payload=system_config_d
        # Qualifier='string'
    )

    if DEBUG:
        print("\n\n function_arn={}\n\n".format(function_arn))


    print("COMPLETED:  invoke_populate_dynamoDB_lambda_function()")




def add_tags_to_assets():
    print("\n Not yet implemented \n")
    print("COMPLETED:  add_tags_to_assets()")


def update_api_from_swagger(context_e, cf_outputs_e):

    system_restApiId = cf_outputs_e['cfoutputBathroomAppAPIiD']

    with open(LOCAL_SWAGGER_FILE_PATH_FILE_PATH) as local_swagger_file:
        local_swagger_file_json = json.load(local_swagger_file)
        local_swagger_file_string = json.dumps(local_swagger_file_json)
        local_swagger_file_byte_data = bytes(local_swagger_file_string, "utf-8")
        api_gateway_client = boto3.client('apigateway', region_name='us-west-2')

        response = api_gateway_client.put_rest_api(
            restApiId=system_restApiId,
            # mode='merge'|'overwrite',
            mode='overwrite',
            failOnWarnings=False,
            # parameters={
            #     'string': 'string'
            # },
            # body=b'bytes'|file
            body=local_swagger_file_byte_data
        )

    if DEBUG:
        print("\n LOCAL_SWAGGER_FILE_PATH_FILE_PATH={}".format(LOCAL_SWAGGER_FILE_PATH_FILE_PATH))
        print("\n system_restApiId={}".format(system_restApiId))
        print("\n response={}".format(response))
    
    print("COMPLETED:  update_api_from_swagger()")





def update_api_lambda_integrations(context_e, cf_outputs_e):
    system_restApiId_b = cf_outputs_e['cfoutputBathroomAppAPIiD']


    update_get_status_api_gateway_integration(context_e, cf_outputs_e, system_restApiId_b)

    update_set_status_api_gateway_integration(context_e, cf_outputs_e, system_restApiId_b)
    
    print("COMPLETED:  update_api_lambda_integrations()")



def save_config_data_to_database(context_k, cf_outputs_k, system_config_k, region_k):    
    # create list of the keys in the system_config_k
    # if the key in cf_outputs_k in contained in the list of keys in system_config_k
        # then, add the value for the key in cf_outputs_k which exists in the list

    # system_config_k_key_list = []
    # for k, v in system_config_k:
    #     system_config_k_key_list.append(k)

    # for k1, v2 in cf_outputs_k:
    #     if k1 in system_config_k_key_list:
    #         system_config_k[k1] = cf_outputs_k[k1]
    #     else:
    #         system_config_k[k1] = cf_outputs_k[k1]

    for key, value in cf_outputs_k:
        system_config_k[key] = cf_outputs_k[key]

    table_name = cf_outputs_k['cfoutputtablestudygurubathroomsconfigname']
    current_config_string = json.dumps(system_config_k)
    now = datetime.datetime.now()
    now_string = str(now)
    date_time_list = now_string.split()
    date_of_put_item = date_time_list[0]
    time_of_put_item = date_time_list[1]

    dynamodb = boto3.resource('dynamodb', region_name=region_k)
    table = dynamodb.Table(table_name)

    try:
        # add the data to the dynamodb
        response = table.put_item(
            Item={
                'current_config': current_config_string,
                'date': date_of_put_item,
                'time': time_of_put_item
            }

        )
        # print response
        print("Added {0} \n at date {1} \n at time {2} \n to DynamoDB".format(current_config_string, date_of_put_item, time_of_put_item) )

    except Exception as err:
        print("Error occurred while adding data to the new DynamoDB table in save_config_data_to_database()")
        print("Error occurred:", err)
        sys.exit()


    if DEBUG:
        print("\n cf_outputs_k={}".format(cf_outputs_k))
        print("\n table_name={}".format(table_name))
        print("\n current_config_string={}".format(current_config_string))
        print("\n now_string={}".format(now_string))
        print("\n date_time_list={}".format(date_time_list))
        print("\n date_of_put_item={}".format(date_of_put_item))
        print("\n time_of_put_item={}".format(time_of_put_item))
        print("\n LOCAL_SWAGGER_FILE_PATH_FILE_PATH={}".format(LOCAL_SWAGGER_FILE_PATH_FILE_PATH))
        print("\n LOCAL_SWAGGER_FILE_PATH_FILE_PATH={}".format(LOCAL_SWAGGER_FILE_PATH_FILE_PATH))

    print("COMPLETED:  setup_lambda_trigger_for_config()")



def setup_lambda_trigger_for_config(context_j, cf_outputs_j):

    aws_s3_client = boto3.client('s3', region_name='us-west-2')

    #add trigger on config s3 bucket 

    print("\n Not yet implemented \n")
    print("COMPLETED:  setup_lambda_trigger_for_config()")


def update_date_and_time_in_configuration():
    print("\n Not yet implemented \n")
    print("COMPLETED:  update_date_and_time_in_configuration()")


def setup_dns_for_s3_website():
    print("\n Not yet implemented \n")
    print("COMPLETED:  setup_dns_for_s3_website()")


def setup_dns_for_api():
    print("\n Not yet implemented \n")
    print("COMPLETED:  setup_dns_for_api()")


def deploy_api_gateway_api():
    print("\n Not yet implemented \n")
    print("COMPLETED:  deploy_api_gateway_api()")


def publish_config_data_to_system_admin():
    print("\n Not yet implemented \n")
    print("COMPLETED:  publish_config_data_to_system_admin()")








def lambda_handler(event, context):

    if DEBUG:
        print("event={}".format(event))
        print("context={}".format(context))


    region = DEFAULT_REGION

    # clone_git_repo()                                  (ToDo)
    cf_outputs = get_cloudformation_outputs(context)

    system_config = get_system_config_file(context, cf_outputs)  

    create_zip_files_for_lambda(system_config) 
    
    put_zip_files_in_S3_bucket(cf_outputs, context)

    #deleteme
    #next  use this for testing during development when there the function was not yet in the cloudformation stack
    # cf_outputs['cfoutputtablestudygurubathroomsname'] = "TheBathroomApp22-tablestudygurubathrooms-KCZPH9OJ95X5"  
    # cf_outputs['cfoutputsbathroomappcreatepopulatedynamodblambdafunction'] = "arn:aws:lambda:us-west-2:101845606311:function:TESTbathroomappcreatepopulatedynamodblambdafunction"   

    update_lambda_functions_code(cf_outputs)

    invoke_populate_dynamoDB_lambda_function(context, cf_outputs, system_config)

    update_api_from_swagger(context, cf_outputs, system_config)

    #Todo deleteme if update_api_lambda_integrations() works
    # setting up API with proper Lambda Integration will be done manually for now.  
    # After authentication is added this will be captured into update_api_from_swagger()
    # This allows a full deployment and auto configuration 
    update_api_lambda_integrations(context, cf_outputs)
    save_config_data_to_database(context, cf_outputs, system_config, region)

    add_tags_to_assets()                              
    setup_lambda_trigger_for_config(context, cf_outputs)
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
 






