from app.db.file_manager.minio_connection import minio_client, BUCKET_NAME


def get_file(file_name: str):
    return minio_client.get_object(
        bucket_name=BUCKET_NAME,
        object_name=file_name
    )
