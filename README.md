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

[![Watch the video](https://user-images.githubusercontent.com/6573380/28448417-adab9ca4-6d8c-11e7-935a-e4ad29e08ee3.png)](https://cloudcraft.co/view/beef112e-7eec-4480-bc4c-11c56041f189?key=BuYN0O-c-5sQ6ajRyJgFhw)



##Features: 
* Auto Unoccupied after 5 minutes 
* We will assume users will use the App or Webpage to mark Occupied or Vacant 
* Do not allow Occupy requests if the bathroom status is Occupied.  
* Always check Status at user interface level before requesting to Occupy/Reserve the bathroom 


## Need to develop: 
 Please see Issues page

[Issues](https://github.com/drumadrian/aws-bathroom-status-app/issues/12)






##Bathroom App Consumers (Client-side software): 

* Integrate with iOS

* Amazon Alexa

* Slack? 

* Webpage 








![bathroom1](https://cloud.githubusercontent.com/assets/6573380/22574527/3940d0ac-e964-11e6-9d74-1fe4e8da8fa5.jpg)




