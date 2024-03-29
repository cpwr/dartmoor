from sqlalchemy.ext.asyncio.session import AsyncSession

from app import crud, schemas
from app.core.config import settings
# from app.db import Base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.Base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


async def init_db(session: AsyncSession) -> None:
    user = await crud.user.get_by_email(session, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        await crud.user.create(session, obj_in=user_in)
