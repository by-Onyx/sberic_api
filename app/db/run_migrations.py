import subprocess

from dotenv import load_dotenv

load_dotenv()

# subprocess.run(["alembic", "revision", "--autogenerate", "-m", "insert_data"])
subprocess.run(["alembic", "upgrade", "head"])
