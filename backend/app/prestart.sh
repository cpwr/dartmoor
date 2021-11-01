#! /usr/bin/env bash

set -e
# Run migrations
alembic revision --autogenerate
alembic upgrade head
set +e
