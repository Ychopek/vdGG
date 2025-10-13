"""Описание: Реализуйте класс Rectangle с методами для вычисления площади и периметра. Дополнительно создайте метод для проверки, является ли прямоугольник квадратом.
Атрибут класса:
rectangles_quantity (количество созданных объектов этого класса)
Атрибуты:
width (ширина)
height (высота)
Методы:
area(): возвращает площадь.
perimeter(): возвращает периметр.
is_square(): возвращает True, если ширина равна высоте."""
class Rectangle:
    rectangle_quantity = 0
    @classmethod
    def increase_quantity(cls):
        cls.rectangle_quantity += 1
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.increase_quantity()
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def is_square(self):
        return self.width == self.height

rect = Rectangle(5, 10)
print(rect.area()) # 50
print(rect.perimeter()) # 30
print(rect.is_square()) # False