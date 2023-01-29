CREATE TABLE IF NOT EXISTS users(
    id UUID PRIMARY KEY,
    tg_id BIGINT,
    tg_username VARCHAR(32)
);