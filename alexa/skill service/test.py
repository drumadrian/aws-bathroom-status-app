from boto3 import client as boto3_client
import json

lambda_client = boto3_client('lambda', region_name='us-west-2')

# def lambda_handler(event, context):
# msg = {"key":"new_invocation", "at": datetime.now()}
message = {"unique_id": "F102"}

print 'message={}'.format(message)

invocation_response = lambda_client.invoke(FunctionName="test-get-status",
                                       InvocationType='RequestResponse',
                                       Payload=json.dumps(message))



invocation_response_string = invocation_response['Payload'].read()

json_acceptable_string = invocation_response_string.replace("'", "\"")
invocation_response_dictionary = json.loads(json_acceptable_string)



print ""
print "formatted and printed invocation response={}".format(invocation_response_dictionary) 

print "" 
print ""
print ""

answer = invocation_response_dictionary['Item']['bstatus']

print "The answer is {}".format(answer)

# print(invocation_response['Item']['bstatus'])

# Sample Response
# {
#     "Item": {
#         "stall": 10,
#         "bathroom": 2,
#         "bstatus": "0",
#         "unique_id": "F102",
#         "gender": "F",
#         "timestamp": "1245678903"
#     }
# }







print "" 
print ""
print ""

blank = " "

favorite_stall = 'F102'

favorite_stall_speech_output = blank + "I now know your favorite stall is " + favorite_stall + ""

print favorite_stall_speech_output