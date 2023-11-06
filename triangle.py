class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def tr_type(self):
        if self.side1 == self.side2 == self.side3:
            print('Треугольник равносторонний')
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            print('Треугольник равнобедренный')
        else:
            print('Треугольник разносторонний')

    def tr_square(self):
        p = (self.side1+self.side2+self.side3)/2
        x = (p*(p-self.side1) * (p - self.side2) * (p - self.side3))**0.5
        return x


t = Triangle(3,9,4)
print(t.tr_type())
print(t.tr_square())





