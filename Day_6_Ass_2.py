pi = 3.14

class Cone:

    def __init__(self, radius, height):
        self.r = radius
        self.h = radius

    def calculate_volume(self):
        volume = (pi * self.r**2) * (self.h/3)
        print(f"Volume of the cone is {volume:.2f} cubic units.")

    def calculate_surface_area(self):
        base = (pi * self.r**2)
        side = pi * self.r * (self.r**2 + self.h**2)**(0.5)
        surface_area = base + side
        print(f"Surface area of the cone is {surface_area:.2f} square units.")

cone_obj = Cone(4, 7)
cone_obj.calculate_volume()
cone_obj.calculate_surface_area()