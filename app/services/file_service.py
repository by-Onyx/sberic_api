from app.db.file_manager.minio_connection import minio_client, BUCKET_NAME


class FileService:

    def get_file(self, file_name: str):
        return minio_client.get_object(
            bucket_name=BUCKET_NAME,
            object_name=file_name
        )
