[![Build Status](https://travis-ci.org/drumadrian/aws-bathroom-status-app.svg?branch=master)](https://travis-ci.org/drumadrian/aws-bathroom-status-app)

# AWS bathroom-status-app
Use in AWS to update the status of the restroom stalls. 






# Architecture


Architecture: 
*  DynamoDB
*  Webpage
*  (later) Auth
*  IoT 
*  Lamba 
*  Static webpages in AWS S3
*  AWS API Gateway 



Feature: 
* Auto Unoccupied after 5 minutes 
* We will assume users will use the App or Webpage to mark Occupied or Vacant 
* Do not allow Occupy requests if the bathroom status is Occupied.  
* Always check Status at user interface level before requesting to Occupy/Reserve the bathroom 


Need: 
* a DynamoDB
* (2) Lambda functions
* (2) queues 
* (2) API Gateway endpoints 
* a Webpage on S3 
* (1) IoT Button 
* AWS Cognito for Authentication 
* an iOS App 
* an Alexa Skill 
* (1) CloudFormation Stack 










Bathroom App: 

Integrate with iOS
Amazon Alexa
Slack? 
Webpage 


