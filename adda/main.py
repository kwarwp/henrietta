# henrietta.adda.main.py
from _spy.vitollino.main import Cena, STYLE

#STYLE['width'] = 700

#cretaceo_s = "https://i.imgur.com/FV4goWj.jpg"
#cretaceo_o = "https://i.imgur.com/FV4goWj.jpg"
FrutosDaTerra = "https://i.imgur.com/FV4goWj.jpg"
Calcita = "https://i.imgur.com/biw6bwh.jpg"

class CenaFrutosDaTerra():
  def __init__(self):
    self.cena_f = Cena(img = FrutosDaTerra)
    self.cena_c = Cena(Calcita, direita=self.cena_f)
    self.cena_s  = Cena(cretaceo_s, direita=self.cena_o)
    #self.cena_l  = Cena(cretaceo_l, direita=self.cena_s,
    #esquerda = self.cena_n)
    self.cena_f = self.cena_c
    self.cena_s.meio = Cena(vai=self.vai_sul)
    #self.cena_n.direita = self.cena_l
    #self.cena_o.esquerda = self.cena_s
    #self.cena_s.esquerda = self.cena_l
    #cena2 = Cena2()
    #self.cena1.direita = cena2

    self.cena_f.vai()
  def vai(self, *_):
    self.cena_f.vai()
  def vai_sul(self, *_):
    from anastasia.main import CenaAnhanguera
    CenaAnhanguera().vai()

def vai_CenaFrutosDaTerra():
  cena1 = CenaFrutosDaTerra()
  cena1.vai()

if __name__ == "__main__":
	vai_CenaFrutosDaTerra()
