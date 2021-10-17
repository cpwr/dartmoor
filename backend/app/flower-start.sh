#! /usr/bin/env bash
set -e

python /app/app/celeryworker_pre_start.py

until timeout -k 10 10 celery -A app.worker inspect ping; do
    >&2 echo "Celery workers not available"
done

echo 'Starting flower'

celery -A app.worker flower -l info -Q main-queue -c 1 --port=5555 --url_prefix=monitor --broker_api=amqp://guest:guest@queue:15672/api/ --broker=amqp://guest:guest@queue:5672//
