import boto3
def lambda_handler(event, context):
    glue_client = boto3.client('glue')
    glue_client.start_crawler(Name='api_table')
