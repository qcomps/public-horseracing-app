"""empty message

Revision ID: 908476d0f9b7
Revises: 3237fd8e017a
Create Date: 2020-08-12 12:30:06.938552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '908476d0f9b7'
down_revision = '3237fd8e017a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column('predicted_individual_perf', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('results', 'predicted_individual_perf')
    # ### end Alembic commands ###
