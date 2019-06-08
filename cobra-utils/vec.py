class vec2:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    def __add__(self, other): return self.x + other.x, self.y + other.y
    def __sub__(self, other): return self.x - other.x, self.y - other.y
    def __mul__(self, other: float): return self.x * other, self.y * other
    def __div__(self, other: float): return self.x / other, self.y / other
    def __eq__(self, other) -> bool: return self.x == other.x and self.y == other.y
    def __ne__(self, other) -> bool: return (self == other) == False
    def __str__(self): return "({0:.4f}, {1:.4f})".format(self.x, self.y)
class vec3:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other): return self.x + other.x, self.y + other.y, self.z + other.z
    def __sub__(self, other): return self.x - other.x, self.y - other.y, self.z - other.z
    def __mul__(self, other: float): return self.x * other, self.y * other, self.z * other
    def __div__(self, other: float): return self.x / other, self.y / other, self.z / other
    def __eq__(self, other) -> bool: return self.x == other.x and self.y == other.y and self.z == other.z
    def __ne__(self, other) -> bool: return (self == other) == False
    def __str__(self): return "({0:.4f}, {1:.4f}, {2:.4f})".format(self.x, self.y, self.z)