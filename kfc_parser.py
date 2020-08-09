import re


def create_kfc_fixture():
    with open('kfc_rest_info.json') as list_file:
        a = list_file.readline()
        counter = 1
        c = re.findall(r'\{"store".+?"city":\{"en":"Moscow","ru":"Москва и МО"}.+?"coordinates":\[(.+?)\].+?"distanceMeters":.+?}', a)
    with open('fixture_kfc_rest.txt', 'w') as fix:
        for i in c:
            t = i.split(',')
            some_string = '{"pk": %s, "model": "rest_info.restaurantkfc", ' \
                          '"fields": {"some_id": %s, "latitude": %s, ' \
                          '"longitude":' \
                          ' %s}}, \n' % (counter, counter, t[0], t[1])
            counter += 1
            fix.write(some_string)


create_kfc_fixture()
