"""Init

Revision ID: 696d6ea780fd
Revises: 
Create Date: 2023-01-16 22:08:06.982491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '696d6ea780fd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('domains',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=250), nullable=False),
    sa.Column('text', sa.String(length=5000), nullable=False),
    sa.Column('url_page', sa.String(length=250), nullable=False),
    sa.Column('published', sa.DateTime(), nullable=True),
    sa.Column('domain_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['domain_id'], ['domains.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('articles')
    op.drop_table('domains')
    # ### end Alembic commands ###
