import os

from dotenv import load_dotenv
from minio import Minio

load_dotenv()

MINIO_ROOT_USER = os.getenv('MINIO_ROOT_USER')
MINIO_ROOT_PASSWORD = os.getenv('MINIO_ROOT_PASSWORD')
MINIO_URL = os.getenv('MINIO_URL')
BUCKET_NAME = os.getenv('BUCKET_NAME')

minio_client = Minio(
    MINIO_URL,
    access_key=MINIO_ROOT_USER,
    secret_key=MINIO_ROOT_PASSWORD,
    secure=False
)
