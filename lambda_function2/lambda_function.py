import boto3
import os
glue_crawler = os.environ['glue_crawler'] # fetching the glue crawler name 
def lambda_handler(event, context):
    glue_client = boto3.client('glue')# creating boto3 client for glue.
    glue_client.start_crawler(Name=glue_crawler)# triggering  the glue crawler.
