import json
import boto3
from io import BytesIO
import gzip
import traceback
import urllib
import os
import datetime
import re
import copy
from aws_requests_auth.aws_auth import AWSRequestsAuth
from elasticsearch import Elasticsearch, RequestsHttpConnection
from aws_requests_auth.boto_utils import BotoAWSRequestsAuth


es_host = os.environ["ES_PATH"].replace("https://", "")
auth = BotoAWSRequestsAuth(aws_host=es_host,
									aws_region='us-east-1',
									aws_service='es')

# use the requests connection_class and pass in our custom auth class
es = Elasticsearch(host=es_host, use_ssl=True, port=443, connection_class=RequestsHttpConnection, http_auth=auth)


def lambda_handler(event, context):
	print(event)
	bucket = json.loads(event['Records'][0]['Sns']['Message'])['s3Bucket']
	key = json.loads(event['Records'][0]['Sns']['Message'])['s3ObjectKey'][0]
	print("Bucket: " + bucket)
	print("Key: " + key)
	try:
		data = unzip_file(bucket, key)
		print(data)
		for record in json.loads(data)['Records']:
			event_name = record["eventName"]
			updated_event = shorten_request_arn(record)
			updated_event["trail_type"] = get_data_mgmt_type_from_eventname(event_name)
			updated_event["agg_count"] = 1
			record_json = json.dumps(updated_event, indent=3)
			index_into_es(record_json)
			print("Indexed into ES")
	except Exception as e:
		traceback.print_exc()
		raise e

	return {
		"statusCode": 200,
		"body": json.dumps({
			"message": "hello world",
			# "location": ip.text.replace("\n", "")
		}),
	}


def unzip_file(bucket, key):
	try:
		s3 = boto3.resource('s3')
		obj = s3.Object(bucket, key)
		n = obj.get()['Body'].read()
		gzipfile = BytesIO(n)
		gzipfile = gzip.GzipFile(fileobj=gzipfile)
		content = gzipfile.read()
		return content.decode("utf-8")
	except Exception as e:
		print(e)
		raise e


def index_into_es(event):
	indexName = 'ct-' + datetime.datetime.now().strftime("%Y-%m-%d")
	res = es.index(index=indexName, doc_type='record', body=event)


def simplify_arn(arn):
	datetime_pattern = r"2[0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]" # 2019-10-09T00:07:23.254
	simplified = re.sub(datetime_pattern, "-datetime-", arn)
	beginning_to_last_colon = r"^.*:"
	simplified = re.sub(beginning_to_last_colon, "", simplified)
	return simplified


def shorten_request_arn(event):
	updated_event = copy.deepcopy(event)
	if "requestParameters" in event:
		for key,value in event["requestParameters"].items():
			if type(value) == str:
				if value.startswith("arn:"):
					shorten_arn = simplify_arn(value)
					print("*** arn")
					print(shorten_arn)
					updated_event["requestParameters"][key + "-shortened"] = shorten_arn
					updated_event["main_arn"] = shorten_arn
				if key == "Bucket":
					updated_event["main_arn"] = value

	return updated_event


def get_data_mgmt_type_from_eventname(event_name):
	type = "management"

	data_prefixes = ["Put", "Get", "Delete", "Upload", "Copy", "Invoke", "InvokeExecution"]
	for prefix in data_prefixes:
		if event_name.startswith(prefix):
			type = "data"
			break
	return type

