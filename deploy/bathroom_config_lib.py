################################################################################
#   Config Settings
################################################################################
CONFIG_DEBUG = True
################################################################################

import subprocess
import os
import json
import urllib.request
import boto3



def create_zip_file_for_get_status(PATH_TO_ZIP_FILE_FOLDER_a):
	if CONFIG_DEBUG:
		print("STARTING:   create_zip_file_for_get_status() \n")

	zip_file_name = "get_status.zip"
	create_zip_file_for_get_status_command = "zip -r9 {}{} /home/ec2-user/aws-bathroom-status-app/get_status/*".format(PATH_TO_ZIP_FILE_FOLDER_a, zip_file_name)
	os.system(create_zip_file_for_get_status_command)


def create_zip_file_for_set_status(PATH_TO_ZIP_FILE_FOLDER_b):
	if CONFIG_DEBUG:
		print("STARTING:   create_zip_file_for_set_status() \n")

	zip_file_name = "set_status.zip"
	function_file_name = "index.py"
	zip_modules_path = 	"/home/ec2-user/environments/venvironmentforconfig/lib/python3.4/site-packages/"
	zip_code_path = "/home/ec2-user/aws-bathroom-status-app/set_status/"

	create_the_zip_file = "cd {} ; zip -r9 {}{} *".format(zip_modules_path, PATH_TO_ZIP_FILE_FOLDER_b, zip_file_name)

	add_code_to_zip_file = "cd {} ; zip -g {}{} {}".format(zip_code_path, PATH_TO_ZIP_FILE_FOLDER_b, zip_file_name, function_file_name)

	os.system(create_the_zip_file)
	os.system(add_code_to_zip_file)		

	#TODO
	# process = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE)
	# out, err = process.communicate()
	# print(out)

	if CONFIG_DEBUG:
		print("\n create_the_zip_file={}".format(create_the_zip_file))
		print("\n add_code_to_zip_file={}".format(add_code_to_zip_file))
		print("COMPLETED:   create_zip_file_for_set_status() \n")


def create_zip_file_for_sync_dyanomo_and_s3(PATH_TO_ZIP_FILE_FOLDER_c):
	zip_file_name = "sync_dyanomo_and_s3"
	if CONFIG_DEBUG:
		print("create_zip_file_for_sync_dyanomo_and_s3() Not yet implemented \n\n")




def create_zip_file_for_alexa_function(PATH_TO_ZIP_FILE_FOLDER_d):
	if CONFIG_DEBUG:
		print("STARTING:   create_zip_file_for_alexa_function() \n")

	zip_file_name = "alexa.zip"
	function_file_name = "index.py"
	create_the_zip_file = "zip -r9 {}{} /home/ec2-user/environments/venvironmentforconfig/lib/python3.4/site-packages/*".format(PATH_TO_ZIP_FILE_FOLDER_d, zip_file_name)
	add_code_to_zip_file = "zip -g {}{} /home/ec2-user/aws-bathroom-status-app/alexa/skill_service/{}".format(PATH_TO_ZIP_FILE_FOLDER_d, zip_file_name, function_file_name)

	os.system(create_the_zip_file)
	os.system(add_code_to_zip_file)		

	#TODO
	# process = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE)
	# out, err = process.communicate()
	# print(out)
	if CONFIG_DEBUG:
		print("COMPLETED:   create_zip_file_for_alexa_function() \n")



def create_zip_file_for_populate_dynamoDB_lambda_function(PATH_TO_ZIP_FILE_FOLDER_d):
	if CONFIG_DEBUG:
		print("STARTING:   create_zip_file_for_populate_dynamoDB_lambda_function() \n")

	zip_file_name = "populatedynamo.zip"
	function_file_name = "index.py"
	create_the_zip_file = "zip -r9 {}{} /home/ec2-user/environments/venvironmentforconfig/lib/python3.4/site-packages/*".format(PATH_TO_ZIP_FILE_FOLDER_d, zip_file_name)
	add_code_to_zip_file = "zip -g {}{} /home/ec2-user/aws-bathroom-status-app/create_and_populate_dynamodb/{}".format(PATH_TO_ZIP_FILE_FOLDER_d, zip_file_name, function_file_name)

	os.system(create_the_zip_file)
	os.system(add_code_to_zip_file)		

	#TODO
	# process = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE)
	# out, err = process.communicate()
	# print(out)

	if CONFIG_DEBUG:
		print("\n create_the_zip_file={}".format(create_the_zip_file))
		print("\n add_code_to_zip_file={}".format(add_code_to_zip_file))
		print("COMPLETED:   create_zip_file_for_populate_dynamoDB_lambda_function() \n")




