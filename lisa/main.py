# henrietta.lisa.main.py
from _spy.vitollino.main import Cena, STYLE

STYLE ['width'] = 699

R_OESTE = "https://i.imgur.com/XJXjA9r.jpg"
R_LESTE = "https://i.imgur.com/rHzbmtM.jpg"
R_NORTE = "https://i.imgur.com/IPa06hM.jpg"

class CenaRecepcao():
  def __init__(self):
    self.cena_norte = Cena(img = R_NORTE, direita=self.cena_leste)
    self.cena_leste = Cena(img = R_LESTE, esquerda=self.cena_norte)
    self.cena_oeste = Cena(img = R_OESTE, direita=self.cena_norte)
    
    self.cena_norte.direita = self.cena_leste
    self.cena_leste.esquerda = self.cena_norte
    self.cena_norte.esquerda = self.cena_oeste
    self.cena_oeste.direita = self.cena_norte
    
  
  def vai_Recepcao():
      cenaImporta = CenaRecepcao
      cenaImporta.vai()
 
if __name__ == "__main__":
	vai_CenaRecepcao()