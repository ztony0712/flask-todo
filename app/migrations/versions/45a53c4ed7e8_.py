"""empty message

Revision ID: 45a53c4ed7e8
Revises: a03004cff78d
Create Date: 2021-10-18 16:24:43.625340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45a53c4ed7e8'
down_revision = 'a03004cff78d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('step', sa.Integer(), nullable=True))
    op.drop_column('item', 'progress')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('progress', sa.INTEGER(), nullable=True))
    op.drop_column('item', 'step')
    # ### end Alembic commands ###
