"""create_tables

Revision ID: a6a9f1e40973
Revises: 
Create Date: 2024-10-20 21:05:49.944366

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'a6a9f1e40973'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('character_type',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.Text(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('clothes_type',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.Text(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('location_type',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.Text(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('transaction_type',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.Text(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('user',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('login', sa.Text(), nullable=False),
                    sa.Column('password', sa.Text(), nullable=False),
                    sa.Column('age', sa.SMALLINT(), nullable=False),
                    sa.Column('balance', sa.Numeric(precision=10, scale=2), nullable=False),
                    sa.Column('creation_date', sa.TIMESTAMP(), nullable=False,
                              server_default=sa.text('CURRENT_TIMESTAMP')),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('login')
                    )
    op.create_table('character',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.Text(), nullable=False),
                    sa.Column('character_type_id', sa.Integer(), nullable=True),
                    sa.Column('happiness_percent', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['character_type_id'], ['character_type.id'], ondelete='SET NULL'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('clothes',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.Text(), nullable=False),
                    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
                    sa.Column('file_name', sa.Text(), nullable=False),
                    sa.Column('clothes_type_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['clothes_type_id'], ['clothes_type.id'], ondelete='SET NULL'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('file_name')
                    )
    op.create_table('location',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.Text(), nullable=False),
                    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
                    sa.Column('file_name', sa.Text(), nullable=False),
                    sa.Column('type_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['type_id'], ['location_type.id'], ondelete='SET NULL'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('file_name'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('user_transactions',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('transfer_amount', sa.Numeric(precision=10, scale=2), nullable=False),
                    sa.Column('transaction_type_id', sa.Integer(), nullable=False),
                    sa.Column('datetime', postgresql.TIMESTAMP(), nullable=False,
                              server_default=sa.text('CURRENT_TIMESTAMP')),
                    sa.ForeignKeyConstraint(['transaction_type_id'], ['transaction_type.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='SET NULL'),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('character_clothes',
                    sa.Column('character_id', sa.Integer(), nullable=False),
                    sa.Column('clothes_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['clothes_id'], ['clothes.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('character_id', 'clothes_id')
                    )
    op.create_table('user_character',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('character_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'character_id')
                    )
    op.create_table('user_clothes',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('clothes_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['clothes_id'], ['clothes.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'clothes_id')
                    )
    op.create_table('user_location',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('location_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'location_id')
                    )


def downgrade() -> None:
    op.drop_table('user_location')
    op.drop_table('user_clothes')
    op.drop_table('user_character')
    op.drop_table('character_clothes')
    op.drop_table('user_transactions')
    op.drop_table('location')
    op.drop_table('clothes')
    op.drop_table('character')
    op.drop_table('user')
    op.drop_table('transaction_type')
    op.drop_table('location_type')
    op.drop_table('clothes_type')
    op.drop_table('character_type')
