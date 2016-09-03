# DynamoDB Example

## Getting Started

* Copy and paste dynamodb.py into a lambda function
* Set the timeout to at least 30 seconds (at least on first run to give time for the DynamoDB to finish creating)
* Lambda function needs permissions to access dynamo. When creating/choosing a role use the following policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1428341300017",
            "Action": [
                "dynamodb:CreateTable",
                "dynamodb:DescribeTable",
                "dynamodb:DeleteItem",
                "dynamodb:GetItem",
                "dynamodb:PutItem",
                "dynamodb:Query",
                "dynamodb:Scan",
                "dynamodb:UpdateItem"
            ],
            "Effect": "Allow",
            "Resource": "*"
        },
        {
            "Sid": "",
            "Resource": "*",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Effect": "Allow"
        }
    ]
}
```

## Bonus:

* Add more payloads and loop to add more than one row at a time into the database.
* Get the payload from s3 file instead of in the code. (Attached is a data dump in csv from my DB.)
* Get the payload from the `events` variable in `lambda_handler`.



## Troubleshooting:

* You can see error/success outputs and print statements from a lambda function run in CloudWatch.

