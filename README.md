# overview

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- lambdafunctions - Code for the application's Lambda functions.
- template.yaml - A template that defines the application's AWS resources.
- bash.sh -to create s3 event to run the glue crawler

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.


#prerequisite
1. aws cli
2. aws sam
3. python

# below are changes need to be done in the template.yaml file.
1. line 10 need to give http api gateway name
2. line 11 need to give stage name.
3. line 16 need to give the DynamoDB table name
4. line 32 give lambda function name for generating the presigned URL.
5. line 36 need to give the role name for creating t5he lambda fucntion
6. line 40 and 45 need to change the s3 bucket name.
7. line 57 neeed give the crawler name 
8. line 58 need to give the IAM role name for glue crawler.
9. line 59 need to give the database name of glue catalog.
10. line 62 need to give the s3 path of upload file.
11. line 67  need to give lambda name to start the glue crawler.
12. line 71 need to give IAM role name to create the lambda function.

# below are changes need to be done in the bash.sh file.

1. line 1 need to give the lambda function name,s3 bucket name and aws account number.
2. line 8 need to give ARN of lambda function
3. line 13 an 14 need to give prefix and suffix

# Deployemnet.
1. Once changes are done need to start the deployment by using the below command.
      "sam deploy --guided"
2. once deployement is successfully completed, run bash.sh file using below command.
      "./bash.sh"

