import logging
from typing import Any, Dict, Optional, Union

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


log = logging.getLogger(__name__)


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    @staticmethod
    async def get_by_email(session: AsyncSession, *, email: str) -> Optional[User]:
        stmt = select(User).where(User.email == email)
        res = await session.execute(stmt)
        return res.scalars().first()

    @staticmethod
    async def create(session: AsyncSession, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_superuser=obj_in.is_superuser,
        )
        session.add(db_obj)
        await session.commit()
        return db_obj

    async def update(
        self, session: AsyncSession, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return await super().update(session, db_obj=db_obj, obj_in=update_data)

    async def authenticate(self, session: AsyncSession, *, email: str, password: str) -> Optional[User]:
        user = await self.get_by_email(session, email=email)
        if not user:
            return

        log.error("!!!" * 50)
        log.error(user)
        log.error(user.hashed_password)
        log.error("!!!" * 50)
        if not verify_password(password, user.hashed_password):
            return

        return user

    @staticmethod
    def is_active(user: User) -> bool:
        return user.is_active

    @staticmethod
    def is_superuser(user: User) -> bool:
        return user.is_superuser


user = CRUDUser(User)
