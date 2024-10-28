insert into transaction_type (id, name)
values (1, 'Replenishment'),
       (2, 'Purchase'),
       (3, 'Withdrawal');

insert into location_type (id, name)
values (1, 'Ground'),
       (2, 'Underwater'),
       (3, 'Aerial'),
       (4, 'Space');

insert into character_type (id, name)
values (1, 'Gopher');

insert into clothes_type (id, name)
values (1, 'Hat'),
       (2, 'Shirt'),
       (3, 'Pants');

insert into location (id, name, price, file_name, type_id)
values (1, 'Base', 0, 'base_location.jpg', 1);

insert into character (id, name, character_type_id, happiness_percent)
values (1, 'Sberic', 1, 70);

insert into clothes (id, name, price, file_name, clothes_type_id)
values (1, 'Base hat', 150.00, 'base_hat.jpg', 1),
       (2, 'Base shirt', 499.99, 'base_shirt.jpg', 2),
       (3, 'Base pants', 235.99, 'base_pants.jpg', 3);

insert into "user" (id, login, password, age, balance)
values (1, 'by_Onyx', '', 21, 4114.02);

insert into user_character (user_id, character_id)
values (1, 1);

insert into user_location (user_id, location_id)
values (1, 1);

insert into user_clothes (user_id, clothes_id)
values (1, 1),
       (1, 2),
       (1, 3);

insert into character_clothes (character_id, clothes_id)
values (1, 1),
       (1, 2),
       (1, 3);

insert into user_transactions (id, user_id, transfer_amount, transaction_type_id, datetime)
values (1, 1, 5000, 1, now() - INTERVAL '5 minute'),
       (2, 1, 150.00, 2, now() - INTERVAL '2 minute'),
       (3, 1, 499.99, 2, now() - INTERVAL '1 minute'),
       (4, 1, 235.99, 2, now());