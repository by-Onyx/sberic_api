DO
$$
    DECLARE
        user_id      INT;
        character_id INT;
    BEGIN
        insert into location (name, description, price, file_name, type)
        values ('ЧелГУ',
                'Такая лока крутая жесть ваще. А тут очень много разного текста нужно написать, чтоб посмотреть как будет обрезаться лишнее для слишком длинного текст, такого, как этот, например, или, может быть, любой другой настоящий или ненастоящий текст, текст-рыба, ну, в общем, вы поняли.',
                0, 'location.png', 'ground'),
               ('Рай',
                'Такая лока крутая жесть ваще. А тут очень много разного текста нужно написать, чтоб посмотреть как будет обрезаться лишнее для слишком длинного текст, такого, как этот, например, или, может быть, любой другой настоящий или ненастоящий текст, текст-рыба, ну, в общем, вы поняли.',
                0, 'heaven.jpg', 'ground'),
               ('Ад',
                'Такая лока крутая жесть ваще. А тут очень много разного текста нужно написать, чтоб посмотреть как будет обрезаться лишнее для слишком длинного текст, такого, как этот, например, или, может быть, любой другой настоящий или ненастоящий текст, текст-рыба, ну, в общем, вы поняли.',
                0, 'hell.jpeg', 'ground');

        insert into character (name, type, happiness_percent)
        values ('Sberic', 'gopher', 70)
        returning id into character_id;

        insert into clothes (name, description, price, file_name, type, x, y, width, height)
        values ('Шапка крутая пиратская', 'Шапка крутая пиратская шапка', 150.00, 'hat.png', 'hat', 50, 90, 250, 100),
               ('Шапка ковбойская', 'Шапка ковбойская', 150.00, 'hat_cowboy.png', 'hat', 50, 90, 250, 100),
               ('Шапка красная', 'Шапка красная', 150.00, 'hat_red.png', 'hat', 50, 90, 250, 100),
               ('Кофта зеленая', 'Кофта зеленая', 150.00, 'hoodie_green.png', 'hat', 50, 282, 174, 100),
               ('Кофта красная', 'Кофта красная', 150.00, 'hoodie_red.png', 'hat', 50, 282, 174, 100),
               ('Рубашка', 'Рубашка', 150.00, 'shirt_white.png', 'hat', 50, 282, 174, 100),
               ('Шарф красный', 'Шарф красный', 150.00, 'scarf_red.png', 'hat', 50, 270, 134, 110),
               ('Шарф зеленый', 'Шарф зеленый', 150.00, 'scarf_green.png', 'hat', 50, 270, 134, 110);

        insert into "user" (login, password, age, game_balance, real_balance, parent_id)
        values ('by_Onyx', 'password', 21, 5000, 5000, null)
        returning id into user_id;

        insert into user_character (user_id, character_id, is_active)
        values (user_id, character_id, true);

        insert into user_location (user_id, location_id, is_active)
        values (user_id, (select id from location where name = 'ЧелГУ'), true);

        insert into user_clothes (user_id, clothes_id)
        values (user_id, (select id from clothes where name = 'Шапка ковбойская')),
               (user_id, (select id from clothes where name = 'Шарф зеленый')),
               (user_id, (select id from clothes where name = 'Рубашка')),
               (user_id, (select id from clothes where name = 'Кофта красная'));

        insert into character_clothes (character_id, clothes_id)
        values (character_id, (select id from clothes where name = 'Шапка ковбойская')),
               (character_id, (select id from clothes where name = 'Рубашка'));
    END
$$;