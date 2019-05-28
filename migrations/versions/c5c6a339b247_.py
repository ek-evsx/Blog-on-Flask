"""empty message

Revision ID: c5c6a339b247
Revises: 3508999f74f2
Create Date: 2019-05-28 20:59:15.987688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5c6a339b247'
down_revision = '3508999f74f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('name', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'name')
    # ### end Alembic commands ###