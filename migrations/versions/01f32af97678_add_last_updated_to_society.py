"""Add last updated to society

Revision ID: 01f32af97678
Revises: 18aa58f91b03
Create Date: 2020-09-27 18:39:03.781230

"""
from alembic import op
import sqlalchemy as sa
from datetime import time


# revision identifiers, used by Alembic.
revision = '01f32af97678'
down_revision = '18aa58f91b03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('societies', sa.Column('updated_at', sa.DateTime(), server_default=sa.func.current_timestamp(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('societies', 'updated_at')
    # ### end Alembic commands ###
