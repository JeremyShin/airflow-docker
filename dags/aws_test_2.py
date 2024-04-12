import boto3

# Retrieve the list of existing buckets
s3 = boto3.client('s3', endpoint_url="http://localhost:4566")
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

# s3_client = boto3.client('s3', endpoint_url="http://localhost:4566")
# resposne = s3_client.upload_file('./test.csv', 'processed-data', 'test.csv')

obj_list = s3.list_objects(Bucket='processed-data')
contents_list = obj_list['Contents']

for content in contents_list:
    print(content)