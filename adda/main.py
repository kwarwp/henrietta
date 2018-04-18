# henrietta.adda.main.py
from _spy.vitollino.main import Cena, STYLE

STYLE['width'] = 700

cretaceo_s = "https://imgur.com/FV4goWj"
cretaceo_o = "https://imgur.com/FV4goWj"
cretaceo_n = "https://imgur.com/FV4goWj"
cretaceo_l = "https://imgur.com/FV4goWj"

class CenaCretaceo():
  def __init__(self):
    self.cena_n = Cena(img = cretaceo_n)
    self.cena_o = Cena(cretaceo_o, direita=self.cena_n)
    self.cena_s  = Cena(cretaceo_s, direita=self.cena_o)
    self.cena_l  = Cena(cretaceo_l, direita=self.cena_s,
    esquerda = self.cena_n)
    self.cena_n.esquerda = self.cena_o
    self.cena_n.direita = self.cena_l
    self.cena_o.esquerda = self.cena_s
    self.cena_s.esquerda = self.cena_l
    #cena2 = Cena2()
    #self.cena1.direita = cena2

    self.cena_n.vai()
  def vai(self, *_):
    self.cena_n.vai()
  def vai_sul(self, *_):
    from anastasia.main import CenaAnhanguera
    CenaAnhanguera().vai()

def Game():
  cena1 = CenaCretaceo()
  cena1.vai()

if __name__ == "__main__":
	Game()
