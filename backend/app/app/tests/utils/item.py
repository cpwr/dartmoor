from typing import Optional

from sqlalchemy.ext.asyncio.session import AsyncSession

from app import crud, models
from app.schemas.post import PostCreate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


async def create_random_post(session: AsyncSession, *, owner_id: Optional[int] = None) -> models.Post:
    if owner_id is None:
        user = await create_random_user(db)
        owner_id = user.id
    title = random_lower_string()
    description = random_lower_string()
    post_in = PostCreate(title=title, description=description, id=id)
    return await crud.post.create_with_owner(db=db, obj_in=post_in, owner_id=owner_id)
