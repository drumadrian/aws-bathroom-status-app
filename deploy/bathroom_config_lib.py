################################################################################
#   Config Settings
################################################################################
CONFIG_DEBUG = True
################################################################################

import subprocess
import os


def create_zip_file_for_get_status():
	print("This baby is fat \n")

def create_zip_file_for_set_status():
	if CONFIG_DEBUG:
		print("STARTING:   create_zip_file_for_set_status() \n")

		create_the_zip_file = "zip -r9 /home/ec2-user/set_status.zip /home/ec2-user/environments/venvironmentforconfig/lib/python3.4/site-packages/*"
		add_code_to_zip_file = "zip -g /home/ec2-user/set_status.zip /home/ec2-user/aws-bathroom-status-app/set_status/set_status.py"

		os.system(create_the_zip_file)
		os.system(add_code_to_zip_file)		

		#TODO
		# process = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE)
		# out, err = process.communicate()
		# print(out)

	if CONFIG_DEBUG:
		print("COMPLETED:   create_zip_file_for_set_status() \n")

def create_zip_file_for_sync_dyanomo_and_s3():
	print("This baby is sync \n")


def create_zip_file_for_alexa_function():
	print("This baby is alexa \n")
