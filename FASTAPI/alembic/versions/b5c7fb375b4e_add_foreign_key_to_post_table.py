"""add foreign-key to post table

Revision ID: b5c7fb375b4e
Revises: 0b067979d2b4
Create Date: 2022-01-21 18:55:51.698215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5c7fb375b4e'
down_revision = '0b067979d2b4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('post', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="post", referent_table="users", 
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")    
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='post')
    op.drop_column('post', 'owner_id')
    pass
