# henrietta.lisa.main.py
from _spy.vitollino.main import Cena, STYLE
from _spy.vitollino.main import INVENTARIO as inv

STYLE ['width'] = 700

R_OESTE = "https://i.imgur.com/XJXjA9r.jpg"
R_LESTE = "ttps://i.imgur.com/rHzbmtM.jpg"
R_NORTE = "ttps://i.imgur.com/IPa06hM.jpg"

class CenaRecepcao():
  def __init__(self):
    
    self.cena_norte = Cena(img = R_NORTE)
    self.cena_leste = Cena(img = R_LESTE, esquerda=self.cena_norte)
    self.cena_oeste = Cena(img = R_OESTE, direita=self.cena_norte)
   
   
   def vai_CenaRecepcao():
  cenaImporta = CenaRecepcao()
  cenaImporta.vai()
 
if __name__ == "__main__":
	vai_CenaRecepcao()