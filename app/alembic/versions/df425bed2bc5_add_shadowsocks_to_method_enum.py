"""Add shadowsocks to method enum

Revision ID: df425bed2bc5
Revises: 6415692aeb39
Create Date: 2020-12-12 08:11:49.116212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df425bed2bc5'
down_revision = '6415692aeb39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("ALTER TYPE methodenum ADD VALUE IF NOT EXISTS 'SHADOWSOCKS'")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###