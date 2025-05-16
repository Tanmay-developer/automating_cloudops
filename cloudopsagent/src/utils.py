import boto3
import json


def get_secret(SecName):
    """
    Fetches the WhatsApp API token from AWS Secrets Manager.
    """
    client = boto3.client("secretsmanager")
    
    try:
        response = client.get_secret_value(SecretId=SecName)
        result = json.loads(response['SecretString'])
        return result
    except Exception as e:
        print(f"Error fetching secret: {e}")
        return None