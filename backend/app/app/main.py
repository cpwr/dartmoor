from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from strawberry.asgi import GraphQL

from app.api.api_v1.api import api_router
from app.core.config import settings
from app.api.graphql.schema import schema

from app.db.init_db import init_db
from app.db.session import SessionLocal

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url="/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
)


@app.on_event("startup")
async def create_superuser():
    async with SessionLocal() as session:
        async with session.begin():
            await init_db(session)


app.mount("/static", StaticFiles(directory="static"), name="static")

graphql_app = GraphQL(schema, debug=True)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Adds REST API
app.include_router(api_router, prefix=settings.API_V1_STR)

# Adds GraphQL API
app.add_route("/graphql", graphql_app)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Psychologist's blog",
        openapi_version="3.0.2",
        version="1.0",
        description="OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://example.com/assets/assets/images/oksana.jpg"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
