import json

data = {

    "current_config": {
        
        "alexa_function_region": "us-east-1",
        "alexa_lambda_function_arn": "The Bathroom App for Home",
        "get_status_lambda_function_arn": "The Bathroom App",
        "set_status_lambda_function_arn": "The Bathroom App",
        "sync_dyanomo_and_s3_lambda_function_arn": "The Bathroom App",
        "name_of_bathroom_status_system": "The Bathroom App",
        "sns_topic_arn_for_admin": "The Bathroom App",
        "aws_s3_bucket_name": "The Bathroom App",
        "aws_s3_bucket_name_for_website": "The Bathroom App",
        "root_domain": "The Bathroom App",
        "api_url": "The Bathroom App",
        "database_table_name": "The Bathroom App",
        "dynamo_db_database_arn": "not_yet_set",
        "system_admin_name": "not_yet_set",
        "system_admin_email_address": "not_yet_set",
        "date_of_last_update": "not_yet_set",
        "time_of_last_update": "not_yet_set"
        
  },


  "prior_config": {

        "alexa_function_region": "us-east-1",
        "alexa_lambda_function_arn": "The Bathroom App for Home",
        "get_status_lambda_function_arn": "The Bathroom App",
        "set_status_lambda_function_arn": "The Bathroom App",
        "sync_dyanomo_and_s3_lambda_function_arn": "The Bathroom App",
        "name_of_bathroom_status_system": "The Bathroom App",
        "sns_topic_arn_for_admin": "The Bathroom App",
        "aws_s3_bucket_name": "The Bathroom App",
        "aws_s3_bucket_name_for_website": "The Bathroom App",
        "root_domain": "The Bathroom App",
        "api_url": "The Bathroom App",
        "database_table_name": "The Bathroom App",
        "dynamo_db_database_arn": "not_yet_set",
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
