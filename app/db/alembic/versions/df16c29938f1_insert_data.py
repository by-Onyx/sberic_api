"""insert_data

Revision ID: df16c29938f1
Revises: caec9ff6ed72
Create Date: 2024-11-26 12:18:12.354242

"""
import os
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'df16c29938f1'
down_revision: Union[str, None] = 'caec9ff6ed72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    sql_file_path = os.path.join(os.path.dirname(__file__), "../files/insert_data.sql")

    with open(sql_file_path, 'r', encoding='utf-8') as file:
        sql_commands = file.read()
        op.execute(sql_commands)


def downgrade() -> None:
    sql_file_path = os.path.join(os.path.dirname(__file__), "../files/truncate_data.sql")

    with open(sql_file_path, 'r', encoding='utf-8') as file:
        sql_commands = file.read()
        op.execute(sql_commands)
