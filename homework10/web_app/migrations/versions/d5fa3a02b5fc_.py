"""empty message

Revision ID: d5fa3a02b5fc
Revises: ec0304b8aa55
Create Date: 2021-06-20 20:45:04.659271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5fa3a02b5fc'
down_revision = 'ec0304b8aa55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stock_db',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), server_default='', nullable=False),
    sa.Column('price', sa.Integer(), server_default='0', nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('stock')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stock',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), server_default=sa.text("''::character varying"), autoincrement=False, nullable=False),
    sa.Column('price', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='stock_pkey')
    )
    op.drop_table('stock_db')
    # ### end Alembic commands ###