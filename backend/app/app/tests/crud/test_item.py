from sqlalchemy.ext.asyncio.session import AsyncSession

from app import crud
from app.schemas.post import PostCreate, PostUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def test_create_post(session: AsyncSession) -> None:
    title = random_lower_string()
    description = random_lower_string()
    post_in = PostCreate(title=title, description=description)
    user = create_random_user(db)
    post = crud.post.create_with_owner(db=db, obj_in=post_in, owner_id=user.id)
    assert post.title == title
    assert post.description == description
    assert post.owner_id == user.id


def test_get_post(session: AsyncSession) -> None:
    title = random_lower_string()
    description = random_lower_string()
    post_in = PostCreate(title=title, description=description)
    user = create_random_user(db)
    post = crud.post.create_with_owner(db=db, obj_in=post_in, owner_id=user.id)
    stored_post = crud.post.get(db=db, id=post.id)
    assert stored_post
    assert post.id == stored_post.id
    assert post.title == stored_post.title
    assert post.description == stored_post.description
    assert item.owner_id == stored_item.owner_id


def test_update_item(session: AsyncSession) -> None:
    title = random_lower_string()
    description = random_lower_string()
    item_in = PostCreate(title=title, description=description)
    user = create_random_user(db)
    item = crud.item.create_with_owner(db=db, obj_in=item_in, owner_id=user.id)
    description2 = random_lower_string()
    item_update = PostUpdate(description=description2)
    item2 = crud.item.update(db=db, db_obj=item, obj_in=item_update)
    assert item.id == item2.id
    assert item.title == item2.title
    assert item2.description == description2
    assert item.owner_id == item2.owner_id


def test_delete_item(session: AsyncSession) -> None:
    title = random_lower_string()
    description = random_lower_string()
    item_in = PostCreate(title=title, description=description)
    user = create_random_user(db)
    item = crud.item.create_with_owner(db=db, obj_in=item_in, owner_id=user.id)
    item2 = crud.item.remove(db=db, id=item.id)
    item3 = crud.item.get(db=db, id=item.id)
    assert item3 is None
    assert item2.id == item.id
    assert item2.title == title
    assert item2.description == description
    assert item2.owner_id == user.id
