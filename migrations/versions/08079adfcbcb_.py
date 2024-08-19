"""empty message

Revision ID: 08079adfcbcb
Revises: 8af21628299c
Create Date: 2024-08-19 15:35:23.691644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08079adfcbcb'
down_revision = '8af21628299c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###
