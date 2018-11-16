"""add qntd_andamentos

Revision ID: 391fcb150ba2
Revises: 
Create Date: 2018-11-11 23:46:27.192494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '391fcb150ba2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'processos',
        sa.Column('qntd_andamentos', sa.Integer(), nullable=True)
    )


def downgrade():
    op.drop_column('processos', 'qntd_andamentos')
