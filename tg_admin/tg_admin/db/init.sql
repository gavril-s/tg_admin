CREATE TABLE IF NOT EXISTS messages(
    id UUID PRIMARY KEY,
    user_id UUID,
    from_chat_id BIGINT,
    to_chat_id BIGINT,
    sending_time TIMESTAMP DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS users(
    id BIGINT PRIMARY KEY,
    is_bot BOOLEAN,
    first_name VARCHAR(64),
    last_name VARCHAR(64) DEFAULT NULL,
    username VARCHAR(32) DEFAULT NULL,
    is_premium BOOLEAN DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS chats(
    id BIGINT PRIMARY KEY,
    chat_type VARCHAR(16),
    title VARCHAR(256) DEFAULT NULL,
    username VARCHAR(32) DEFAULT NULL,
    first_name VARCHAR(64),
    last_name VARCHAR(64) DEFAULT NULL
);