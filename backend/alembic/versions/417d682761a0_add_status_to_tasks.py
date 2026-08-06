"""add status to tasks

Revision ID: 417d682761a0
Revises: 358c27ff3576
Create Date: 2026-08-07 01:01:15.832164

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '417d682761a0'
down_revision: Union[str, Sequence[str], None] = '358c27ff3576'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    task_status = sa.Enum(
        "TODO",
        "IN_PROGRESS",
        "DONE",
        name="taskstatus",
    )

    task_status.create(op.get_bind(), checkfirst=True)

    op.add_column(
        "tasks",
        sa.Column(
            "status",
            task_status,
            nullable=False,
            server_default="TODO",
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column("tasks", "status")

    task_status = sa.Enum(
        "TODO",
        "IN_PROGRESS",
        "DONE",
        name="taskstatus",
    )

    task_status.drop(op.get_bind(), checkfirst=True)
