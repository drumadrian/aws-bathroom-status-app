import json

data = {

    "current_config": {
        
        "alexa_lambda_function_arn": "The Bathroom App for Home",
        "get_status_lambda_function_arn": "The Bathroom App",
        "set_status_lambda_function_arn": "The Bathroom App",
        "sync_dyanomo_and_s3_lambda_function_arn": "The Bathroom App",
        "BathroomAppAPI": "1d234",
        "API_RootUrl": "Root URL of the API gateway",
        "adminTopicEmailListforNotifications_arn": "123",
        "bathroomappsuperpolicy_arn": "123",
        "bathroomappsuperrole_arn": "123",
        "s3awsbathroomappfiles_arn": "The Bathroom App",
        "s3awsbathroomappwebsitebucket_arn": "The Bathroom App",
        "tablestudygurubathrooms_name": "The Bathroom App",
        "tablestudygurubathroomsconfig_name": "The Bathroom App",
        "system_admin_name": "not_yet_set",
        "system_admin_email_address": "not_yet_set",
        "alexa_function_region": "us-east-1",
        "root_domain": "The Bathroom App Domain",
        "name_of_bathroom_status_system": "The Bathroom App",
        "aws_s3_bucket_name": "The Bathroom App",
        "aws_s3_bucket_name_for_website": "The Bathroom App",
        "date_of_last_update": "not_yet_set",
        "time_of_last_update": "not_yet_set"
        
  },

  "prior_config": {

        "alexa_function_region": "us-east-1",
        "alexa_lambda_function_arn": "The Bathroom App for Home",
        "get_status_lambda_function_arn": "The Bathroom App",
        "set_status_lambda_function_arn": "The Bathroom App",
        "sync_dyanomo_and_s3_lambda_function_arn": "The Bathroom App",
        "BathroomAppAPI": "1d234",
        "root_domain": "The Bathroom App Domain",
        "API_RootUrl": "Root URL of the API gateway",
        "adminTopicEmailListforNotifications_arn": "123",
        "bathroomappsuperpolicy_arn": "123",
        "bathroomappsuperpolicy_arn": "123",
        "name_of_bathroom_status_system": "The Bathroom App",
        "sns_topic_arn_for_admin": "The Bathroom App",
        "aws_s3_bucket_name": "The Bathroom App",
        "aws_s3_bucket_name_for_website": "The Bathroom App",
        "tablestudygurubathrooms_name": "The Bathroom App",
        "tablestudygurubathroomsconfig_name": "The Bathroom App",
        "system_admin_name": "not_yet_set",
        "system_admin_email_address": "not_yet_set",
        "date_of_last_update": "not_yet_set",
        "time_of_last_update": "not_yet_set"

  },

  "bathrooms": [    

      {
        "gender" : "M",
        "building": "",
        "name":"",
        "stalls":[
          {
            "stall_id":"not_set"
          },
          {
            "stall_id":"not_set"
          }
        ]
      },
      {
        "gender" : "F",
        "building": "",
        "name":"",
        "stalls":[
          {
            "stall_id":"not_set"
          },
          {
            "stall_id":"not_set"
          }
        ]
      }
  
  ]
}


with open("default-config-data.json", "w") as outfile:  
    json.dump(data, outfile)
    # json.dump(data, outfile, indent=4)