def get_local_system_config_file(current_LOCAL_CONFIG_FILE_PATH):
	with open(current_LOCAL_CONFIG_FILE_PATH) as json_file:  
		local_config_data = json.load(json_file)

		if CONFIG_DEBUG:
			print("local_config_data is of type: {}\n\n".format(type(local_config_data)))
			for section in local_config_data:
				print("section is of type: {}\n\n".format(type(section)))
				print("\nsection in local_config_data=\n{}".format(section))
				print("local_config_data['current_config']['alexa_function_region']={}".format(local_config_data['current_config']['alexa_function_region']))
	return local_config_data




def get_S3_system_config_file(cf_outputs_d):
	print("get_S3_system_config_file() Not yet implemented \n")
	S3_config_data = "blank by design"
	return S3_config_data


def get_cloudformation_stackId(context_c):
	if context_c == "":
		instanceid = urllib.request.urlopen('http://169.254.169.254/latest/meta-data/instance-id').read().decode()
		# instanceid = "i-0e9e3c787428d0f5a"
		
		ec2_client = boto3.client('ec2', region_name='us-west-2')
		response_b = ec2_client.describe_tags(
		    Filters=[
		        {
		            'Name': 'resource-id',
		            'Values': [
		                instanceid,
		            ],
		        },
		    ],
		)
	else:
		print("Not yet implemented")

	if CONFIG_DEBUG:
		print("\n\n(describe_tags)response_b={}\n\n".format(response_b))

	for tag in response_b['Tags']:
		if tag['Key'] == "aws:cloudformation:stack-id":
			stackId_arn = tag['Value']
	# stackId_arn = "arn:aws:cloudformation:us-west-2:101845606311:stack/The-Bathroom-App-17/a0b69700-69b4-11e7-9deb-50a686fc37d2"

	if CONFIG_DEBUG:
		print("\nstackId_arn={}\n".format(stackId_arn))

	return stackId_arn


def update_lambda_function_for_get_status(PATH_TO_ZIP_FILE_FOLDER, cf_outputs_c):
	function_arn = cf_outputs_c['cfoutputbathroomappgetstatuslambdafunctionarn']
	zip_file_name = "get_status.zip"
	# path_to_zip_file = PATH_TO_ZIP_FILE_FOLDER + zip_file_name
	S3_config_bucket = cf_outputs_c['cfoutputs3awsbathroomappfiles']

	client = boto3.client('lambda', region_name='us-west-2')

	response = client.update_function_code(
    FunctionName=function_arn,
    # ZipFile=b'bytes',
    S3Bucket=S3_config_bucket,
    S3Key=zip_file_name,
    # S3ObjectVersion='string',
    # Publish=True|False,
    # DryRun=True|False
	)


	if CONFIG_DEBUG:
		print("\nfunction_arn={}".format(function_arn))
		print("\nzip_file_name={}".format(zip_file_name))
		# print("\npath_to_zip_file={}".format(path_to_zip_file))
		print("\nS3_config_bucket={}".format(S3_config_bucket))
		print("\nresponse={}".format(response))



def update_lambda_function_for_set_status(PATH_TO_ZIP_FILE_FOLDER, cf_outputs_e):
	function_arn = cf_outputs_e['cfoutputbathroomappsetstatuslambdafunctionarn']
	zip_file_name = "set_status.zip"
	# path_to_zip_file = PATH_TO_ZIP_FILE_FOLDER + zip_file_name
	S3_config_bucket = cf_outputs_e['cfoutputs3awsbathroomappfiles']

	client = boto3.client('lambda', region_name='us-west-2')

	response = client.update_function_code(
    FunctionName=function_arn,
    # ZipFile=b'bytes',
    S3Bucket=S3_config_bucket,
    S3Key=zip_file_name,
    # S3ObjectVersion='string',
    # Publish=True|False,
    # DryRun=True|False
	)


	if CONFIG_DEBUG:
		print("\nfunction_arn={}".format(function_arn))
		print("\nzip_file_name={}".format(zip_file_name))
		# print("\npath_to_zip_file={}".format(path_to_zip_file))
		print("\nS3_config_bucket={}".format(S3_config_bucket))
		print("\nresponse={}".format(response))


