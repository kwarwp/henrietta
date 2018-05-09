# henrietta.meredith.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"] = 600
STYLE ["height"] = "600px"


ARVORE = "https://static.significados.com.br/foto/arvore.jpg"
MAE = 'https://media.istockphoto.com/vectors/cartoon-mother-holding-her-son-vector-id506469526'
EU = 'https://st2.depositphotos.com/1007566/12280/v/950/depositphotos_122808052-stock-illustration-girl-kid-cartoon.jpg'


def familia ():
    arvore = Cena(img = ARVORE)
    arvore.vai()
    mae = Elemento(img = MAE, tit = "Mother", style = dict(left=120, top="270px", width=80, height="100px"))
    eu = Elemento (img = EU, tit = "I", style = dict(left=40, top="450px", width=100, height="100px"))
    mae_text= Texto(arvore, "Mother")
    eu_text= Texto(arvore, "I")
    mae.vai = mae_text.vai
    eu.vai = eu_text.vai
    eu.entra (arvore)
    mae.entra(arvore)
    
familia ()
    


