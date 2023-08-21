# FROM postgres:alpine3.14

# Uncomment to use Mac M1
FROM --platform=linux/arm64/v8 postgres:alpine3.14
COPY create-databases.sh /docker-entrypoint-initdb.d/
COPY create_table.sql /docker-entrypoint-initdb.d/
