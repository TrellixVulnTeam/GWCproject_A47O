"""empty message

Revision ID: ac2c3950a44b
Revises: b0180ab048b2
Create Date: 2020-12-15 22:16:22.850882

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ac2c3950a44b'
down_revision = 'b0180ab048b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservation', sa.Column('roomID', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'reservation', 'space', ['roomID'], ['id'])
    op.add_column('space', sa.Column('is_publish', sa.Boolean(), nullable=True))
    op.alter_column('space', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.drop_column('space', 'is_reserved')
    op.drop_column('space', 'reservations')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('space', sa.Column('reservations', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    op.add_column('space', sa.Column('is_reserved', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.alter_column('space', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.drop_column('space', 'is_publish')
    op.drop_constraint(None, 'reservation', type_='foreignkey')
    op.drop_column('reservation', 'roomID')
    # ### end Alembic commands ###
