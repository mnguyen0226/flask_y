"""many-to-many relationship

Revision ID: ceeecbe1801b
Revises: 653c918be546
Create Date: 2023-01-20 12:13:06.185070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ceeecbe1801b"
down_revision = "653c918be546"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "like",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("author", sa.Integer(), nullable=False),
        sa.Column("post_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["author"], ["users.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["post_id"], ["posts.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("like")
    # ### end Alembic commands ###