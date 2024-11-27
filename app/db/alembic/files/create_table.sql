create type character_enum as enum ('gopher');

create type clothes_enum as enum ('hat', 'shirt', 'scarf');

create type location_enum as enum ('ground', 'underwater', 'aerial', 'space');

create type transaction_enum as enum ('replenishment', 'purchase', 'withdrawal');

create table character
(
    id                serial
        primary key,
    name              text           not null
        unique,
    type              character_enum not null,
    happiness_percent integer        not null
);

create table clothes
(
    id          serial
        primary key,
    name        text           not null,
    description text           not null,
    price       numeric(10, 2) not null,
    file_name   text           not null
        unique,
    type        clothes_enum   not null,
    x           numeric(7, 2)  not null,
    y           numeric(7, 2)  not null,
    width       numeric(7, 2)  not null,
    height      numeric(7, 2)  not null
);

create table location
(
    id          serial
        primary key,
    name        text           not null
        unique,
    description text           not null,
    price       numeric(10, 2) not null,
    file_name   text           not null
        unique,
    type        location_enum  not null
);

create table "user"
(
    id            serial
        primary key,
    login         text                                not null
        unique,
    password      text                                not null,
    age           smallint                            not null,
    game_balance  numeric(10, 2)                      not null,
    real_balance  numeric(10, 2)                      not null,
    creation_date timestamp default CURRENT_TIMESTAMP not null,
    parent_id     integer
                                                      references "user"
                                                          on delete set null
);

create table purpose
(
    id          serial
        primary key,
    name        text           not null,
    user_id     integer        not null
        references "user"
            on delete cascade,
    price       numeric(10, 2) not null,
    accumulated numeric(10, 2) not null,
    is_complete boolean        not null
);

create table character_clothes
(
    character_id integer not null
        references character
            on delete cascade,
    clothes_id   integer not null
        references clothes
            on delete cascade,
    primary key (character_id, clothes_id)
);

create table user_character
(
    user_id      integer not null
        references "user"
            on delete cascade,
    character_id integer not null
        references character
            on delete cascade,
    is_active    boolean not null,
    primary key (user_id, character_id)
);

create table user_clothes
(
    user_id    integer not null
        references "user"
            on delete cascade,
    clothes_id integer not null
        references clothes
            on delete cascade,
    primary key (user_id, clothes_id)
);

create table user_location
(
    user_id     integer not null
        references "user"
            on delete cascade,
    location_id integer not null
        references location
            on delete cascade,
    is_active   boolean not null,
    primary key (user_id, location_id)
);

create table user_transactions
(
    id              serial
        primary key,
    user_id         integer
                                                        references "user"
                                                            on delete set null,
    transfer_amount numeric(10, 2)                      not null,
    type            transaction_enum                    not null,
    datetime        timestamp default CURRENT_TIMESTAMP not null
);