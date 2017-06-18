"""init tables

Revision ID: 577e59df1128
Revises: 
Create Date: 2017-06-18 18:19:57.123092

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy import ForeignKey

# revision identifiers, used by Alembic.
revision = '577e59df1128'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Note: Indexing?
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("email", sa.String(128), nullable=False),
        sa.Column("password", sa.String(128), nullable=False),
        sa.Column("name", sa.String(128)),
    )

    op.create_table(
        "post",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("user_id", sa.Integer, ForeignKey("user.id")),
        sa.Column("image_name", sa.String(128)),
        sa.Column("content", sa.String(512)),
        sa.Column("date_created", sa.DateTime, nullable=False),
        sa.Column("is_liked", sa.Integer, nullable=False, default=0)
    )


def downgrade():
    pass
