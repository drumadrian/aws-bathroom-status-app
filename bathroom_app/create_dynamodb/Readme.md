

## Setup dynamodb

Two ways:
* Load `create_populate_dynamodb.py` into a lambda function. 
* IAM role for the lambda function must have permission to use DynamoDB.

OR

* Add `lambda_handler("","")` to the bottom of the `create_populate_dynamodb.py` file.
* Run `python create_populate_dynamodb.py`. 
* AWS Credentials on the local machine must have permission to use DynamoDB.
