from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio.session import AsyncSession

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Post])
async def read_posts(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve posts.
    """
    if crud.user.is_superuser(current_user):
        posts = await crud.post.get_multi(db, skip=skip, limit=limit)
    else:
        posts = await crud.post.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return posts


@router.post("/", response_model=schemas.Post)
async def create_post(
    *,
    db: AsyncSession = Depends(deps.get_db),
    post_in: schemas.PostCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new post.
    """
    post = await crud.post.create_with_owner(db=db, obj_in=post_in, owner_id=current_user.id)
    return post


@router.put("/{id}", response_model=schemas.Post)
async def update_post(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    post_in: schemas.PostUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an post.
    """
    post = await crud.post.get(db=db, id=id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if not crud.user.is_superuser(current_user) and (post.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    post = await crud.post.update(db=db, db_obj=post, obj_in=post_in)
    return post


@router.get("/{id}", response_model=schemas.Post)
async def read_item(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get item by ID.
    """
    item = await crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Post not found")
    if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return item


@router.delete("/{id}", response_model=schemas.Post)
async def delete_item(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    item = await crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Post not found")
    if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    item = await crud.item.remove(db=db, id=id)
    return item
