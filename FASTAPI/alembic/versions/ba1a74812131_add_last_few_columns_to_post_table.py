"""add last few columns to post table

Revision ID: ba1a74812131
Revises: b5c7fb375b4e
Create Date: 2022-01-21 19:06:14.980102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba1a74812131'
down_revision = 'b5c7fb375b4e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('post', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('post', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)    
    pass


def downgrade():
    op.drop_column('post', 'published')
    op.drop_column('post', 'created_at')
    pass
