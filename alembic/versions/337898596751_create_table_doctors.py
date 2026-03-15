"""create table doctors

Revision ID: 337898596751
Revises: 375531eb9985
Create Date: 2026-03-15 09:18:09.513052

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '337898596751'
down_revision: Union[str, Sequence[str], None] = '375531eb9985'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "doctors",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.String(50), nullable=False),
        sa.Column("last_name", sa.String(50), nullable=False),
        sa.Column("specialization", sa.String(50)),
        sa.Column("created_at", sa.DateTime, server_default= sa.func.now(), nullable=False )
    )
    pass


def downgrade() -> None:
    op.drop_table("doctors")
    pass
