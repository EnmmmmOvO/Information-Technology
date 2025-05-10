-- USERS = {
--     "HamishWHC": {
--         "role": "user",
--         "password": "$argon2id$v=19$m=65536,t=3,p=4$14gM9oLtre3L4bQ0S/7BDQ$SjXIF2XWwef+EY2LQZRZLwBKbLZLplqFLcPpKMD0vew",
--     },
--     "ssparrow4": {
--         "role": "user",
--         "password": "$argon2id$v=19$m=65536,t=3,p=4$14gM9oLtre3L4bQ0S/7BDQ$SjXIF2XWwef+EY2LQZRZLwBKbLZLplqFLcPpKMD0vew",
--     },
--     "TrashPanda": {
--         "role": "user",
--         "password": "$argon2id$v=19$m=65536,t=3,p=4$14gM9oLtre3L4bQ0S/7BDQ$SjXIF2XWwef+EY2LQZRZLwBKbLZLplqFLcPpKMD0vew",
--     },
--     "admin": {
--         "role": "user",
--         "password": "$argon2id$v=19$m=65536,t=3,p=4$14gM9oLtre3L4bQ0S/7BDQ$SjXIF2XWwef+EY2LQZRZLwBKbLZLplqFLcPpKMD0vew",
--     },
-- }

CREATE TABLE users (
    username TEXT, 
    role TEXT, 
    password TEXT
);

INSERT INTO users VALUES (
    "admin", 
    "user",
    "$argon2id$v=19$m=65536,t=3,p=4$14gM9oLtre3L4bQ0S/7BDQ$SjXIF2XWwef+EY2LQZRZLwBKbLZLplqFLcPpKMD0vew"
);

INSERT INTO users VALUES (
    "ssparrow4", 
    "user",
    "$argon2id$v=19$m=65536,t=3,p=4$14gM9oLtre3L4bQ0S/7BDQ$SjXIF2XWwef+EY2LQZRZLwBKbLZLplqFLcPpKMD0vew"
); 

INSERT INTO users VALUES (
    "TrashPanda", 
    "admin",
    "$argon2id$v=19$m=65536,t=3,p=4$14gM9oLtre3L4bQ0S/7BDQ$SjXIF2XWwef+EY2LQZRZLwBKbLZLplqFLcPpKMD0vew"
); 

INSERT INTO users VALUES (
    "HamishWHC", 
    "admin",
    "$argon2id$v=19$m=65536,t=3,p=4$14gM9oLtre3L4bQ0S/7BDQ$SjXIF2XWwef+EY2LQZRZLwBKbLZLplqFLcPpKMD0vew"
); 