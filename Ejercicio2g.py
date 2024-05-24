from interpreter import draw
from pieces import *
from picture import *

""""creacion de las fichas"""
square = Picture(SQUARE)
bishop = Picture(BISHOP)
king = Picture(KING)
knight = Picture(KNIGHT)
pawn = Picture(PAWN)
queen = Picture(QUEEN)
rock = Picture(ROCK)
square2 = Picture(SQUARE).negative()
bishop2 = Picture(BISHOP).negative()
king2 = Picture(KING).negative()
knight2 = Picture(KNIGHT).negative()
pawn2 = Picture(PAWN).negative()
queen2 = Picture(QUEEN).negative()
rock2 = Picture(ROCK).negative()

"""fichas superpuestas en los casilleros"""
f1 = square.under(rock2)
f2 = square2.under(knight2)
f3 = square.under(bishop2)
f4 = square2.under(queen2)
f5 = square.under(king2)
f6 = square.under(pawn).negative()
f7 = square2.under(pawn).negative()
f8 = square.under(rock).negative()
f9 = square2.under(knight).negative()
f10 = square.under(bishop).negative()

"""tablero"""
line1 = f1.join(f2).join(f3).join(f4).join(f5).join(f10).join(f9).join(f8)
line2 = f6.join(f7).horizontalRepeat(4)
line3 = square.join(square2).horizontalRepeat(4)
line4 = square.join(square2).horizontalRepeat(4).negative()
line5 = line3.up(line4).verticalRepeat(2)
line6 = f6.join(f7).horizontalRepeat(4).negative()
line7 = f1.join(f2).join(f3).join(f4).join(f5).join(f10).join(f9).join(f8).negative()
tablero = line1.up(line2).up(line5).up(line6).up(line7)

draw(tablero.img)