"""create_tables

Revision ID: caec9ff6ed72
Revises: 
Create Date: 2024-11-26 12:08:42.120191

"""
import os
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'caec9ff6ed72'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    sql_file_path = os.path.join(os.path.dirname(__file__), "../files/create_table.sql")

    with open(sql_file_path, 'r', encoding='utf-8') as file:
        sql_commands = file.read()
        op.execute(sql_commands)


def downgrade() -> None:
    sql_file_path = os.path.join(os.path.dirname(__file__), "../files/drop_table.sql")

    with open(sql_file_path, 'r', encoding='utf-8') as file:
        sql_commands = file.read()
        op.execute(sql_commands)
