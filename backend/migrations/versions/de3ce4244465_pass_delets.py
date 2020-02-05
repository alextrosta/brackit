"""pass delets

Revision ID: de3ce4244465
Revises: 81a88e019a16
Create Date: 2020-02-05 08:46:39.901371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de3ce4244465'
down_revision = '81a88e019a16'
branch_labels = None
depends_on = None


def upgrade():
    # # ### commands auto generated by Alembic - please adjust! ###
    # op.alter_column('round', 'bracket_id',
    #            existing_type=sa.INTEGER(),
    #            nullable=True)

    with op.batch_alter_table('round') as batch_op:
        batch_op.alter_column('bracket_id', existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('round', 'bracket_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
