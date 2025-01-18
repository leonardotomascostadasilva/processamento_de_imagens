-- Active: 1737229134443@@127.0.0.1@5432@mydatabase
CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    image_data BYTEA,
    context TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
