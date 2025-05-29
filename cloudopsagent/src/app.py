import json
from tools import getmyagent
import urllib.parse
import logging
from twilio.rest import Client
from utils import get_secret

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"Received event: {event}")

    body = event.get('body')

    params = urllib.parse.parse_qs(body) if body else {}
    message_body = params.get('Body', [''])[0]

    if not message_body:
        logger.error("No message body received.")
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "No message body provided"})
        }

    logger.info(f"Message body extracted: {message_body}")
    response_message = getmyagent(message_body)

    logger.info(f"Response message from LLM: {response_message}")

    account_sid = get_secret("TWILIO_ACCOUNT_SID")
    auth_token = get_secret("TWILIO_AUTH_TOKEN")
    whatsapp_no = get_secret("MY_WHATSAPP_ID")

    client = Client(account_sid, auth_token)

    try: 
        message = client.messages.create(
            body=response_message,
            from_="whatsapp:+14155238886",
            to=f"whatsapp:{whatsapp_no}",
        )
        logger.info(f"Message sent: SID {message.sid}")
    except Exception as e:
        logger.error(f"Failed to send message: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Failed to send message"})
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Message sent successfully."})
    }