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


def create_zip_file_for_get_status():
	if CONFIG_DEBUG:
		print("This baby is fat \n")

	create_zip_file_for_get_status = "zip -r9 /home/ec2-user/outputs/get_status.zip /home/ec2-user/aws-bathroom-status-app/get_status/*"
	os.system(create_zip_file_for_get_status)


def create_zip_file_for_set_status():
	if CONFIG_DEBUG:
		print("STARTING:   create_zip_file_for_set_status() \n")

		create_the_zip_file = "zip -r9 /home/ec2-user/outputs/set_status.zip /home/ec2-user/environments/venvironmentforconfig/lib/python3.4/site-packages/*"
		add_code_to_zip_file = "zip -g /home/ec2-user/outputs/set_status.zip /home/ec2-user/aws-bathroom-status-app/set_status/set_status.py"

		os.system(create_the_zip_file)
		os.system(add_code_to_zip_file)		

		#TODO
		# process = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE)
		# out, err = process.communicate()
		# print(out)

	if CONFIG_DEBUG:
		print("COMPLETED:   create_zip_file_for_set_status() \n")

def create_zip_file_for_sync_dyanomo_and_s3():
	if CONFIG_DEBUG:
		print("This baby is sync \n")


def create_zip_file_for_alexa_function():
	if CONFIG_DEBUG:
		print("This baby is alexa \n")


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




def get_S3_system_config_file():
	return S3_config_data

def get_cloudformation_stackId(context_c):
	if context_c == "":
		instanceid = urllib.request.urlopen('http://169.254.169.254/latest/meta-data/instance-id').read().decode()
		# instanceid = "i-0e9e3c787428d0f5a"
		
		ec2_client = boto3.client('ec2')
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

	print(response_b)
	for tag in response_b['Tags']:
		if tag['Key'] == "aws:cloudformation:stack-id":
			stackId_arn = tag['Value']
	# stackId_arn = "arn:aws:cloudformation:us-west-2:101845606311:stack/The-Bathroom-App-17/a0b69700-69b4-11e7-9deb-50a686fc37d2"

	if CONFIG_DEBUG:
		print("\stackId_arn={}\n".format(stackId_arn))

	return stackId_arn





