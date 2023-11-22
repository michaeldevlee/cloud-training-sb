import sys
import logging
import pymysql
import json
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# rds settings
user_name = os.environ['USER_NAME']
password = os.environ['PASSWORD']
rds_proxy_host = os.environ['RDS_PROXY_HOST']
db_name = os.environ['DB_NAME']

# Initialize AWS SDK clients
s3_client = boto3.client('s3')
logs = boto3.client('logs')

export_to_time = 1
export_from_time = 2

log_group_fields_response = logs.describe_log_groups(
    logGroupNamePattern='/aws/lambda/query-every-hour'
)


# create the database connection outside of the handler to allow connections to be
# re-used by subsequent function invocations.
try:
        conn = pymysql.connect(host=rds_proxy_host, user=user_name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit(1)

logger.info("SUCCESS: Connection to RDS for MySQL instance succeeded")

def lambda_handler(event, context):
    logger.info(log_group_fields_response)
    logger.info(log_group_fields_response[0])
    """
    This function selects all records from the 'employees' table in the RDS database
    """
    item_count = 0

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM employees")
        logger.info("Fetching records from the 'employees' table:")
        for row in cur:
            item_count += 1
            logger.info(row)
    
    return "Retrieved %d items from the 'employees' table" % (item_count)

    