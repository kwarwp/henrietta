# henrietta.meredith.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["Width"] = 10000


ARVORE = "https://static.significados.com.br/foto/arvore.jpg"
MAE = 'https://media.istockphoto.com/vectors/cartoon-mother-holding-her-son-vector-id506469526'

def familia ():
    arvore = Cena(img = ARVORE)
    arvore.vai()
    mae = Elemento(img = MAE, tit = "Mother", style = dict(left=50, top=200, width=50, high=50))
    mae_text= Texto(arvore, "Mother")
    mae.vai = mae_text.vai
    mae.entra(arvore)
    
familia ()
    


