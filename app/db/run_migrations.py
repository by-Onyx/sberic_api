import subprocess

from dotenv import load_dotenv

load_dotenv()

try:
    # subprocess.run(["alembic", "revision", "--autogenerate", "-m", "insert_data"])
    subprocess.run(["alembic", "upgrade", "head"])
except Exception as e:
    print(f"Ошибка при выполнении миграций: {e}")
