import unittest
from app import *


s3_put_object =  {
		"eventVersion": "1.05",
		"userIdentity": {
			"type": "AWSService",
			"invokedBy": "cloudtrail.amazonaws.com"
		},
		"eventTime": "2019-11-09T19:18:45Z",
		"eventSource": "s3.amazonaws.com",
		"eventName": "PutObject",
		"awsRegion": "us-east-1",
		"sourceIPAddress": "cloudtrail.amazonaws.com",
		"userAgent": "cloudtrail.amazonaws.com",
		"requestParameters": {
			"bucketName": "cloudtrail-log-analytics-s3bucket-1wq1mer0z4wte",
			"Host": "cloudtrail-log-analytics-s3bucket-1wq1mer0z4wte.s3.amazonaws.com",
			"x-amz-acl": "bucket-owner-full-control",
			"x-amz-server-side-encryption": "AES256",
			"key": "AWSLogs/112280397275/CloudTrail/us-east-1/2019/11/09/112280397275_CloudTrail_us-east-1_20191109T1915Z_70IaedJDSUJDc2Tu.json.gz"
		},
		"responseElements": {
			"x-amz-server-side-encryption": "AES256"
		},
		"additionalEventData": {
			"SignatureVersion": "SigV4",
			"CipherSuite": "ECDHE-RSA-AES128-SHA",
			"bytesTransferredIn": 1155,
			"SSEApplied": "SSE_S3",
			"AuthenticationMethod": "AuthHeader",
			"x-amz-id-2": "Br3bOkQLq7xWDXHYx27hauZaIQ16jYANu2nGL6IuvYXuA+aBrQ1GijCZAItgWIgmCJCvDR4BGVk=",
			"bytesTransferredOut": 0
		},
		"requestID": "D15B2D8B187FCF71",
		"eventID": "0a15bd1a-b1f1-44da-baf2-dd41b9e09411",
		"readOnly": "false",
		"resources": [
			{
				"type": "AWS::S3::Object",
				"ARN": "arn:aws:s3:::cloudtrail-log-analytics-s3bucket-1wq1mer0z4wte/AWSLogs/112280397275/CloudTrail/us-east-1/2019/11/09/112280397275_CloudTrail_us-east-1_20191109T1915Z_70IaedJDSUJDc2Tu.json.gz"
			},
			{
				"accountId": "112280397275",
				"type": "AWS::S3::Bucket",
				"ARN": "arn:aws:s3:::cloudtrail-log-analytics-s3bucket-1wq1mer0z4wte"
			}
		],
		"eventType": "AwsApiCall",
		"recipientAccountId": "112280397275",
		"sharedEventID": "e21b3097-3de9-4e35-a963-1690bfdc8553"
	}

