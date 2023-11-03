"""added name fields

Revision ID: 2218f859f3d7
Revises: d1a735737601
Create Date: 2023-11-03 15:37:44.451084

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '2218f859f3d7'
down_revision: Union[str, None] = 'd1a735737601'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('solution_description_images', sa.Column('name', sa.String(), nullable=False))
    op.add_column('solutions', sa.Column('name', sa.String(), nullable=False))
    op.add_column('task_description_images', sa.Column('name', sa.String(), nullable=False))
    op.add_column('tasks', sa.Column('name', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'name')
    op.drop_column('task_description_images', 'name')
    op.drop_column('solutions', 'name')
    op.drop_column('solution_description_images', 'name')
    # ### end Alembic commands ###
