# henrietta.grace.main.py
from _spy.vitollino.main import Cena, STYLE

STYLE['WIDTH'] = 700

mares_entrada = "https://i.imgur.com/2UJALzV.jpg"
mares_frente = "https://i.imgur.com/32jplNw.jpg"
mares_direita = "https://i.imgur.com/Q3FZ5qz.jpg"
mares_esquerda = "https://i.imgur.com/dCUicdo.jpg"
mares_sul = "https://i.imgur.com/5Oqrcfx.jpg"
mares_passado = "https://i.imgur.com/zK2PoZZ.jpg"
passado_concha = "https://i.imgur.com/5WWKm98.jpg"

class Mares_do_passado():
    def __init__ (self):
      self.cena_entrada = Cena(img = mares_entrada)
      self.cena_n = Cena(img = mares_frente)
      self.cena_l = Cena(img = mares_direita)
      self.cena_past = Cena(img = mares_passado)
      self.cena_concha = Cena(img = passado_concha)
      
      self.cena_s = Cena(img = mares_sul)
      self.cena_o = Cena(img = mares_esquerda)