# Burger_king_info_
shows all competitors (kfc) of each burger king restaurant in moscow

Инструкция по запуску:
    Из корневой папки с проектом!
        
        1. docker-compose build
        2. docker-compose up
        3. docker-compose run web python /code/manage.py migrate --noinput
        4. docker-compose run web python /code/manage.py loaddata fixture_bk_rest.json
        5. docker-compose run web python /code/manage.py loaddata fixture_kfc_rest.json

В результатете по пути list_of_restaurants/ можно увидеть все рестораны бургер кинг Москвы, где для каждого есть адрес и количество ресторанов KFC в радиусе 2км
kfc_rest_info.json - файл с полной информацией обо всех ресторанах kfc
bk_parser.py - парсит страницу со всеми ресторанами бургер кинг, выбирает только те, которые находятся в Москве и возвращает json фикстуру
kfc_parser.py - парсит страницу со всеми ресторанами kfc, выбирает только те, которые находятся в Москве и возвращает json фикстуру
Фикстуры созданы заранее, поэтому файлы bk_parser.py и kfc_parser.py в ходе выполнения программы не вызываются и находятся в директории проекта для того, чтобы показать как создавались фикстуры.
