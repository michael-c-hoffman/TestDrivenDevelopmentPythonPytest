import boto3
import logging

import requests

logger = logging.getLogger(__name__)

def handler(event, context):
    response = requests.get("https://www.google.com")
    logger.info(response.text)
