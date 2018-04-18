# henrietta.adda.main.py
from _spy.vitollino.main import Cena, STYLE

STYLE['width'] = 700
#colocar as imagens 
frutosDaTerra_n = "http://bit.ly/2FOvGTr"
#cretaceo_n = "https://i.imgur.com/EwPWbms.jpg"
#cretaceo_o = "https://i.imgur.com/c9lK8Vm.jpg"
#cretaceo_s = "https://i.imgur.com/QFLIccY.jpg"
#cretaceo_l = "https://i.imgur.com/K1LChZw.jpg"

class CenaCretaceo():
  def __init__(self):
    #from meredith.main import Cena2
    self.cena_n = Cena(img = frutosDaTerra_n)
    self.cena_o = Cena(cretaceo_o, direita=self.cena_n)
    self.cena_s  = Cena(cretaceo_s, direita=self.cena_o)
    self.cena_l  = Cena(cretaceo_l, direita=self.cena_s,
    esquerda = self.cena_n)
    self.cena_n.esquerda = self.cena_o
    self.cena_o.esquerda = self.cena_s
    self.cena_s.esquerda = self.cena_l
    #cena2 = Cena2()
    #self.cena1.direita = cena2

    self.cena_n.vai()
  def vai(self, *_):
    self.cena_n.vai()

def Game():
  cena1 = CenaCretaceo()
  cena1.vai()

if __name__ == "__main__":
	Game()
