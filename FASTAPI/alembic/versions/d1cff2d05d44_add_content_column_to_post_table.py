"""add content column to post table

Revision ID: d1cff2d05d44
Revises: 20e3eab0b62b
Create Date: 2022-01-21 17:45:08.785772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1cff2d05d44'
down_revision = '20e3eab0b62b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('post', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('post', 'content')
    pass
