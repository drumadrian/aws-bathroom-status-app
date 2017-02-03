[![Build Status](https://travis-ci.org/drumadrian/aws-bathroom-status-app.svg?branch=master)](https://travis-ci.org/drumadrian/aws-bathroom-status-app)

# AWS bathroom-status-app
Use in AWS to update the status of the restroom stalls. 



![bathroom2](https://cloud.githubusercontent.com/assets/6573380/22574528/3943d338-e964-11e6-9c07-b6841f809f70.jpg)





## Architecture


*  DynamoDB
*  Webpage
*  (later) Auth
*  IoT 
*  Lamba 
*  Static webpages in AWS S3
*  AWS API Gateway 



##Features: 
* Auto Unoccupied after 5 minutes 
* We will assume users will use the App or Webpage to mark Occupied or Vacant 
* Do not allow Occupy requests if the bathroom status is Occupied.  
* Always check Status at user interface level before requesting to Occupy/Reserve the bathroom 


## Need to develop: 
* a DynamoDB
* (2) Lambda functions
* (2) queues (no initially needed)
* (2) API Gateway endpoints 
* a Webpage on S3 
* (1) IoT Button 
* AWS Cognito for Authentication 
* an iOS App 
* an Alexa Skill 
* (1) CloudFormation Stack 










##Bathroom App Consumers (Client-side software): 

* Integrate with iOS

* Amazon Alexa

* Slack? 

* Webpage 








![bathroom1](https://cloud.githubusercontent.com/assets/6573380/22574527/3940d0ac-e964-11e6-9d74-1fe4e8da8fa5.jpg)





---
#Repository Notes:
#### <a name="fenced-code-block">Explanation of Folders and Files</a>


##Folders 

### bathroom_app
- This folder holdes the main source code for project
- **create_dynamodb**
	- The Python script used to [create the DynamoDB database](http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html "AWS Documentation") and HASH/partition key 
- **get_status**
	- This is the initial attempt to use a Javascript function in a lambda function to return the status of a status request recieved.  API Gateway will ultimately trigger this Lambda function.  
- **set_status**
	- This function is written in Python to set the status of a given stall
	- This function combines set-occupied() and set-vacant() into a single function
		- This may later find that it is better to separate these functions/activities


	

### documentation

- This folder holds original documentation for this project.  Related files, images, etc. are stored here
- Most items in the folder that constitute documention are precluded by this README page. 



