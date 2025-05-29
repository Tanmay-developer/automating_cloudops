import boto3
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_secret(SecName):
    logger.info("Retre")
    client = boto3.client("secretsmanager")
    try:
        response = client.get_secret_value(SecretId=SecName)
        result = json.loads(response['SecretString'])
        return result
    except Exception as e:
        logger.raise(f"Error fetching secret: {e}")
        return None