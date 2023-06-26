"""create posts table

Revision ID: 9c9902ba1063
Revises: 
Create Date: 2023-06-25 01:44:43.963721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c9902ba1063'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.Integer(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
