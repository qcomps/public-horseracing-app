"""empty message

Revision ID: 5134237598ba
Revises: 3968538d0d4b
Create Date: 2020-07-19 22:10:39.604147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5134237598ba'
down_revision = '3968538d0d4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column('morning_line_odds', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('results', 'morning_line_odds')
    # ### end Alembic commands ###