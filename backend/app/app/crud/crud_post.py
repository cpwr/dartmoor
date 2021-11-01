from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app.models.post import Post
from app.schemas.post import PostCreate, PostUpdate


class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):
    async def create_with_owner(
        self, session: AsyncSession, *, obj_in: PostCreate, owner_id: int
    ) -> Post:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        await db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def get_multi_by_owner(
        self, session: AsyncSession, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Post]:
        return (
            await db.query(self.model)
            .filter(Post.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


post = CRUDPost(Post)
