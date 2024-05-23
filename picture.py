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
    """ Devuelve el espejo vertical de la imagen """
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
    return Picture(None)

  def join(self, p):
    max_height = max(len(self.img), len(p.img))
    img1 = self.img + [''] * (max_height - len(self.img))
    img2 = p.img + [''] * (max_height - len(p.img))
    joined_img = [line1 + line2 for line1, line2 in zip(img1, img2)]
    return Picture(joined_img)

  def up(self, p):
    joined_img = self.img + p.img
    return Picture(joined_img)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

