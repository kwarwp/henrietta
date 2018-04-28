# henrietta.danae.main.py
# dana.lisa.main.py
from _spy.vitollino.main import Cena, Elemento, INVENTARIO as inv
from _spy.vitollino.main import STYLE
STYLE ["width"] = 900 
STYLE ["min-hight"] = 600
#STYLE ["max-height"] = 600
floresta = "https://img.elo7.com.br/product/zoom/12F2B86/painel-de-festa-floresta-festa-personalizada.jpg"
coqueiro = "https://lh5.googleusercontent.com/-BBPWTiFTHEU/TXjoNCqwMZI/AAAAAAAAARE/MLZAmwW--yI/s1600/coco%252520anao%255B1%255D.jpg"
#aguadecoco = "https://gartic.com.br/imgs/mural/th/the_skywalker/agua-de-coco.png"
orvalho = "https://st.depositphotos.com/1030956/4910/i/950/depositphotos_49103197-stock-photo-macro-tree-branch-with-raindrops.jpg"
seiva = "http://cdn.ciclovivo.com.br/wp-content/uploads/2015/009/img/noticias/1238633982_9f95150143%20(1).jpg"
cacto = "http://clipart.coolclips.com/480/vectors/tf05089/CoolClips_natu0731.png"

class Agua():
     def __init__ (self):
      
      self.floresta= Cena(img=floresta)
      self.florestaOrvalho= Cena(img=floresta)
      self.florestaCoqueiro= Cena(img=floresta)
      self.florestaSeiva= Cena(img=floresta)
      self.florestaCacto= Cena(img=floresta)

      self.floresta.direita = self.florestaCoqueiro
      self.florestaCoqueiro.esquerda = self.floresta
      
      self.floresta.esquerda = self.florestaOrvalho
      self.florestaOrvalho.direita = self.floresta
      
      self.florestaCoqueiro.direita = self.florestaCacto
      self.florestaCacto.esquerda = self.florestaCoqueiro
      
      self.florestaOrvalho.esquerda = self.florestaSeiva
      self.florestaSeiva.direita = self.florestaOrvalho      
      
      self.florestaSeiva.esquerda = self.florestaCacto
      self.florestaCacto.direita = self.florestaSeiva
      
      self.minicoqueiro= Elemento(img=coqueiro, style=dict (left=100, top= 300, height=200 ,width=200,bottom=100))
      #self.aguadecoco= Elemento (img=aguadecoco, style=dict (left=90, top=100 , height=100, width=100, bottom=10))
      self.miniorvalho= Elemento (img=orvalho, style=dict (left=95, top= 100, height=100, width=100, bottom=15))
      self.miniseiva= Elemento (img=seiva, style=dict (left=100, top= 100, height=100, width=100, bottom=15))
      self.minicacto= Elemento (img=cacto, style=dict (left=95, top= 100, height=100, width=100, bottom=15))
      
      self.minicoqueiro.entra (self.florestaCoqueiro)
      self.minicacto.entra (self.florestaCacto)
      self.miniseiva.entra (self.florestaSeiva)
      self.miniorvalho.entra (self.florestaOrvalho)
      
      #criar a funÃÂ§ÃÂ£o de abrir elemento ao clicar em elemento
      self.cenaCoqueiro = Cena (img=coqueiro)
      self.minicoqueiro.vai = self.cenaCoqueiro.vai
      self.cenaCoqueiro.esquerda = self.florestaCoqueiro
      self.cenaCoqueiro.direita = self.florestaCoqueiro
            
      self.cenaCacto = Cena (img= cacto)
      self.minicacto.vai = self.cenaCacto.vai
      self.cenaCacto.esquerda = self.florestaCacto
      self.cenaCacto.direita = self.florestaCacto
                      
      self.cenaOrvalho = Cena (img= orvalho)
      self.miniorvalho.vai = self.cenaOrvalho.vai
      self.cenaOrvalho.esquerda = self.florestaOrvalho
      self.cenaOrvalho.direita = self.florestaOrvalho
                      
      self.cenaSeiva = Cena (img= seiva)
      self.miniseiva.vai = self.cenaSeiva.vai
      self.cenaSeiva.esquerda = self.florestaSeiva
      self.cenaSeiva.direita = self.florestaSeiva
     
      
     
      self.floresta.vai ()
if __name__ == "__main__":
     Agua()