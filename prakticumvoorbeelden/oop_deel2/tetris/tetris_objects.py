import numpy as np
from pygame import Rect

"""
Classnames always UpperCamelCase
"""


class Figure:
    # Constructor method
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    # Returns attribute color
    def getColor(self):
        return self.color

    """
    Returns Shape in Object Coordinates
    as Numpy Array
    """

    def getShape(self):
        return self.shape

    # Change shape by multiplying with Numpy Array
    # self.shape gets new shape
    # Counter clockwise
    def rotate(self):
        self.shape = np.rot90(self.shape, 1, axes=(1, 0))

    # # Return Pygame Rect
    # # https://www.pygame.org/docs/ref/rect.html
    # def getRect(self):
    #     Rect(left, top, width, height)
