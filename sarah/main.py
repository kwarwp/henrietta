# henrietta.sarah.main.py
from _spy.vitollino.main import Cena

salapedras1 = "https://i.imgur.com/2kCYcjs.jpg"
salapedras2 = "https://i.imgur.com/AkcB954.jpg"
salapedras3 = "https://i.imgur.com/AXT4Zcl.jpg%20https://i.imgur.com/mr58OsA.jpg"

class Cenasalapedras():
    def __init__(self):
    self.cena1 = Cena(img = salapedras1)
    self.cena2 = Cena(img = salapedras2, direita=self.cena1)
    self.cena3 = Cena(img = salapedras3, direita=self.cena2,
    esquerda = self.cena1)
    self.cena1.esquerda = self.cena2
    self.cena2.esquerda = self.cena3
    
    
    