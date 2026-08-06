"""add priority to tasks

Revision ID: ae809793e216
Revises: 417d682761a0
Create Date: 2026-08-07 01:34:39.642064

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae809793e216'
down_revision: Union[str, Sequence[str], None] = '417d682761a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    task_priority = sa.Enum(
        "LOW",
        "MEDIUM",
        "HIGH",
        name="taskpriority",
    )

    task_priority.create(op.get_bind(), checkfirst=True)

    op.add_column(
        "tasks",
        sa.Column(
            "priority",
            task_priority,
            nullable=False,
            server_default="MEDIUM",
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column(
        "tasks",
        "priority",
    )

    task_priority = sa.Enum(
        "LOW",
        "MEDIUM",
        "HIGH",
        name="taskpriority",
    )

    task_priority.drop(
        op.get_bind(),
        checkfirst=True,
    )
