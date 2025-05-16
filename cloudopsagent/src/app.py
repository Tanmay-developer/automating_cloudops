import json
from agent import getmyagent

def lambda_handler(event, context):
    print(f"Received event: {event}")

    # Parse the form-encoded data from Twilio
    body = event.get('query')

    response_message = getmyagent(body) 
    
    return {
        "response": response_message 
    }