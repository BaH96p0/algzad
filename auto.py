class Auto:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def set_brand(self, brand):
        self.brand = brand

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_mileage(self, mileage):
        self.mileage = mileage

    def showcar(self):
        print(f'''
Марка машины: {self.brand}
Модель машины: {self.model}
Год выпуска: {self.year}
Пробег машины: {self.mileage}
''')


a = Auto('Hyndai', 'Tucson',2023, 10000)
print(a.showcar())
a.set_brand('Nissan')
a.set_model('Passat')
a.set_year(2008)
a.set_mileage(100000)
print(a.showcar())