from interpreter import draw
from pieces import *
from picture import *


knight = Picture(KNIGHT)
knight_Black = Picture(KNIGHT)
knight_Black.negative()

combined_knights = knight.join(knight_Black)
draw(combined_knights.img)


