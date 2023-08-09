DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email_address text
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    view_count int,
    user_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);

INSERT INTO users (username, email_address) VALUES ('Test username 1', 'Test email address 1');
INSERT INTO users (username, email_address) VALUES ('Test username 2', 'Test email address 2');
INSERT INTO users (username, email_address) VALUES ('Test username 3', 'Test email address 3');
INSERT INTO users (username, email_address) VALUES ('Test username 4', 'Test email address 4');

INSERT INTO posts (title, content, view_count, user_id) VALUES ('Test title 1', 'Test content 1', 8, 1);
INSERT INTO posts (title, content, view_count, user_id) VALUES ('Test title 2', 'Test content 2', 7, 1);
INSERT INTO posts (title, content, view_count, user_id) VALUES ('Test title 3', 'Test content 3', 6, 2);
INSERT INTO posts (title, content, view_count, user_id) VALUES ('Test title 4', 'Test content 4', 5, 2);
INSERT INTO posts (title, content, view_count, user_id) VALUES ('Test title 5', 'Test content 5', 4, 3);
INSERT INTO posts (title, content, view_count, user_id) VALUES ('Test title 6', 'Test content 6', 3, 3);
INSERT INTO posts (title, content, view_count, user_id) VALUES ('Test title 7', 'Test content 7', 2, 4);
INSERT INTO posts (title, content, view_count, user_id) VALUES ('Test title 8', 'Test content 8', 1, 4);
