import boto3
import logging

import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def download_model_from_s3(
    local_dir="./model", s3_prefix="ml-models/tinybert-sentiment-analysis"
):
    """
    Download the fine-tuned model from S3 bucket
    """
    bucket_name = os.getenv("BUCKET_NAME")
    if not bucket_name:
        raise ValueError("BUCKET_NAME not found in .env file")

    os.makedirs(local_dir, exist_ok=True)

    s3_client = boto3.client("s3")

    model_files = [
        "config.json",
        "model.safetensors",
        "special_tokens_map.json",
        "tokenizer_config.json",
        "tokenizer.json",
        "vocab.txt",
    ]

    logger.info(f"Downloading model from S3 bucket: {bucket_name}/{s3_prefix}")

    for file_name in model_files:
        try:
            local_file_path = os.path.join(local_dir, file_name)

            if os.path.exists(local_file_path):
                logger.info(f"File {file_name} already exists, skipping...")
                continue

            s3_key = f"{s3_prefix}/{file_name}" if s3_prefix else file_name

            logger.info(f"Downloading {s3_key}...")
            s3_client.download_file(bucket_name, s3_key, local_file_path)
            logger.info(f"Successfully downloaded {file_name}")
        except Exception as e:
            logger.error(f"Error downloading {file_name}: {e}")
            raise

    logger.info("Model download completed successfully")
    return local_dir
