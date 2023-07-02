"""add content column to posts table

Revision ID: 29546efbd313
Revises: c23a3be63e8a
Create Date: 2023-07-02 11:32:17.452474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29546efbd313'
down_revision = 'c23a3be63e8a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
