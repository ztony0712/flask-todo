"""empty message

Revision ID: 3da0d5163390
Revises: fd82fa1dcf17
Create Date: 2021-10-17 22:15:30.692708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3da0d5163390'
down_revision = 'fd82fa1dcf17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('item', 'status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('status', sa.BOOLEAN(), nullable=True))
    # ### end Alembic commands ###
