"""add title column to posts table

Revision ID: 8be349694989
Revises: 9c9902ba1063
Create Date: 2023-06-25 01:48:26.538762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8be349694989'
down_revision = '9c9902ba1063'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts","content")
    pass