dynamodb_event = {
		"eventVersion": "1.06",
		"userIdentity": {
			"type": "AssumedRole",
			"principalId": "AROARUJDO4XNS3VDZZQ4C:awslambda_292_20191110150720334",
			"arn": "arn:aws:sts::112280397275:assumed-role/picture-organizing-two-ProcessKeywordDBStreamRole-1ILTPEVDZ86SM/awslambda_292_20191110150720334",
			"accountId": "112280397275",
			"accessKeyId": "ASIARUJDO4XNSCW45Z7T",
			"sessionContext": {
				"sessionIssuer": {
					"type": "Role",
					"principalId": "AROARUJDO4XNS3VDZZQ4C",
					"arn": "arn:aws:iam::112280397275:role/picture-organizing-two-ProcessKeywordDBStreamRole-1ILTPEVDZ86SM",
					"accountId": "112280397275",
					"userName": "picture-organizing-two-ProcessKeywordDBStreamRole-1ILTPEVDZ86SM"
				},
				"attributes": {
					"creationDate": "2019-11-10T15:07:20Z",
					"mfaAuthenticated": "false"
				}
			}
		},
		"eventTime": "2019-11-10T15:10:52Z",
		"eventSource": "dynamodb.amazonaws.com",
		"eventName": "DescribeStream",
		"awsRegion": "us-east-1",
		"sourceIPAddress": "54.237.198.6",
		"userAgent": "leb-kcl-6193f5fe-c0f5-45ae-b1b0-65f92d577657,amazon-kinesis-client-library-java-lambda_1.2.1, aws-internal/3 aws-sdk-java/1.11.419 Linux/4.14.133-88.105.amzn1.x86_64 OpenJDK_64-Bit_Server_VM/25.181-b13 java/1.8.0_181",
		"requestParameters": {
			"streamArn": "arn:aws:dynamodb:us-east-1:112280397275:table/master-pictures/stream/2019-10-09T00:07:23.254"
		},
		"responseElements": "null",
		"requestID": "LAHU4HOSPLHRP4V91QGF0LTH0VVV4KQNSO5AEMVJF66Q9ASUAAJG",
		"eventID": "d8ef6772-d406-4c5a-a2fa-2923126c938c",
		"readOnly": "true",
		"eventType": "AwsApiCall",
		"apiVersion": "2012-08-10",
		"managementEvent": "true",
		"recipientAccountId": "112280397275"
	}


iam_event = {
		"eventVersion": "1.05",
		"userIdentity": {
			"type": "AWSService",
			"invokedBy": "lambda.amazonaws.com"
		},
		"eventTime": "2019-11-10T15:07:20Z",
		"eventSource": "sts.amazonaws.com",
		"eventName": "AssumeRole",
		"awsRegion": "us-east-1",
		"sourceIPAddress": "lambda.amazonaws.com",
		"userAgent": "lambda.amazonaws.com",
		"requestParameters": {
			"roleSessionName": "awslambda_292_20191110150720334",
			"roleArn": "arn:aws:iam::112280397275:role/picture-organizing-two-ProcessKeywordDBStreamRole-1ILTPEVDZ86SM"
		},
		"responseElements": {
			"credentials": {
				"sessionToken": "IQoJb3JpZ2luX2VjEMD//////////wEaCXVzLWVhc3QtMSJHMEUCIQDYZj+PhrmaiZb9DfaiDbK85bnweSx8X3Fm5IzgbX4yqgIgZYe3xJsb4i21hbQ3JownM5Xy794ag8qOmlihVKdy7ooq5gEI2P//////////ARAAGgwxMTIyODAzOTcyNzUiDM+OoG2Abpti97wQnSq6Afj0sVuPGtfDM+RT+D2CiJkiHL/7+XTXdlTnoUhz1dkkJTSnuoM74VAhbBL1TnnUbTdlrlYJADZ+zyRlRJMoK2+kCr+nF4ycYYNZcLZlYque1KmcyaoMLtn8DcRKIJpERqrw9wk5OLbFxeMFEdVUdbrBNGUVVNv/+NsR+etQ/qIfP/9x6IQ+vKX8+fPm+0HFyKIpJdMwfK0OoJkfEC4rxbUR9JGPkFf6/C5YAVsIjjlfRsQCP14XAxampjCoz6DuBTrgAdfl3typkuBzN8GRg+ACdGnyQ1BztnDZ6uw8invfvPilSUq24oSDKmFhNjeuMJy6bIf6Yl77LjPtizw2Ximhau9wSRIg4/yQX+8AQG4N+5nsgFsOD+YLBSfu5dKJ5/fAJue/StDZ3IFqyoSzuwdKez3zv34O1uCT9ZGPsMKQcrfZmZ0Ur24avc8m4W7EBk/FDGohNLUfdXRtY2m079WuV9WvxmeHZDndn5IrQOFnlWNkBnzP9pfR6PYrSFJCnasC72jnH5slKHkWaiJC8sREFCBr0YD1zybZhvpnv8aDNc85",
				"accessKeyId": "ASIARUJDO4XNSCW45Z7T",
				"expiration": "Nov 10, 2019 5:17:20 PM"
			}
		},
		"requestID": "cac47af7-03cb-11ea-8f54-9185027e1c99",
		"eventID": "ff6e325e-18dd-4fbe-aa09-36bcaf74af68",
		"resources": [
			{
				"ARN": "arn:aws:iam::112280397275:role/picture-organizing-two-ProcessKeywordDBStreamRole-1ILTPEVDZ86SM",
				"accountId": "112280397275",
				"type": "AWS::IAM::Role"
			}
		],
		"eventType": "AwsApiCall",
		"recipientAccountId": "112280397275",
		"sharedEventID": "37a641a7-4ecb-4295-9603-c9cf101a0689"
	}


