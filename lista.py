import boto3

client = boto3.client("s3", "us-east-1")
responce = client.list_buckets()

print(responce)
print("Hola mundo")