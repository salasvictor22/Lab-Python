from interpreter import draw
from pieces import *
from picture import *

queen = Picture(QUEEN)
queens = queen.join(queen).join(queen).join(queen)
draw(queens.img)