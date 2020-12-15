"""empty message

Revision ID: 0ce0b68c292a
Revises: 3d6811f9fb31
Create Date: 2020-12-16 00:13:29.596602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ce0b68c292a'
down_revision = '3d6811f9fb31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('reservation', 'roomID',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_unique_constraint(None, 'reservation', ['id'])
    op.create_unique_constraint(None, 'user', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'reservation', type_='unique')
    op.alter_column('reservation', 'roomID',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
