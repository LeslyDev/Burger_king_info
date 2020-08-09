# Burger_king_info_
shows all competitors (kfc) of each burger king restaurant in moscow

Инструкция по запуску:

    Из корневой папки с проектом!

        1. docker-compose build
        2. docker-compose up
        3. docker-compose run web python /code/manage.py migrate --noinput
        4. docker-compose run web python /code/manage.py loaddata fixture_bk_rest.json
        5. docker-compose run web python /code/manage.py loaddata fixture_kfc_rest.json
