import boto3
import os
glue_crawler = os.environ['glue_crawler']
def lambda_handler(event, context):
    glue_client = boto3.client('glue')
    glue_client.start_crawler(Name=glue_crawler)
