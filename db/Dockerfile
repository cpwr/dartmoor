FROM postgres:13.4-buster

ENV POSTGRES_PASSWORD=od30092016
ENV POSTGRES_USER=oksana
ENV POSTGRES_DB=oksana_blog
ENV POSTGRES_SERVER=db


COPY db/init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
