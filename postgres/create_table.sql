
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