lambda_event = {
		"eventVersion": "1.05",
		"userIdentity": {
			"type": "IAMUser",
			"principalId": "AIDAJ6J45YO4ULNBAXD3C",
			"arn": "arn:aws:iam::112280397275:user/ziegler-aws",
			"accountId": "112280397275",
			"accessKeyId": "ASIAIOKPUFMUK4AL3K2Q",
			"userName": "ziegler-aws",
			"sessionContext": {
				"sessionIssuer": {},
				"webIdFederationData": {},
				"attributes": {
					"mfaAuthenticated": "false",
					"creationDate": "2019-11-10T14:18:13Z"
				}
			},
			"invokedBy": "cloudformation.amazonaws.com"
		},
		"eventTime": "2019-11-10T14:18:18Z",
		"eventSource": "lambda.amazonaws.com",
		"eventName": "UpdateFunctionCode20150331v2",
		"awsRegion": "us-east-1",
		"sourceIPAddress": "cloudformation.amazonaws.com",
		"userAgent": "cloudformation.amazonaws.com",
		"requestParameters": {
			"functionName": "arn:aws:lambda:us-east-1:112280397275:function:cloudtrail-log-analytics-IndexEventsFunction-1MXRDTV7D9Z58",
			"publish": "false",
			"s3Key": "8ebd738222a3bbc4076ee67d5c595cd4",
			"s3Bucket": "svz-sam",
			"dryRun": "false"
		},
		"responseElements": {
			"functionName": "cloudtrail-log-analytics-IndexEventsFunction-1MXRDTV7D9Z58",
			"functionArn": "arn:aws:lambda:us-east-1:112280397275:function:cloudtrail-log-analytics-IndexEventsFunction-1MXRDTV7D9Z58",
			"runtime": "python3.7",
			"role": "arn:aws:iam::112280397275:role/cloudtrail-log-analytics-IndexEventsFunctionRole-PEWIDJ4ZOYWI",
			"handler": "app.lambda_handler",
			"codeSize": 6994702,
			"description": "",
			"timeout": 3,
			"memorySize": 128,
			"lastModified": "2019-11-10T14:18:18.006+0000",
			"codeSha256": "c4ZdIDijPCkJT49+cpS2V0e48ERTc/iOXcaILm7gx9w=",
			"version": "$LATEST",
			"vpcConfig": {
				"subnetIds": [],
				"securityGroupIds": [],
				"vpcId": ""
			},
			"environment": {},
			"tracingConfig": {
				"mode": "PassThrough"
			},
			"revisionId": "5a2cebce-dd6c-4fc1-a158-b8617f312305"
		},
		"requestID": "af235d90-cd65-4423-a4b8-5f0c27a8bd46",
		"eventID": "f33977fb-6f91-4ddb-bbf5-5b88d7c6a019",
		"eventType": "AwsApiCall",
		"recipientAccountId": "112280397275"
	}


