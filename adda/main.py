# henrietta.adda.main.py
from _spy.vitollino.main import Cena, STYLE

STYLE['width'] = 699

TutorialInterativo = "https://i.imgur.com/hVov95h.png"
Cena_direita = "https://i.imgur.com/D8KXmJs.png"
Cena_esquerda = "https://i.imgur.com/4hYhuEQ.png"

class CenaTutorialInterativo():
  def __init__(self):
    self.cena_t = Cena(img = TutorialInterativo)
    
    self.cena_t.esquerda = Cena(vai=self.vai_esquerda)
    self.cena_e.vai()
    
    self.cena_t.meio = Cena(vai=self.vai_importar)
    self.cena_t.vai()
    
    self.cena_t.direita = Cena(vai=self.vai_direita)
    self.cena_d.vai()
    
  def vai(self, *_):
    self.cena_t.vai()
    
    self.cena_e = Cena(Cena_esquerda, esquerda=self.cena_t)
    self.cena_t = self.cena_e
    
    self.cena_d = Cena(Cena_direita, direita=self.cena_t)
    self.cena_t = self.cena_d
    
  def vai_esquerda(self, *_):
    vai()
    
  def vai_importar(self, *_):
    from kristen.main import go_cretaceo
    go_cretaceo()

  def vai_direita(self, *_):
    vai()
    
def vai_CenaTutorialInterativo():
  cenaImporta = CenaTutorialInterativo()
  cenaImporta.vai()

if __name__ == "__main__":
	vai_CenaTutorialInterativo()