def update_lambda_function_for_sync_dyanomo_and_s3(PATH_TO_ZIP_FILE_FOLDER, cf_outputs_f):
	if CONFIG_DEBUG:
		print("update_lambda_function_for_sync_dyanomo_and_s3() Not yet implemented \n")


def update_lambda_function_for_alexa_function(PATH_TO_ZIP_FILE_FOLDER, cf_outputs_b):
	function_arn = cf_outputs_b['cfoutputbathroomappalexalambdafunctionarn']
	zip_file_name = "alexa.zip"
	# path_to_zip_file = PATH_TO_ZIP_FILE_FOLDER + zip_file_name
	S3_config_bucket = cf_outputs_b['cfoutputs3awsbathroomappfiles']

	client = boto3.client('lambda', region_name='us-west-2')

	response = client.update_function_code(
    FunctionName=function_arn,
    # ZipFile=b'bytes',
    S3Bucket=S3_config_bucket,
    S3Key=zip_file_name,
    # S3ObjectVersion='string',
    # Publish=True|False,
    # DryRun=True|False
	)


	if CONFIG_DEBUG:
		print("\nfunction_arn={}".format(function_arn))
		print("\nzip_file_name={}".format(zip_file_name))
		# print("\npath_to_zip_file={}".format(path_to_zip_file))
		print("\nS3_config_bucket={}".format(S3_config_bucket))
		print("\nresponse={}".format(response))



def update_lambda_function_for_populate_dynamoDB_lambda_function(PATH_TO_ZIP_FILE_FOLDER, cf_outputs_f):
	if CONFIG_DEBUG:
		print("STARTING:   update_lambda_function_for_populate_dynamoDB_lambda_function() \n")

	function_arn = cf_outputs_f['cfoutputsbathroomappcreatepopulatedynamodblambdafunction']
	zip_file_name = "populatedynamo.zip"
	# path_to_zip_file = PATH_TO_ZIP_FILE_FOLDER + zip_file_name
	S3_config_bucket = cf_outputs_f['cfoutputs3awsbathroomappfiles']

	client = boto3.client('lambda', region_name='us-west-2')

	response = client.update_function_code(
    FunctionName=function_arn,
    # ZipFile=b'bytes',
    S3Bucket=S3_config_bucket,
    S3Key=zip_file_name,
    # S3ObjectVersion='string',
    # Publish=True|False,
    # DryRun=True|False
	)


	if CONFIG_DEBUG:
		print("\nfunction_arn={}".format(function_arn))
		print("\nzip_file_name={}".format(zip_file_name))
		# print("\npath_to_zip_file={}".format(path_to_zip_file))
		print("\nS3_config_bucket={}".format(S3_config_bucket))
		print("\nresponse={}".format(response))


	#Now, we need to update the environment data with the correct dynamoDB table name
	dynamodbTableName = cf_outputs_f['cfoutputtablestudygurubathroomsname']

	response = client.update_function_configuration(
	    FunctionName=function_arn,
	    # Role='string',
	    # Handler='string',
	    # Description='string',
	    # Timeout=123,
	    # MemorySize=123,
	    # VpcConfig={
	    #     'SubnetIds': [
	    #         'string',
	    #     ],
	    #     'SecurityGroupIds': [
	    #         'string',
	    #     ]
	    # },
	    Environment={
	        'Variables': {
	            'dynamodb_table_name': dynamodbTableName
	        }
	    }
	    # Runtime='nodejs'|'nodejs4.3'|'nodejs6.10'|'java8'|'python2.7'|'python3.6'|'dotnetcore1.0'|'nodejs4.3-edge',
	    # DeadLetterConfig={
	    #     'TargetArn': 'string'
	    # },
	    # KMSKeyArn='string',
	    # TracingConfig={
	    #     'Mode': 'Active'|'PassThrough'
	    # }
	)

	if CONFIG_DEBUG:
		print("\nfunction_arn={}".format(function_arn))
		print("\ndynamodbTableName={}".format(dynamodbTableName))
		print("\nresponse={}".format(response))
		print("COMPLETED:   update_lambda_function_for_populate_dynamoDB_lambda_function() \n")




