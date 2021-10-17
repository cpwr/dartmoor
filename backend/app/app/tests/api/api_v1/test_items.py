from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.core.config import settings
from app.tests.utils.post import create_random_post


async def test_create_post(
    client: TestClient, superuser_token_headers: dict, session: AsyncSession
) -> None:
    data = {"title": "Foo", "description": "Fighters"}
    response = await client.post(
        f"{settings.API_V1_STR}/posts/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content
    assert "owner_id" in content


async def test_read_post(
    client: TestClient, superuser_token_headers: dict, session: AsyncSession
) -> None:
    post = await create_random_post(db)
    response = await client.get(
        f"{settings.API_V1_STR}/posts/{post.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == post.title
    assert content["description"] == post.description
    assert content["id"] == post.id
    assert content["owner_id"] == post.owner_id
