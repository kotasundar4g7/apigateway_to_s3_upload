# Test-Case Report for Serverless File Upload API

## Test Cases

### Test Case 1: Authentication and Signed URL Generation

- **Description**: Test the `/authenticate` endpoint for generating a signed URL.
- **Status**: Passed
- **Details**:
  - Response Status Code: 200
  - Response Body: Contains `uploadUrl` and `requestId`

### Test Case 2: File Upload Using Signed URL

- **Description**: Test the file upload using the signed URL.
- **Status**: Passed
- **Details**:
  - Upload Status Code: 200
  - S3 Bucket: File successfully uploaded

### Test Case 3: Metadata Recording in DynamoDB

- **Description**: Verify that the metadata of the authentication request is recorded in DynamoDB.
- **Status**: Passed
- **Details**:
  - DynamoDB Record: Exists with correct `RoleName` and `Timestamp`

### Test Case 4: AWS Glue Crawler Trigger

- **Description**: Verify that the AWS Glue Crawler is triggered upon file upload.
- **Status**: Passed
- **Details**:
  - Glue Crawler: Trigger verified (mocked)

## Summary

All test cases passed successfully. The API is functioning as expected, with correct metadata recording in DynamoDB, successful file uploads to S3, and appropriate triggers for AWS Glue Crawler.
c