from interpreter import draw
from pieces import *
from picture import *

square = Picture(SQUARE)
square2 = Picture(SQUARE).negative()
line = square.join(square2).horizontalRepeat(4)
line2 = square.join(square2).horizontalRepeat(4).horizontalMirror()
line3 = line.up(line2).verticalRepeat(2)
draw(line3.img)