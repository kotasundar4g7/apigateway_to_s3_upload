aws lambda add-permission --function-name LD_crawler_testing_data --principal s3.amazonaws.com --statement-id 54 --action "lambda:InvokeFunction" --source-arn arn:aws:s3:::demo-dev-classhd --source-account 339712708642
aws s3api put-bucket-notification-configuration \
  --bucket demo-dev-classhd \
  --notification-configuration '{
    "LambdaFunctionConfigurations": [
      {
        "Id": "MyNotification",
        "LambdaFunctionArn": "arn:aws:lambda:ap-south-1:339712708642:function:LD_crawler_testing_data",
        "Events": ["s3:ObjectCreated:*"],
        "Filter": {
          "Key": {
            "FilterRules": [
              {"Name": "prefix", "Value": "testing_data/"},
              {"Name": "suffix", "Value": ".json"}
            ]
          }
        }
      }
    ]
  }'