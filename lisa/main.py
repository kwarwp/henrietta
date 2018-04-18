# henrietta.lisa.main.py
from _spy.vitollino.main import Cena, STYLE

STYLE ['width'] = 700

dino_direita = "https://i.imgur.com/P6nIihH.jpg"
dino_esquerda = "https://i.imgur.com/P54FLEU.jpg"

class CenaDino():
    def __init__(self):
      self.cena_direita = Cena(img = dino_direita)
      self.cena_esquerda = Cena(img = dino_esquerda, direita=self.cena_direita)
      self.cena_direita.esquerda = self.cena_esquerda
      self.cena_direita.direita = self.cena_esquerda
      self.cena_esquerda.direita = self.cena_direita
      self.cena_esquerda.esquerda = self.cena_direita
    #cena2 = Cena2()
    #self.cena1.direita = cena2
    
    
    
def sala():
  cena_dino = CenaDino()
  cena_dino.vai()
  
  if __name__ == "__main__":
  	sala()