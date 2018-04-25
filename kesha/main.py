# henrietta.kesha.main.py
# dana.lisa.main.py
from _spy.vitollino.main import Cena, Elemento, INVENTARIO as inv
from _spy.vitollino.main import STYLE
STYLE ["width"] = 900
#STYLE ["max-height"] = 600
floresta = "https://img.elo7.com.br/product/zoom/12F2B86/painel-de-festa-floresta-festa-personalizada.jpg"
coqueiro = "https://lh5.googleusercontent.com/-BBPWTiFTHEU/TXjoNCqwMZI/AAAAAAAAARE/MLZAmwW--yI/s1600/coco%252520anao%255B1%255D.jpg"
aguadecoco = "https://gartic.com.br/imgs/mural/th/the_skywalker/agua-de-coco.png"
orvalho = "https://st.depositphotos.com/1030956/4910/i/950/depositphotos_49103197-stock-photo-macro-tree-branch-with-raindrops.jpg"
seivadearvore = "http://cdn.ciclovivo.com.br/wp-content/uploads/2015/009/img/noticias/1238633982_9f95150143%20(1).jpg"
cacto = "http://clipart.coolclips.com/480/vectors/tf05089/CoolClips_natu0731.png"

class Agua():
     def __init__ (self):
      self.floresta= Cena(img=floresta)
      self.floresta0= Cena(img=floresta)
      self.floresta1= Cena(img=floresta, esquerda=self.floresta)
      self.floresta2= Cena(img=floresta, direita=self.floresta)
      self.floresta3= Cena(img=cacto, esquerda=self.floresta0)
      self.floresta4= Cena(img=seivadearvore)
      self.coqueiro= Elemento(img=coqueiro, style=dict (left=100, top= 300, height=200 ,width=200,bottom=100))
      self.aguadecoco= Elemento (img=aguadecoco, style=dict (left=90, top=100 , height=100, width=100, bottom=10))
      self.orvalho= Elemento (img=orvalho, style=dict (left=95, top= 100, height=100, width=100, bottom=15))
      #self.seivadearvore= Elemento (img=seivadearvore, style=dict (left=100, top= 100, height=100, width=100, bottom=15))
      self.cacto= Elemento (img=cacto, style=dict (left=85, top= 100, height=100, width=15, bottom=15))
      
      self.floresta.direita= self.floresta1
      self.coqueiro.entra(self.floresta1)
      #criar a funÃ§Ã£o de abrir elemento ao clicar em elemento
      self.floresta.esquerda= self.floresta2
      self.orvalho.entra(self.floresta2)
      self.floresta.meio= self.floresta0
      self.floresta0.direita= (self.floresta3)
      self.cacto.entra = (self.floresta3)
      self.floresta.esquerda= (self.floresta4)
      self.seivadearvore.entra (self.floresta4)
       #def chama(x):
         
      
       
      
      self.floresta.vai ()
if __name__ == "__main__":
     Agua()

