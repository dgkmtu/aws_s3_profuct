import boto3

def get_bucket_name():
	s3 = boto3.client("s3")
	response = s3.list_buckets()

	for bucket in response["Buckets"]:
		print(bucket["Name"])

if __name__ == "__main__":

	get_bucket_name()