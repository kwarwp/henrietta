# henrietta.adda.main.py
from _spy.vitollino.main import Cena, STYLE

STYLE['width'] = 700

FrutosDaTerra = "https://i.imgur.com/FV4goWj.jpg"
Calcita = "https://i.imgur.com/biw6bwh.jpg"

class CenaFrutosDaTerra():
  def __init__(self):
    self.cena_f = Cena(img = FrutosDaTerra)
    self.cena_c = Cena(Calcita, direita=self.cena_f)
    self.cena_f = self.cena_c
    self.cena_f.meio = Cena(vai=self.vai_sul)

    self.cena_f.vai()
  def vai(self, *_):
    self.cena_f.vai()
  def vai_sul(self, *_):
    from kristen.main import go_cretaceo
    go_cretaceo()

def vai_CenaFrutosDaTerra():
  cena1 = CenaFrutosDaTerra()
  cena1.vai()

if __name__ == "__main__":
	vai_CenaFrutosDaTerra()
