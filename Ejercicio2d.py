from interpreter import draw
from pieces import *
from picture import *

square = Picture(SQUARE)
square2 = Picture(SQUARE)
square2.negative()
squares = square.join(square2).horizontalRepeat(4)
draw(squares.img)