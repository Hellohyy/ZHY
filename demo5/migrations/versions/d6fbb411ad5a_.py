"""empty message

Revision ID: d6fbb411ad5a
Revises: 
Create Date: 2019-07-02 21:08:32.319695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6fbb411ad5a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cc',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('bf_StudentID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('bf_Name', sa.String(length=20), nullable=False),
    sa.Column('bf_sex', sa.String(length=10), nullable=False),
    sa.Column('bf_nation', sa.String(length=20), nullable=False),
    sa.Column('bf_BornDate', sa.String(length=255), nullable=False),
    sa.Column('cla_Name', sa.String(length=40), nullable=False),
    sa.Column('bf_NativePlace', sa.String(length=255), nullable=False),
    sa.Column('bf_ResidenceType', sa.String(length=255), nullable=False),
    sa.Column('bf_policy', sa.String(length=50), nullable=False),
    sa.Column('cla_id', sa.Integer(), nullable=False),
    sa.Column('cla_term', sa.String(length=255), nullable=False),
    sa.Column('bf_zhusu', sa.String(length=5), nullable=False),
    sa.Column('bf_leaveSchool', sa.String(length=5), nullable=False),
    sa.Column('bf_qinshihao', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('bf_StudentID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    op.drop_table('cc')
    op.drop_table('admin')
    # ### end Alembic commands ###
