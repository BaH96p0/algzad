class Rechtangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def recht_info(self):
        print(f'''
Длина прямоугльника: {self.length}
Ширина прямоугльника: {self.width}
''')


    def square_n_perimeter(self):
        print(f'''
Периметр треугольника: {self.length + self.width * 2}
Площадь треугольника: {self.length * self.width}
''')


r = Rechtangle(5, 4)
print(r.recht_info())
print(r.square_n_perimeter())
