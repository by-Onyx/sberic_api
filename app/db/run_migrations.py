import subprocess

from app.db.file_manager.minio_migration import migration as minio_migration

try:
    # subprocess.run(["alembic", "revision", "--autogenerate", "-m", "add_"])
    subprocess.run(["alembic", "upgrade", "head"])
except Exception as e:
    print(f"Ошибка при выполнении миграций: {e}")

minio_migration()
