"""Table userType added

Revision ID: 3bed557a94e4
Revises: 
Create Date: 2022-11-23 20:21:34.199910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bed557a94e4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userType', sa.Column('value', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('userType', 'value')
    # ### end Alembic commands ###