import os

from minio import S3Error

from app.db.file_manager.minio_connection import minio_client

BUCKET_NAME = os.getenv('BUCKET_NAME')
CURRENT_DIR = os.path.dirname(__file__)


def migration():
    __create_bucket()
    __add_mock_files()


def __create_bucket():
    if not minio_client.bucket_exists(BUCKET_NAME):
        try:
            minio_client.make_bucket(BUCKET_NAME)
        except S3Error as e:
            print(f"Не удалось создать bucket: {e}")


def __add_mock_files():
    objects = minio_client.list_objects(BUCKET_NAME, recursive=True)
    is_empty = not any(objects)
    if is_empty:
        try:
            minio_client.fput_object(
                bucket_name=BUCKET_NAME,
                object_name='base_hat.png',
                file_path=CURRENT_DIR + '/mock_minio_files/base_hat.png',
            )
            minio_client.fput_object(
                bucket_name=BUCKET_NAME,
                object_name='base_location.png',
                file_path=CURRENT_DIR + '/mock_minio_files/base_location.png'
            )
        except S3Error as e:
            print(f"Ошибка при загрузке файла: {e}")
