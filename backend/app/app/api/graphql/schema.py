from __future__ import annotations

import typing
import strawberry
from strawberry.schema.config import StrawberryConfig


@strawberry.type
class Book:
    title: str
    author: Author


@strawberry.type
class Author:
    name: str
    books: typing.List['Book']


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"


schema = strawberry.Schema(
    query=Query,
    mutation=None,
    subscription=None,
    config=StrawberryConfig(auto_camel_case=False)
)
