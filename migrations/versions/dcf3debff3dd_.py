"""empty message

Revision ID: dcf3debff3dd
Revises: 4ece8eb7eece
Create Date: 2023-07-16 14:34:17.395786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcf3debff3dd'
down_revision = '4ece8eb7eece'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('notify_me', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.drop_column('notify_me')

    # ### end Alembic commands ###
