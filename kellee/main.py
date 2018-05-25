# henrietta.kellee.main.py
from _spy.vitollino.main import Cena, Elemento, Texto

NEWTON = "http://4.bp.blogspot.com/-5gZeG2PCX-0/ViRIc3iUP_I/AAAAAAAACn4/IWvXueCewjU/s1600/fg_3456011-1024x576.jpg"
GALILEU = "https://pbs.twimg.com/profile_images/666413287639269377/-Yw4RtjG_400x400.png"
MACA = "https://macmagazine.com.br/wp-content/uploads/2011/02/24-rainbows.png"
ILUMINATTI = "https://vignette.wikia.nocookie.net/clubpenguin/images/2/2d/Illuminati.png/revision/latest?cb=20150117022611"

def teorias():
    inicio = Cena(img=NEWTON)
    inicioe = Elemento(img=MACA, tit"Eis que a gravidade aparece", style = dict(left= 150,top=100, width=60, height=200,bottom=100))    
    lado1 = Cena(img=GALILEU, direita =inicio)
    lado1_e = Elemento(img=ILUMINATTI, tit'O universo nÃÂ£o gira em torno de vocÃÂª nÃÂ£o,bb', style = dict(left= 150, top=100, width=60, height=200, bottom=100))
    
    inicio_e.entra(inicio)
    lado1_e.entra(lado1)
    
    lado1.vai()
    
teorias()