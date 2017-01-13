
## Setup dynamodb

**In Lambda**
* Load `create_populate_dynamodb.py` into a lambda function. 
* IAM role for the lambda function must have permission to use DynamoDB.

OR

**From Local**
* Add `lambda_handler("","")` to the bottom of the `create_populate_dynamodb.py` file.
* Run `python create_populate_dynamodb.py` from the local terminal. 
* AWS Credentials on the local machine must have permission to use DynamoDB.
