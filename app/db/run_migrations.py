import subprocess

from dotenv import load_dotenv

from app.db.file_manager.minio_migration import migration as minio_migration

load_dotenv()

try:
    # subprocess.run(["alembic", "revision", "--autogenerate", "-m", "add_"])
    subprocess.run(["alembic", "upgrade", "head"])
except Exception as e:
    print(f"Ошибка при выполнении миграций: {e}")

minio_migration()
