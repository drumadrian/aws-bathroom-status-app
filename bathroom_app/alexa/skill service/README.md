


![simple](https://cloud.githubusercontent.com/assets/6573380/23096609/d7fcb040-f5d4-11e6-8149-fbdf0bcdb0be.png)



##Purpose
* This source code for the skill service should call the normal AWS Lambda function and reuse the existing code/logic.  

* This code should also gather matrics for usage of the Alexa skill and send out relevant AWS SNS Notifications

##Language

* This AWS Lambda function is written in Python
* Javascript my be considered in the future if it is much more beneficial

##Metrics/Analytics
* This function should use it's own DynamoDB table or Redshift table for storing usage data.



![simple2](https://cloud.githubusercontent.com/assets/6573380/23096608/d5fb9b08-f5d4-11e6-850a-a74aae78f957.png)
