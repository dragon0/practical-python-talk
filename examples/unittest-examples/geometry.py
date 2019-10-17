import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector2({self.x}, {self.y})".format(self=self)

    @staticmethod
    def from_angle(t):
        return Vector2(math.cos(t), math.sin(t))

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scale):
        return Vector2(self.x * scale, self.y * scale)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def direction(self):
        return math.atan2(self.y, self.x)

    def magnitude(self):
        return math.sqrt(self.magnitude_squared())

    def magnitude_squared(self):
        return self.x**2 + self.y**2

    def normalized(self):
        magnitude = self.magnitude()
        return Vector2(self.x/magnitude, self.y/magnitude)

