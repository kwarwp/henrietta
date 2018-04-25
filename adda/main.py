# henrietta.adda.main.py
from _spy.vitollino.main import Cena, STYLE

STYLE['width'] = 699

TutorialInterativo = "https://i.imgur.com/hVov95h.png"
Cena_direita = "https://i.imgur.com/D8KXmJs.png"
Cena_esquerda = "https://i.imgur.com/4hYhuEQ.png"

class CenaTutorialInterativo():
  def __init__(self):
    self.cena_t = Cena(img = TutorialInterativo)
    
    
    
    self.cena_t.meio = Cena(vai=self.vai_importar)
    self.cena_t.vai()
    
    self.cena_t.direita = Cena(vai=self.vai_direita)
    self.cena_t.vai()

class CenaEsquerda():
  def __init__(self):
    self.cena_e = Cena(img = Cena_esquerda)

class CenaDireita():
  def __init__(self):
    self.cena_d = Cena(img = Cena_direita)



  def vai(self, *_):
    self.cena_t.vai()
    
  def vai_importar(self, *_):
    from kristen.main import go_cretaceo
    go_cretaceo()
    
  def vai_esquerda(self, *_):
    CenaEsquerda()
    
  def vai_direita(self, *_):
    CenaDireita()
    
    
    
def vai_CenaTutorialInterativo():
  cenaImporta = CenaTutorialInterativo()
  cenaImporta.vai()

if __name__ == "__main__":
	vai_CenaTutorialInterativo()
    
    
    
def vai_CenaEsquerda():
  cenaEsq = CenaEsquerda()
  cenaEsq.vai()

if __name__ == "__main__":
	vai_CenaEsquerda() 
    
    
    
def vai_CenaDireita():
  cenaDir = CenaDireita()
  cenaDir.vai()

if __name__ == "__main__":
	vai_CenaDireita()     
