# henrietta.adda.main.py
from _spy.vitollino.main import Cena, STYLE

STYLE['width'] = 700

#colocar as imagens 
frutosDaTerra_n = "http://bit.ly/2FOvGTr"

class CenaFrutosDaTerra():
  def __init__(self):
	#from meredith.main import Cena2
    self.cena_n = Cena(img = frutosDaTerra_n)
    
    self.cena_n.vai()
    def vai(self, *):
  
