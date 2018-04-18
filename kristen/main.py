# henrietta.kristen.main.py
from _spy.vitollino.main import Cena, STYLE

STYLE['width'] = 700

cretaceo_n = "https://i.imgur.com/EwPWbms.jpg"

class Cena1():
  def __init__(self):
    #from meredith.main import Cena2
    self.cena1 = Cena(img = cretaceo_n)
    #cena2 = Cena2()
    #self.cena1.direita = cena2

    self.cena1.vai()
  def vai(self, *_):
    self.cena1.vai()

def Game():
  cena1 = Cena1()
  cena1.vai()

if __name__ == "__main__":
	Game()
