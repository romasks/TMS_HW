import math

class Sphere:
    def __init__(self, r=None, x=None, y=None, z=None) -> None:
        self.r = 1 if r == None else r
        self.x = 0 if x == None else x
        self.y = 0 if x == None else y
        self.z = 0 if x == None else z

    def __str__(self) -> str:
        return f"radius = {self.r}, position = ({self.x}, {self.y}, {self.z})"
    
    def get_volume(self) -> float:
        return (4.0 / 3) * math.pi * (self.r ** 3) 
    
    def get_square(self) -> float:
        return 4 * math.pi * (self.r ** 2) 
    
    def get_radius(self) -> int:
        return self.r
    
    def get_center(self) -> tuple:
        return (self.x, self.y, self.z)
    
    def set_radius(self, radius) -> None:
        self.r = radius
    
    def set_center(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def is_point_inside(self, x, y, z) -> bool:
        return (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2 < (self.r ** 2)

sphere1 = Sphere()
print(sphere1)

sphere2 = Sphere(3)
print(sphere2)

sphere3 = Sphere(4, 5, 6, 7)
print(sphere3)

point = (2, 1, 1)
is_point_inside = sphere2.is_point_inside(*point)
print(f"Is point {point} inside sphere: {is_point_inside}")
