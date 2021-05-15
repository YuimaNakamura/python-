class Country:

    def __init__(self, country_name):
        self.country_name = country_name


class City(Country):

    def __init__(self, country_name, city_name):
        super().__init__(country_name)
        self.city_name = city_name


classes = []
classes.append(City('Japan', 'Tokyo'))
classes.append(City('USA', 'Washington, D.C.'))

for test_cls in classes:
    print('===== Class =====')
    print('country_name --> ' + test_cls.country_name)
    print('city_name --> ' + test_cls.city_name)
