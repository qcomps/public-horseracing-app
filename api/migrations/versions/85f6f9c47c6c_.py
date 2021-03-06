"""empty message

Revision ID: 85f6f9c47c6c
Revises: 4ee388a4cf87
Create Date: 2020-07-03 23:27:06.816314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85f6f9c47c6c'
down_revision = '4ee388a4cf87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('past_performances', 'today_race_number')
    op.drop_column('past_performances', 'today_track')
    op.drop_column('past_performances', 'today_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('past_performances', sa.Column('today_date', sa.DATE(), autoincrement=False, nullable=True))
    op.add_column('past_performances', sa.Column('today_track', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('past_performances', sa.Column('today_race_number', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
