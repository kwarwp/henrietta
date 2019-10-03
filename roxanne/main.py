from _spy.vitollino.main import Cena, STYLE

STYLE['width'] = 700

entra_n = "https://i.imgur.com/gc2frjm.jpg"
entra_nzoom = "https://i.imgur.com/ELvdLzp.jpg"
entra_nabre = "https://i.imgur.com/u6ou7mM.jpg"
entra_l = "https://i.imgur.com/F9Cem7k.jpg"
entra_o = "https://i.imgur.com/gO8JFgU.jpg"
entra_oz = "https://i.imgur.com/JBQY8wh.jpg"


class Entrada():
    def __init__ (self):
    
        self.cena_n  = Cena(img = entra_n) 
        self.cena_na = Cena(img = entra_nabre)
        self.cena_nz = Cena(img = entra_nzoom)
        
        self.cena_l  = Cena(img = entra_l, esquerda = self.cena_n)

        self. cena_o = Cena(img = entra_o, direita = self.cena_n)
        self.cena_oz = Cena(img = entra_oz, direita = self.cena_o)

        self.cena_n.esquerda = self.cena_o
        self.cena_o.esquerda= self.cena_oz
        self.cena_oz.direita = self.cena_n
        self.cena_n.meio = self.cena_nz
        self.cena_nz.meio = self.cena_na
        self.cena_nz.esquerda = Cena(vai = self.vai_sul)

        self.cena_n.vai()
        
    def vai(self, *_):
    self.cena_o.vai()
    
    def vai_sul(self, *_):
    from Kristen.main import go_cretaceo
    go_cretaceo()

def entrada():
    museu = Entrada()
    museu.vai()

if __name__ == "__main__":
    entrada()