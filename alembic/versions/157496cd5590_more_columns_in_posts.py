"""more columns in posts

Revision ID: 157496cd5590
Revises: f821d7d7d4d7
Create Date: 2023-06-25 21:40:30.642550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '157496cd5590'
down_revision = 'f821d7d7d4d7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts',sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
