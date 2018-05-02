# henrietta.kellee.main.pyfrom _spy.vittolino.main import Cena, Elemento, Texto
from _spy.vitollino.main import Cena, Elemento, Texto
NEWTON = "https://netnature.files.wordpress.com/2017/11/sem-tc3adtulo37.png?w=524&h=324"
MACA = "https://amdpc.files.wordpress.com/2008/03/apple_computer_logo_svg.png"
GALILEU = "https://pbs.twimg.com/profile_images/666413287639269377/-Yw4RtjG_400x400.png"
ORBITA = "https://upload.wikimedia.org/wikipedia/commons/4/48/Sobo_1909_768.png"




def teorias():

    inicio = Cena(img= NEWTON)
    inicio_mud = Elemento(img = MACA, tit="Eis que a gravidade atua", style = dict(right= 100,
                                                                                   top=200,
                                                                                   width=110,bottom=20))
    lado1 = Cena(img = GALILEU, direita = inicio)
    lado1_mud = Elemento(img = ORBITA, tit = "O mundo não gira em torno de você não,@", style = dict(left = 100,
                                                                                                     top = 200,
                                                                                                     width = 125, bottom = 20))
    
    inicio_mud.entra(inicio)
    inicio.esquerda = lado1
    lado1_mud.entra(lado1)
    lado1.vai()
    
teorias()
    
                         
    
     
  



