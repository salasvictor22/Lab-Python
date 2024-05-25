from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    vertical = []
    for value in reversed(self.img):
        vertical.append(value)
    return Picture(vertical)

  def horizontalMirror(self):
    horizontal = []
    for line in self.img:
      horizontal.append(line[::-1])
    return Picture(horizontal)

  def negative(self):
    self.img = [''.join([self._invColor(char) for char in line]) for line in self.img]
    return self

  def join(self, p):
    joined_img = [line1 + line2 for line1, line2 in zip(self.img, p.img)]
    return Picture(joined_img)
   
  def up(self, p):
    joined_img = self.img + p.img
    return Picture(joined_img)

  def under(self, p):
    combined_img = []
    for line_self, line_p in zip(self.img, p.img):
        combined_line = ''.join(char_p if char_p != ' ' else char_self for char_self, char_p in zip(line_self, line_p))
        combined_img.append(combined_line)
    return Picture(combined_img)
  
  def horizontalRepeat(self, n):
    repeated_img = [''.join([line] * n) for line in self.img]
    return Picture(repeated_img)

  def verticalRepeat(self, n):
    repeated_img = self.img * n
    return Picture(repeated_img)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

