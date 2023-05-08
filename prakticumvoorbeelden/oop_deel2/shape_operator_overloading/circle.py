# Import Abstract Base Class Shape
# from package shapes
import math
from shapes import Shape

color = "black"


class Circle(Shape):
    """
    This class inherits from Shape and can be used
    to generate Circle objects
    Arguments: radius
    """

    def __init__(self, radius, color):
        super().__init__(radius)
        self.radius = radius
        self.area = math.pow(self.radius, 2) * 0.5 * math.pi
        self.setColor(color)

    def getRadius(self):
        return self.radius

    # Zijn twee circle objecten hetzelfde?
    def __ne__(self, other):
        return (
            self.getColor() != other.getColor() or self.getRadius() != other.getRadius()
        )
