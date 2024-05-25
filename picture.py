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
    """Devuelve el espejo vertical de la imagen"""
    vertical = []
    for value in reversed(self.img):
        vertical.append(value)
    return Picture(vertical)

  def horizontalMirror(self):
    """Devuelve el espejo horizontal de la imagen"""
    horizontal = []
    for line in self.img:
      horizontal.append(line[::-1])
    return Picture(horizontal)

  def negative(self):
    """Devuelve un negativo de la imagen"""
    self.img = [''.join([self._invColor(char) for char in line]) for line in self.img]
    return self

  def join(self, p):
    """Devuelve una nueva figura poniendo la figura del argumento al lado derecho de la figura actual"""
    joined_img = [line1 + line2 for line1, line2 in zip(self.img, p.img)]
    return Picture(joined_img)
   
  def up(self, p):
    """Devuelve una nueva figura poniendo la figura recibida como argumento, encima de la figura actual"""
    joined_img = self.img + p.img
    return Picture(joined_img)

  def under(self, p):
    """"Devuelve una nueva figura poniendo la figura recibida como argumento, sobre la figura actual"""
    combined_img = []
    for line_self, line_p in zip(self.img, p.img):
        combined_line = ''.join(char_p if char_p != ' ' else char_self for char_self, char_p in zip(line_self, line_p))
        combined_img.append(combined_line)
    return Picture(combined_img)
  
  def horizontalRepeat(self, n):
    """Devuelve una nueva figura repitiendo la figura actual al costado la cantidad de veces que indique el valor de n"""
    repeated_img = [''.join([line] * n) for line in self.img]
    return Picture(repeated_img)

  def verticalRepeat(self, n):
    """verticalRepeat Devuelve una nueva figura repitiendo la figura actual debajo, la cantidad de veces que indique el valor de n"""
    repeated_img = self.img * n
    return Picture(repeated_img)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

