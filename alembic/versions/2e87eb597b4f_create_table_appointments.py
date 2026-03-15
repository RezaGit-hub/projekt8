"""create table appointments

Revision ID: 2e87eb597b4f
Revises: 337898596751
Create Date: 2026-03-15 17:54:30.499570

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e87eb597b4f'
down_revision: Union[str, Sequence[str], None] = '337898596751'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "appointments",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("patient_id", sa.Integer, nullable=False),
        sa.Column("doctor_id", sa.Integer, nullable=False),
        sa.Column("appointment_date", sa.DateTime, nullable=False),
        sa.Column("reason", sa.String(250)),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now(), nullable=False),

        sa.ForeignKeyConstraint(["patient_id"], ["patients.id"]),
        sa.ForeignKeyConstraint(["doctor_id"], ["doctors.id"])

    )

    op.create_index("idx_patient_id", "appointments", ["patient_id"])
    op.create_index("idx_doctor_id", "appointments", ["doctor_id"])
    pass


def downgrade() -> None:
    op.drop_index("idx_patient_id", table_name="appointments")
    op.drop_index("idx_doctor_id", table_name="appointments")
    op.drop_table("appointments")
    pass