class Tests(unittest.TestCase):

	def test_unzip_file__given_valid_bucket__then_results_returned(self):
		# Arrange
		bucket = "svz-playground"
		key = "trail.gz"
		
		# Act
		result = unzip_file(bucket, key)
		
		# Assert
		self.assertGreater(len(result), 0)
		self.assertTrue("Records" in str(result))
		

	def test_simplify_arn__given_iam__then_last_part(self):
		# Arrange
		input = "arn:aws:iam::112280397275:role/picture-organizing-two-ProcessKeywordDBStreamRole-1ILTPEVDZ86SM"

		# Act
		result = simplify_arn(input)
		
		# Assert
		self.assertEqual(result, "role/picture-organizing-two-ProcessKeywordDBStreamRole-1ILTPEVDZ86SM")


	def test_simplify_arn__given_dynamodb__then_last_part(self):
		# Arrange
		input = "arn:aws:dynamodb:us-east-1:112280397275:table/master-pictures/stream/2019-10-09T00:07:23.254"

		# Act
		result = simplify_arn(input)
		
		# Assert
		self.assertEqual(result, "table/master-pictures/stream/-datetime-")


	def test_shorten_request_arns__given_lambda__then_new_shortened_arn_added(self):
		# Arrange
		input = lambda_event

		# Act
		result= shorten_request_arn(input)
		print(json.dumps(result, indent=3))
		
		# Assert
		self.assertTrue("functionName-shortened" in result["requestParameters"])
		self.assertTrue("main_arn" in result)
		

	def test_shorten_request_arns__given_dynamodb__then_new_shortened_arn_added(self):
		# Arrange
		input = dynamodb_event

		# Act
		result= shorten_request_arn(input)
		print(json.dumps(result, indent=3))
		
		# Assert
		self.assertTrue("streamArn-shortened" in result["requestParameters"])
		self.assertTrue("main_arn" in result)


	def test_shorten_request_arns__given_s3__then_new_shortened_arn_added(self):
		# Arrange
		input = s3_put_object

		# Act
		result= shorten_request_arn(input)
		print(json.dumps(result, indent=3))
		
		# Assert
		self.assertFalse("functionName-shortened" in result["requestParameters"])
		self.assertFalse("main_arn" in result)


	def test_get_data_mgmt_type_from_eventname__given_put_object__then_data_returned(self):
		# Arrange
		input = "PutObject"

		# Act
		result = get_data_mgmt_type_from_eventname(input)

		# Assert
		self.assertEqual(result, "data")


	def test_get_data_mgmt_type_from_eventname__given_get_object__then_data_returned(self):
		# Arrange
		input = "GetObject"

		# Act
		result = get_data_mgmt_type_from_eventname(input)

		# Assert
		self.assertEqual(result, "data")		


	def test_get_data_mgmt_type_from_eventname__given_delete_object__then_data_returned(self):
		# Arrange
		input = "DeleteObject"

		# Act
		result = get_data_mgmt_type_from_eventname(input)

		# Assert
		self.assertEqual(result, "data")


	def test_get_data_mgmt_type_from_eventname__given_copy_object__then_data_returned(self):
		# Arrange
		input = "CopyObject"

		# Act
		result = get_data_mgmt_type_from_eventname(input)

		# Assert
		self.assertEqual(result, "data")


	def test_get_data_mgmt_type_from_eventname__given_upload_part__then_data_returned(self):
		# Arrange
		input = "UploadPart"

		# Act
		result = get_data_mgmt_type_from_eventname(input)

		# Assert
		self.assertEqual(result, "data")


	def test_get_data_mgmt_type_from_eventname__given_invoke_execution__then_data_returned(self):
		# Arrange
		input = "Invoke"

		# Act
		result = get_data_mgmt_type_from_eventname(input)

		# Assert
		self.assertEqual(result, "data")


	def test_get_data_mgmt_type_from_eventname__given_list_object__then_management_returned(self):
		# Arrange
		input = "ListObjects"

		# Act
		result = get_data_mgmt_type_from_eventname(input)

		# Assert
		self.assertEqual(result, "management")

