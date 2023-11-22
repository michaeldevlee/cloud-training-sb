import sys
import logging
import pymysql
import json
import os
import boto3
from datetime import datetime, timedelta
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS SDK clients
s3_client = boto3.client('s3')
logs = boto3.client('logs')


logger.info("SUCCESS: Connection to RDS for MySQL instance succeeded")

def lambda_handler(event, context):
    query = "fields @timestamp, @message, @logStream, @log"
    log_group = "/aws/lambda/export-to-s3-from-log-group"

    start_query_response = logs.start_query(
    logGroupName=log_group,
    startTime=int((datetime.today() - timedelta(hours=1)).timestamp()),
    endTime=int(datetime.now().timestamp()),
    queryString=query,
    limit=2
    )
    
    query_id = start_query_response['queryId']
    
    results = logs.get_query_results(
    queryId=query_id
)
    
    return results

    