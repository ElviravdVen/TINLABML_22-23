from abc import ABC, abstractmethod
import math


# Abstraction: Abstract Superclass
class Shape(ABC):
    # Constructor method with Arguments/Parameters
    def __init__(self, width, height=1, colorArg="black"):
        # Attributes
        self.width = width
        self.height = height
        self.color = colorArg

        if colorArg is not None:
            self.setColor(colorArg)

    def setColor(self, colorArg):
        self.color = colorArg

    def getArea(self):
        return self.area

    def getColor(self):
        return self.color

    # Operator Overloading
    # to enable addition of Shapes by area
    def __add__(self, other):
        return self.getArea() + other.getArea()

    # # Operator Overloading
    # # to enable the comparison of shapes
    # def __eq__(self, other):
    #     return self.getArea() == other.getArea() and self.getColor() == other.getColor()


# Constructor
# Starts with Double Underscore -> dunder methods
class Rectangle(Shape):
    # Indent
    # DocString to document the purpose
    """
    This class can be used to generate Rectangle Objects
    with arguments
    width and height
    """

    # Default arguments always last
    def __init__(self, widthArg, heightArg, colorArg="blue"):
        """_summary_"""
        # Attributes
        # Encapsulated in object
        self.width = widthArg
        self.height = heightArg
        self.area = round(self.width * self.height)
        self.color = colorArg


# Each class inherits from Rectangle
class Box(Rectangle):
    def __init__(self, widthArg, heightArg, depthArg):
        super().__init__(widthArg, heightArg)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.area = self.base * self.height * 0.5
