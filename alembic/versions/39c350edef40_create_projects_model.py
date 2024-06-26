"""
Create projects model

Revision ID: 39c350edef40
Revises: 
Create Date: 2024-04-03 23:43:05.647270

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '39c350edef40'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=32), nullable=True),
    sa.Column('description', sa.UnicodeText(), nullable=True),
    sa.Column('date_range', postgresql.DATERANGE(), nullable=True),
    sa.Column('area_of_interest', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_project_id'), 'project', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_project_id'), table_name='project')
    op.drop_table('project')
    # ### end Alembic commands ###
