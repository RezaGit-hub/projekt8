"""create users table

Revision ID: 83016e9d9fc0
Revises: 
Create Date: 2026-03-11 19:25:00.510208

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83016e9d9fc0'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String(100), nullable= False, unique=True),
        sa.Column("password_hash", sa.Text(), nullable= False),
        sa.Column("role", sa.String(30), server_default="user")
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
