# henrietta.adda.main.py
from _spy.vitollino.main import Cena, STYLE

STYLE['width'] = 699

TutorialInterativo = "https://i.imgur.com/tfatd8y.png"
Cena_direita = "https://i.imgur.com/2YX3bLb.png"
Cena_esquerda = "https://i.imgur.com/NC0Sj4z.png"
comousarelemento = "https://i.imgur.com/amn4taQ.png"
class CenaTutorialInterativo():
  def __init__(self):
    
    self.cena_t = Cena(img = TutorialInterativo)
    
    self.cena_d = Cena(Cena_direita, direita=self.cena_t)

    self.cena_e  = Cena(Cena_esquerda, esquerda=self.cena_t)

    
    #self.cena_t = Cena(img = TutorialInterativo)
    
    self.cena_t.direita = self.cena_d
    self.cena_t.esquerda = self.cena_e
    
    self.cena_t.meio = Cena(vai=self.vai_importar)
    self.cena_t.vai()
    
    
  def vai(self, *_):
    self.cena_t.vai()
    
    
    
  def vai_importar(self, *_):
    from kristen.main import go_cretaceo
    go_cretaceo()
    
def vai_CenaTutorialInterativo():
  cenaImporta = CenaTutorialInterativo()
  cenaImporta.vai()
 
if __name__ == "__main__":
	vai_CenaTutorialInterativo()
    
     
  from _spy.vitollino.main import Cena, Texto, Elemento, STYLE
from _spy.vitollino.main import INVENTARIO as inv

FLORESTA = "https://st.depositphotos.com/1718692/2958/i/950/depositphotos_29580473-stock-photo-stones-and-tree-roots-in.jpg"
TRANSPARENTE = "http://1.bp.blogspot.com/-eK24sreQNsg/Uvy1AT5iVSI/AAAAAAAAAGo/TRHh_nkqhVY/s1600/fundo-blog.png"
class Estados:
    def __init__(self):
        floresta = Cena(FLORESTA)
        self.fantasma = Cena()
        floresta.vai()
        self.galhos = gag = Elemento(img=TRANSPARENTE,tit="galhos", style=dict(
            left=28, top=130, width=60, height="60px"))
        gag.entra(floresta)
        gag.vai 
        
        
if __name__ == "__main__":
    Estados()

