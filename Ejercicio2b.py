from interpreter import draw
from pieces import *
from picture import *

knight = Picture(KNIGHT)
knight_Black = Picture(KNIGHT).negative()
combined_knights = knight.join(knight_Black)
combined_knights2 = knight_Black.join(knight).horizontalMirror()
image = combined_knights.up(combined_knights2)
draw(image.img)
