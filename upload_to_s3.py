import boto3
import os
from dotenv import load_dotenv

load_dotenv()

bucket_name = os.getenv('BUCKET_NAME')
s3 = boto3.client("s3")

def create_bucket(bucket_name):
    try:
        s3.create_bucket(
            Bucket=bucket_name,
        )
        print(f"Bucket {bucket_name} created successfully.")
    except s3.exceptions.BucketAlreadyOwnedByYou:
        print(f"Bucket {bucket_name} already exists.")
    except Exception as e:
        print(f"Error creating bucket: {e}")

def upload_directory(directory_path, s3_prefix):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file).replace("\\", "/")
            relpath = os.path.relpath(file_path, directory_path)
            s3_key = os.path.join(s3_prefix, relpath).replace("\\", "/")
            
            s3.upload_file(file_path, bucket_name, s3_key)
            print(f"Uploaded {s3_key}")

if __name__ == "__main__":
    create_bucket(bucket_name)
    upload_directory('tinybert-sentiment-analysis', 'ml-models/tinybert-sentiment-analysis')
