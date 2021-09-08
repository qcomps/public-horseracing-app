"""empty message

Revision ID: 1cc17045d008
Revises: 5134237598ba
Create Date: 2020-07-19 23:10:55.109266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cc17045d008'
down_revision = '5134237598ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('past_performances', sa.Column('comment', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('past_performances', 'comment')
    # ### end Alembic commands ###