import json
import boto3
import secrets
from datetime import datetime, timedelta
import os
 
dynamodb = boto3.client('dynamodb')
s3 = boto3.client('s3')
DYNAMODB_TABLE = os.environ['DYNAMODB_TABLE']
S3_BUCKET = os.environ['S3_BUCKET']
 
def lambda_handler(event, context):
    try:
        print(f"Event: {event}")  # Log the incoming event
        if isinstance(event, dict) and 'body' in event:
            body = json.loads(event['body'])
        else:
            body = event
        role_name = body.get('role_name') #Extract role name from the request (authentication logic can be added here)
        if not role_name:
            raise ValueError("Missing 'role_name' in request")
 
        request_time = datetime.utcnow().isoformat() # fecting the time stamp to store into dynamoDB
 
        # Recording the metadata into the dynamoDB.
        dynamodb.put_item(
            TableName=DYNAMODB_TABLE,
            Item={
                'rolename': {'S': role_name},
                'requesttime': {'S': request_time}
            }
        )
 
        # Generate a signed URL for S3 upload
        bucket_name = S3_BUCKET
        key = f'uploads/{secrets.token_hex(5)}.json' #path to load json file 
        url = s3.generate_presigned_url(
            ClientMethod='put_object',
            Params={
                'Bucket': bucket_name,
                'Key': key,
                'ContentType': 'application/json',
                'Metadata': {
                    'client': 'client_value',
                    'environment': 'environment_value'
                }
            },
            ExpiresIn=3600  # 60 minutes to expire the signed URL
        )
 
 
        return {
            'statusCode': 200,
            'body': json.dumps({
                'uploadUrl': url,
                'key': key
            })
        } # returning the signed URL to the api
 
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Internal server error',
                'error': str(e)
            })
        }