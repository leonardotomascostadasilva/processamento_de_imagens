CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    image_data BYTEA,
    context TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);