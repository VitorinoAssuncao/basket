
DROP TABLE IF EXISTS "public"."users";

CREATE SEQUENCE IF NOT EXISTS users_users_id_seq

CREATE TABLE "public"."users" (
    "user_id" int4 NOT NULL DEFAULT nextval('users_users_id_seq'::regclass),
    "user_name" text,
    "user_login" text NOT NULL,
    "user_password" varchar NOT NULL,
    "user_email" text NOT NULL,
    PRIMARY KEY ("user_id")
);

DROP TABLE IF EXISTS "public"."games";

CREATE SEQUENCE IF NOT EXISTS games_game_id_seq

CREATE TABLE "public"."games" (
    "game_id" int4 NOT NULL DEFAULT nextval('games_game_id_seq'::regclass),
    "game_user_id" int8,
    "game_number" int8,
    "game_seasson" int8,
    "game_points" int8,
    PRIMARY KEY ("game_id")
);