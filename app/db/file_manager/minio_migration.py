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
                object_name='hat.png',
                file_path=CURRENT_DIR + '/mock_minio_files/hat.png',
            )
            minio_client.fput_object(
                bucket_name=BUCKET_NAME,
                object_name='hat_cowboy.png',
                file_path=CURRENT_DIR + '/mock_minio_files/hat_cowboy.png',
            )
            minio_client.fput_object(
                bucket_name=BUCKET_NAME,
                object_name='hat_red.png',
                file_path=CURRENT_DIR + '/mock_minio_files/hat_red.png',
            )
            minio_client.fput_object(
                bucket_name=BUCKET_NAME,
                object_name='hoodie_green.png',
                file_path=CURRENT_DIR + '/mock_minio_files/hoodie_green.png',
            )
            minio_client.fput_object(
                bucket_name=BUCKET_NAME,
                object_name='hoodie_red.png',
                file_path=CURRENT_DIR + '/mock_minio_files/hoodie_red.png',
            )
            minio_client.fput_object(
                bucket_name=BUCKET_NAME,
                object_name='scarf_green.png',
                file_path=CURRENT_DIR + '/mock_minio_files/scarf_green.png',
            )
            minio_client.fput_object(
                bucket_name=BUCKET_NAME,
                object_name='scarf_red.png',
                file_path=CURRENT_DIR + '/mock_minio_files/scarf_red.png',
            )
            minio_client.fput_object(
                bucket_name=BUCKET_NAME,
                object_name='shirt_white.png',
                file_path=CURRENT_DIR + '/mock_minio_files/shirt_white.png',
            )



            minio_client.fput_object(
                bucket_name=BUCKET_NAME,
                object_name='location.png',
                file_path=CURRENT_DIR + '/mock_minio_files/location.png',
            )
            minio_client.fput_object(
                bucket_name=BUCKET_NAME,
                object_name='hell.jpeg',
                file_path=CURRENT_DIR + '/mock_minio_files/hell.jpeg',
            )
            minio_client.fput_object(
                bucket_name=BUCKET_NAME,
                object_name='heaven.jpg',
                file_path=CURRENT_DIR + '/mock_minio_files/heaven.jpg',
            )

            print(f"Успешно")
        except S3Error as e:
            print(f"Ошибка при загрузке файла: {e}")
