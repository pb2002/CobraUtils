from math import cos, sin, atan, e
class mat:
    @staticmethod
    def cartesian_to_polar(x: float, y: float) -> tuple: return ((x ** 2 + y ** 2) ** 0.5, atan(y/x))
    @staticmethod
    def polar_to_cartesian(r: float, theta: float) -> tuple: return (r * cos(theta), r * sin(theta))
    class complex:
        @staticmethod
        def fromPolar(r, theta) -> complex: return complex(r * cos(theta), r * sin(theta))
        @staticmethod
        def sin(z: complex) -> complex: return complex((sin(z.a) / 2) * (e ** -z.b + e ** z.b), -(cos(z.a) / 2) * (e ** -z.b + e ** z.b))
        def __init__(self, a, b):
            self.a = a
            self.b = b
        def __add__(self, o): return self.a + o.a, self.b + o.b
        def __sub__(self, o): return self.a - o.a, self.b - o.b
        def __mul__(self, o): return self.a * o.a - self.b * o.b, self.a * o.b + self.b * o.a