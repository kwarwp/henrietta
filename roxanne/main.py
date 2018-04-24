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
      
      self.cena_na = Cena(img = entra_nabre)
      self.cena_nz = Cena(entra_nzoom, meio = self.cena_na)
      self.cena_n = Cena(entra_n, esquerda = self.cena_nz) 
      
      self.cena_l = Cena(entra_l, esquerda = self.cena_n)
      
      self.cena_oz = Cena(entra_ozoom, direita = self.cena_n)
      self. cena_o = Cena(entra_o, esquerda = self.cena_oz, 
      direita = self.cena_n)
     
      self.cena_n.esquerda = self.cena_o
      self.cena_o.direita = self.cena_n
      self.cena_n.meio = self.cena_nz
      self.cena_nz.meio = self.cena_na
      self.cenanz.direita = Cena(vai =self.vai_cret)
      
      self.cena_n.vai()
      
   def vai(self, *_):
    self.cena_n.vai()
    
   def vai_cret(self, *_ ):
    #pode receber tantos argumentos além desse
    from Kristen.main import go_cretaceo
    go_cretaceo()

                       
def Go_entrada():
  Entrada = Entrada()
  Entrada.vai()

if __name__ == "__main__":
	Go_entrada()