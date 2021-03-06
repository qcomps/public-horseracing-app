"""empty message

Revision ID: a2bb9e7b17a4
Revises: 1cc17045d008
Create Date: 2020-08-10 18:00:13.549695

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a2bb9e7b17a4'
down_revision = '1cc17045d008'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column(
        'scratched', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('results', 'scratched')
    # ### end Alembic commands ###
