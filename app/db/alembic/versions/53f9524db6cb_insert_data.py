"""insert_data

Revision ID: 53f9524db6cb
Revises: a6a9f1e40973
Create Date: 2024-10-20 21:45:45.378434

"""
import os
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '53f9524db6cb'
down_revision: Union[str, None] = 'a6a9f1e40973'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def read_sql_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def upgrade() -> None:
    sql_file_path = os.path.join(os.path.dirname(__file__), '../files/insert_data.sql')

    sql_content = read_sql_file(sql_file_path)
    op.execute(sql_content)


def downgrade() -> None:
    sql_file_path = os.path.join(os.path.dirname(__file__), '../files/truncate_data.sql')

    sql_content = read_sql_file(sql_file_path)
    op.execute(sql_content)
