import boto3
import argparse

def download_s3(download_file, bucket_name):
	s3 = boto3.resource("s3")
	bucket = s3.Bucket(bucket_name)

	bucket.download_file(Filename=download_file, Key=download_file)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("download_file", type=str)
	parser.add_argument("bucket_name", type=str)
	args = parser.parse_args()

	download_file = args.download_file
	bucket_name = args.bucket_name

	download_s3(download_file, bucket_name)