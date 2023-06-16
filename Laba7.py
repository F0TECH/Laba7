import math
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def resize(self, factor):
        self.width *= factor
        self.height *= factor

    def rotate(self, angle):
        # будем считать, что угол задан в градусах
        # реализация метода зависит от конкретной фигуры
        pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def rotate(self, angle):
        # круг не может вращаться, поэтому этот метод будет просто игноририрует угол
        pass

    def __str__(self):
        return f"Круг в центре ({self.x}, {self.y}), радиус {self.radius}"


class Square(Shape):
    def __init__(self, x, y, size):
        super().__init__(x, y)
        self.width = self.height = size

    def rotate(self, angle):
        # квадрат всегда остается квадратом при повороте, поэтому этот метод также игнорирует угол
        pass

    def __str__(self):
        return f"Квадрат с левым верхним углом в точке ({self.x}, {self.y}), размер {self.width}"


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def rotate(self, angle):
        # поворот прямоугольника на угол angle вокруг его центра
        x0, y0 = self.x, self.y
        angle = math.radians(angle)
        cos = math.cos(angle)
        sin = math.sin(angle)

        x1 = x0 + (self.width / 2) * cos - (self.height / 2) * sin
        y1 = y0 - (self.width / 2) * sin - (self.height / 2) * cos

        x2 = x0 - (self.width / 2) * cos - (self.height / 2) * sin
        y2 = y0 + (self.width / 2) * sin - (self.height / 2) * cos

        x3 = 2 * x0 - x1
        y3 = 2 * y0 - y1

        self.x, self.y = x0, y0
        self.width = round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 2)
        self.height = round(math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2), 2)

    def __str__(self):
        return f"Прямоугольник с левым верхним углом в точке ({self.x}, {self.y}), ширина {self.width}, высота {self.height}"
# создаем объекты
circle = Circle(0, 0, 5)
square = Square(10, 10, 5)
rectangle = Rectangle(20, 20, 8, 5)

# перемещаем и изменяем размеры
circle.move(3, 3)
square.resize(2)
rectangle.move(-5, 5)
rectangle.resize(0)