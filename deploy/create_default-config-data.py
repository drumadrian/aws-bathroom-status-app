import json

data = {

    "current_config": {
        
        "cfoutputbathroomappalexalambdafunctionarn": "arn",
        "cfoutputbathroomappgetstatuslambdafunctionarn": "get status arn",
        "cfoutputbathroomappsetstatuslambdafunctionarn": "The Bathroom App",
        "cfoutputbathroomappsyncdyanomoands3lambdafunctionarn": "The Bathroom App",
        "cfoutputsbathroomappcreatepopulatedynamodblambdafunction": "The Lambda Function arn",    
        "cfoutputBathroomAppAPIiD": "1d234",
        "APIRootUrl": "Root URL of the API gateway",
        "cfoutputadminTopicEmailListforNotificationsarn": "123",
        "cfoutputbathroomappsuperpolicyarn": "123",
        "cfoutputbathroomappsuperrolearn": "123",
        "cfoutputs3awsbathroomappfilesarn": "The Bathroom App",
        "cfoutputs3awsbathroomappwebsitebucketarn": "The Bathroom App",
        "cfoutputtablestudygurubathroomsname": "The Bathroom App",
        "cfoutputtablestudygurubathroomsconfigname": "The Bathroom App",
        "cfoutputsystemadminname": "not_yet_set",
        "cfoutputsystemadminemailaddress": "not_yet_set",
        "cfoutputalexafunctionregion": "us-east-1",
        "cfoutputrootdomain": "The Bathroom App Domain",
        "cfoutputnameofbathroomstatussystem": "The Bathroom App",
        "cfoutputs3awsbathroomappfiles": "The Bucket Name",
        "cfoutputs3awsbathroomappwebsitebucket": "The Bucket Name",
        "date_of_last_update": "not_yet_set",
        "time_of_last_update": "not_yet_set"
        
  },

  "prior_config": {

        "cfoutputbathroomappalexalambdafunctionarn": "arn",
        "cfoutputbathroomappgetstatuslambdafunctionarn": "get status arn",
        "cfoutputbathroomappsetstatuslambdafunctionarn": "The Bathroom App",
        "cfoutputbathroomappsyncdyanomoands3lambdafunctionarn": "The Bathroom App",
        "cfoutputsbathroomappcreatepopulatedynamodblambdafunction": "The Lambda Function arn",    
        "cfoutputBathroomAppAPIiD": "1d234",
        "APIRootUrl": "Root URL of the API gateway",
        "cfoutputadminTopicEmailListforNotificationsarn": "123",
        "cfoutputbathroomappsuperpolicyarn": "123",
        "cfoutputbathroomappsuperrolearn": "123",
        "cfoutputs3awsbathroomappfilesarn": "The Bathroom App",
        "cfoutputs3awsbathroomappwebsitebucketarn": "The Bathroom App",
        "cfoutputtablestudygurubathroomsname": "The Bathroom App",
        "cfoutputtablestudygurubathroomsconfigname": "The Bathroom App",
        "cfoutputsystemadminname": "not_yet_set",
        "cfoutputsystemadminemailaddress": "not_yet_set",
        "cfoutputalexafunctionregion": "us-east-1",
        "cfoutputrootdomain": "The Bathroom App Domain",
        "cfoutputnameofbathroomstatussystem": "The Bathroom App",
        "cfoutputs3awsbathroomappfiles": "The Bucket Name",
        "cfoutputs3awsbathroomappwebsitebucket": "The Bucket Name",
        "date_of_last_update": "not_yet_set",
        "time_of_last_update": "not_yet_set"

  },

  "bathrooms": [    

        {
            "stall": 1,
            "gender": 'M',
            "bstatus": 0,
            "bathroom": 1,
            "timestamp": '1245678930'
        },
        {
            "stall": 2,
            "gender": 'M',
            "bstatus": 0,
            "bathroom": 1,
            "timestamp": '1245678920'
        },
        {
            "stall": 3,
            "gender": 'M',
            "bstatus": 0,
            "bathroom": 1,
            "timestamp": '1245678910'
        },
        {
            "stall": 4,
            "gender": 'M',
            "bstatus": 0,
            "bathroom": 2,
            "timestamp": '1245678909'
        },
        {
            "stall": 5,
            "gender": 'M',
            "bstatus": 1,
            "bathroom": 2,
            "timestamp": '1245678908'
        },
        {
            "stall": 6,
            "gender": 'M',
            "bstatus": 1,
            "bathroom": 2,
            "timestamp": '1245678907'
        },
        {
            "stall": 7,
            "gender": 'F',
            "bstatus": 0,
            "bathroom": 1,
            "timestamp": '1245678906'
        },
        {
            "stall": 8,
            "gender": 'F',
            "bstatus": 1,
            "bathroom": 1,
            "timestamp": '1245678905'
        },
        {
            "stall": 9,
            "gender": 'F',
            "bstatus": 0,
            "bathroom": 1,
            "timestamp": '1245678904'
        },
        {
            "stall": 10,
            "gender": 'F',
            "bstatus": 1,
            "bathroom": 2,
            "timestamp": '1245678903'
        },
        {
            "stall": 11,
            "gender": 'F',
            "bstatus": 0,
            "bathroom": 2,
            "timestamp": '1245678902'
        },
        {
            "stall": 12,
            "gender": 'F',
            "bstatus": 1,
            "bathroom": 2,
            "timestamp": '1245678901'
        }
  
  ]
}


with open("default-config-data.json", "w") as outfile:  
    json.dump(data, outfile)
    # json.dump(data, outfile, indent=4)
