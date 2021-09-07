import boto3
import argparse
from glob import glob
from tqdm import tqdm

# ローカルファイルをAWS S3上にアップロードする
def upload_s3(input_file, bucket_name, upload_file):
	s3 = boto3.resource("s3")
	bucket = s3.Bucket(bucket_name)

	# バケット直下にファイルを格納
	bucket.upload_file(input_file, upload_file)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("input_file", type=str)
	parser.add_argument("bucket_name", type=str)
	parser.add_argument("upload_file", type=str)
	args = parser.parse_args()

	input_files = glob(args.input_file)
	print(input_files)
	bucket_name = args.bucket_name
	upload_file = args.upload_file

	for input_file in tqdm(input_files):
		print(input_file)

	#upload_s3(input_file, bucket_name, upload_file)
