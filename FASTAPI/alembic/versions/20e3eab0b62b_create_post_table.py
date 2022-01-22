"""create post table

Revision ID: 20e3eab0b62b
Revises: 
Create Date: 2022-01-21 17:34:34.616476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20e3eab0b62b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('post', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('post')
    pass
