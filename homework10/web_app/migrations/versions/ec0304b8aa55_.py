"""empty message

Revision ID: ec0304b8aa55
Revises: 
Create Date: 2021-06-20 20:38:43.937365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec0304b8aa55'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), server_default='', nullable=False),
    sa.Column('price', sa.Integer(), server_default='0', nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock')
    # ### end Alembic commands ###
