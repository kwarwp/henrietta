# henrietta.anastasia.main.py
from _spy.vitollino.main import Cena, STYLE

STYLE['width'] = 700

gueravoa = "https://i.imgur.com/EbrxU7f.jpg"
amazonsaurocabeca =  "https://i.imgur.com/2veboeq.jpg"
dinossaurope = "https://i.imgur.com/nPjxpDC.jpg"
libelula = "https://i.imgur.com/lDnfrx8.jpg"

class CenaAnhanguera():
  def __init__(self):
    self.cenavoa = Cena(img = gueravoa)
    self.cenacabeca = Cena(amazonsaurocabeca, direita=self.cenavoa)
    self.cenasaurope = Cena(dinossaurope, direita=self.cenacabeca)
    self.cenalibelula = Cena(libelula, direita=self.cenasaurope, esquerda = self.cenavoa)
    self.cenavoa.esquerda = self.cenacabeca
    self.cenavoa.direita = self.cenalibelula
    
    self.cenavoa.vai()
  def vai(self, *_):
    self.cenavoa.vai()
    
def go_anhanguera():
  cena_Anhanguera = CenaAnhanguera()
  cena_Anhaguera.vai()

if __name__ == "__main__":
	go_anhaguera()


    


