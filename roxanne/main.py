from _spy.vitollino.main import Cena, STYLE

STYLE['width'] = 700

entra_n = "https://i.imgur.com/gc2frjm.jpg"
entra_nzoom = "https://i.imgur.com/ELvdLzp.jpg"
entra_nabre = "https://i.imgur.com/u6ou7mM.jpg"
entra_l = "https://i.imgur.com/F9Cem7k.jpg"
entra_o = "https://i.imgur.com/gO8JFgU.jpg"
entra_ozoom = "https://i.imgur.com/JBQY8wh.jpg"


class Entrada():
   def __init__ (self):
      self.cena_n = (img= entra_n)
      self.cena_o = Cena(img = entra_o, direita=self.cena_n, 
      esquerda = self.cena_nz)    
      self.cena_na = Cena(img = entra_nabre)
      self.cena_nz = Cena(img = entra_nzoom)
      self.cena_n = Cena(img = entra_n, direita =self.cena_l, meio = self)
      self.cena_l  =  Cena(img= entra_l,esquerda = self.cena_n)
      
      self.cena_n.esquerda = self.cena_o
      self.cena_o.esquerda = self.cena_s
      self.cena_s.esquerda = self.cena_l
        
        
        
        
        
def Game():
  cena1 = Entrada()
  cena1.vai()

if __name__ == "__main__":
	Game()