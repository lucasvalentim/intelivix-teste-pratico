"""add cinema_no_texto

Revision ID: 75633146d7e9
Revises: 391fcb150ba2
Create Date: 2018-11-11 23:51:14.069405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75633146d7e9'
down_revision = '391fcb150ba2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'andamentos',
        sa.Column('cinema_no_texto', sa.Boolean(), nullable=True)
    )


def downgrade():
    op.drop_column('andamentos', 'cinema_no_texto')
