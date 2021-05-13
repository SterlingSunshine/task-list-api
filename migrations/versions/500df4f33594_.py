"""empty message

Revision ID: 500df4f33594
Revises: a13916140b2d
Create Date: 2021-05-07 20:15:19.939437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '500df4f33594'
down_revision = 'a13916140b2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goal', 'title')
    # ### end Alembic commands ###