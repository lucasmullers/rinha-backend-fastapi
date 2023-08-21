#!/bin/bash

set -e
set -u

function create_user_and_database() {
	local database=$1
	echo "Creating user and database '$database'"
	psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
	    CREATE USER $database PASSWORD '$database';
	    CREATE DATABASE $database;
	    GRANT ALL PRIVILEGES ON DATABASE $database TO $database;
EOSQL
}

function create_table() {
	local database=$1
	echo "Creating table '$database'"
	psql -v ON_ERROR_STOP=1 -d $database -U "$POSTGRES_USER" <<-EOSQL
		DROP TABLE IF EXISTS "public"."pessoas";
		CREATE TABLE "public"."pessoas"(
			"stack" varchar[],
			"id" uuid NOT NULL,
			"apelido" character varying(32) NOT NULL,
			"nome" character varying(100) NOT NULL,
			"nascimento" character varying(10) NOT NULL
		);
		CREATE UNIQUE INDEX pessoas_pkey ON public.pessoas USING btree (id);
		CREATE UNIQUE INDEX pessoas_apelido_key ON public.pessoas USING btree (apelido);
		CREATE INDEX ix_pessoas_id ON public.pessoas USING btree (id);
EOSQL
}


echo "Creating DB(s): rinha"
for db in $(echo "rinha" | tr ',' ' '); do
	create_user_and_database $db
	create_table $db
done
echo "Multiple databases created"
