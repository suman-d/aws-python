# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = boto3.resource('s3')
bucket = s3.create_bucket(Bucket="mydemovideobucket")
bucket = s3.create_bucket(Bucket="mydemovideobucket2", CreateBucketCOnfiguration={'LocationConstraint': session.region_name})
bucket = s3.create_bucket(Bucket="mydemovideobucket2", CreateBucketConfiguration={'LocationConstraint': session.region_name})
fro pathlib import Path
from pathlib import Path
get_ipython().run_line_magic('ls', '/Users/sumandebnath/Downloads/Pexels\\ Videos\\ 1122526.mp4')
pathname = '/Users/sumandebnath/Downloads/Pexels Videos 1122526.mp4'
path - Path(pathname)
path = Path(pathname)
path
path = path.expanduser()
path
path = path.resolve()
path
bucket
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
rekognition_client = session.client('rekognition', region_name='us-west-1')
response = rekognition_client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name, 'Name': path.name}})
response = rekognition_client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name, 'Name': path.name}})
rekognition_client = session.client('rekognition', region_name='us-east-1')
response = rekognition_client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name, 'Name': path.name}})
response
job_id = response["JobId"}
job_id = response["JobId"]
job_id
result = rekognition_client.get_label_detection(JobId=job_id)
result
response["JobStatus"]
result["JobStatus"]
result["Lables"]
result["Labels"]
data = [i for i in result["Labels"] if i['Confidence'] > 80 ]
type(result['Labels'])
result['Labels'][0]
result['Labels'][0]['Confidence']
data = [i for i in result["Labels"] if i['Label']['Confidence'] > 80 ]
data
data = [i for i in result["Labels"] if i['Label']['Confidence'] > 90 ]
data
data = [i['Label']['Name'] for i in result["Labels"] if i['Label']['Confidence'] > 90 ]
data
data = [i['Label']['Name'] for i in result["Labels"] if i['Label']['Confidence'] > 90 ]
set(data)
