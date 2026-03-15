"""create patients table

Revision ID: 375531eb9985
Revises: 83016e9d9fc0
Create Date: 2026-03-15 08:53:21.036627

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '375531eb9985'
down_revision: Union[str, Sequence[str], None] = '83016e9d9fc0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "patients",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.String(50), nullable=False),
        sa.Column("last_name", sa.String(50), nullable=False),
        sa.Column("birth_date", sa.Date, nullable=False),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now(), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table("patients")
    pass
