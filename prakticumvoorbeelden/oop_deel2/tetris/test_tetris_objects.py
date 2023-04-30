#!/usr/bin/env python

from tetris_objects import Figure
from random import randrange
import logging
import numpy as np

logging.basicConfig(level=logging.INFO, filename="log.txt")
logging.info("Loglevel is info")

# Random Red Green Blue Color
color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

# Block
shape = np.array([(0, -1), (-1, -1), (-1, 0), (0, 0)])

# Create block object from class Figure
block = Figure(shape, color)

logging.debug(f"block color : {block.getColor()}")
logging.debug(f"block shape :  {block.getShape()}")

# iBlock

# Shape of iBlock
shape = np.array([(-1, 0), (-2, 0), (0, 0), (1, 0)])

# Random Red Green Blue Color
color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

iBlock = Figure(shape, color)

logging.debug(f"iBlock color : {iBlock.getColor()}")
logging.debug(f"iBlock shape :  {iBlock.getShape()}")

logging.debug("Rotate counterclockwise")
iBlock.rotate()

logging.debug(f"iBlock color : {iBlock.getColor()}")
logging.debug(f"iBlock shape :  {iBlock.getShape()}")

shape = np.array(
    [(-1, 0), (-1, 1), (0, 0), (0, -1)],
)
zShape = Figure(shape, color)
zShape.rotate()
