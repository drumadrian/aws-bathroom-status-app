"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
from boto3 import client as boto3_client
import json


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Alexa Bathroom App. " \
                    "Please request an action by saying, " \
                    "Reserve a stall, or" \
                    "Vacate a stall, or" \
                    "What is the status of my stall"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please request an action by saying, " \
                    "Reserve a stall, or" \
                    "Vacate a stall, or" \
                    "What is the status of my stall"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Bathroom App. " \
                    "Have a nice day," \
                    "and don't forget, " \
                    "If you sprinkle when you tinkle, " \
                    "Be a sweetie and wipe the seatie"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_favorite_stall_attributes(favorite_stall):
    print("Favorite Stall has been set to: {}").format(favorite_stall)
    return {"favoriteStall": favorite_stall}


# --------------- START Intent hander functions ------------------

def GetStallStatus_Intent_Function(intent, session):
    """ Gets the status of a stall or stalls for a user.
    """

    # card_title = intent['name']
    card_title = 'Get Status of a Bathroom Stall'
    session_attributes = {}
    should_end_session = False

    if session.get('attributes', {}) and "favoriteStall" in session.get('attributes', {}):
        favorite_stall = session['attributes']['favoriteStall']
    else:
        favorite_stall = None

    # if 'Color' in intent['slots']:
    #     favorite_color = intent['slots']['Color']['value']
    #     session_attributes = create_favorite_color_attributes(favorite_color)
    #     speech_output = "I now know your favorite color is " + \
    #                     favorite_color + \
    #                     ". You can ask me your favorite color by saying, " \
    #                     "what's my favorite color?"
    #     reprompt_text = "You can ask me your favorite color by saying, " \
    #                     "what's my favorite color?"
    # else:
    #     speech_output = "I'm not sure what your favorite color is. " \
    #                     "Please try again."
    #     reprompt_text = "I'm not sure what your favorite color is. " \
    #                     "You can tell me your favorite color by saying, " \
    #                     "my favorite color is red."

    # Call the Primary back-end Lambda function to Get Status based on user's request
    lambda_client = boto3_client('lambda', region_name='us-west-2')    

    #Todo update to accept the requested stall to check.  Default to unique id F102 for now
    message = {"unique_id": "F102"}

    invocation_response = lambda_client.invoke(FunctionName="test-get-status",
                                           InvocationType='RequestResponse',
                                           Payload=json.dumps(message))

    invocation_response_string = invocation_response['Payload'].read()
    json_acceptable_string = invocation_response_string.replace("'", "\"")
    
    invocation_response_dictionary = json.loads(json_acceptable_string)

    print('')
    print("formatted and printed invocation response={}".format(invocation_response_dictionary) )

    answer = invocation_response_dictionary['Item']['bstatus']

    if answer == '0': 
        print("Stall is available")
        stallAvailability = True
    elif answer == '1':
        stallAvailability = False
        print("Stall is NOT available")
    else:
        raise ValueError("Invalid status from test-get-status")


    # Interpret response from Primary Lambda function
    favorite_stall_speech_output=""

    # Based on the result of the reponse from the Primary Lamnda function, build Alexa's response
    if stallAvailability:
        #ToDo:  Include a check to see if the favorite stall if a valid stall
        speech_output = "Good news, the requested stall is available," + \
                        "Would you like to reserve the stall"
        # reprompt_text = "would you like to reserve the stall?"
        reprompt_text = "Would you like to reserve the stall"
        should_end_session = False
    
    else:
        speech_output = "I'm sorry your stall isn't availble" \
                        "Please try again later" \
                        "In the future, " \
                        "we will be able to notify you when your stall is no longer occupied and is avaiable"
        reprompt_text = None
        should_end_session = True
        
    return build_response(session_attributes, build_speechlet_response(
    card_title, speech_output, reprompt_text, should_end_session))




def SetStatusToOccupied_Intent_Function(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "favoriteStall" in session.get('attributes', {}):
        favorite_stall = session['attributes']['favoriteStall']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "You can say, my favorite color is red."
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


def SetStatusToVacant_Intent_Function(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "You can say, my favorite color is red."
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


# --------------- END Intent hander functions ------------------


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started: requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch: requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent: requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "GetStallStatus":
        return GetStallStatus_Intent_Function(intent, session)

    elif intent_name == "SetStatusToOccupied":
        return SetStatusToOccupied_Intent_Function(intent, session)

    elif intent_name == "SetStatusToVacant":
        return SetStatusToVacant_Intent_Function(intent, session)

    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()

    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()

    else:
        raise ValueError("Invalid intent")


##INTENT SCHEMA SAMPLE
# {
#   "intents": [
#     {
#       "intent": "GetStallStatus",
#       "slots": [
#       {
#         "name" : "Stall",
#         "type": "LIST_OF_NAMES_FOR_A_STALL"
#       }
#      ]
#     },
#     {
#       "intent": "SetStatusToOccupied",
#       "slots": [
#       {
#         "name" : "Stall",
#         "type": "LIST_OF_NAMES_FOR_A_STALL"
#       }
#      ]
#     },
#     {
#       "intent": "SetStatusToVacant",
#       "slots": [
#       {
#         "name" : "Stall",
#         "type": "LIST_OF_NAMES_FOR_A_STALL"
#       }
#      ]
#     },
#     {
#       "intent": "AMAZON.HelpIntent"
#     },
#     {
#       "intent": "AMAZON.StopIntent"
#     },
#     {
#       "intent": "AMAZON.CancelIntent"
#     }
#   ]
#  }





def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    if (event['session']['application']['applicationId'] !=
            "amzn1.ask.skill.104905e9-d5ab-4fbc-8529-1191b993ce66"):
        raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])








