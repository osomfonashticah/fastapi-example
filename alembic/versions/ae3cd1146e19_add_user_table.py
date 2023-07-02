"""add user table

Revision ID: ae3cd1146e19
Revises: 29546efbd313
Create Date: 2023-07-02 11:42:39.523427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae3cd1146e19'
down_revision = '29546efbd313'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))

    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
