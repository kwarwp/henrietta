# henrietta.rachel.main.py
from _spy.vitollino.main import Cena, Texto, Elemento
from _spy.vitollino.main import INVENTARIO as inv
from soraya.main import Bloco

TEMPLO = "http://3.bp.blogspot.com/-UsnGAupu3XM/VHvU2M5BHUI/AAAAAAAAdCE/UKbq_5dTM7k/s1600/IMG_6098.JPG"
CORREDOR = "http://i.muyinteresante.com.mx/dam/sociedad/historia/17/03/8/rabbit-hole-700-year-old-secret-knights-templar-cave-network-8-58c006f4a30df__880.jpg.imgo.jpg"
OCEANO = "https://freeclipartspot.com//storage/upload/ocean-clip-art/ocean-clip-art-51.jpg"
ALGA = "https://i.pinimg.com/originals/70/68/5f/70685fa634c3bb82a8eb5771a0a869ed.png"
CONCHA = "http://www.mat.uc.pt/~picado/conchas/imagens/p10.png"
AQUARIO = "https://www.tenstickers.pt/autocolantes-decorativos/img/preview/autocolante-decorativo-infantil-peixe-aquario-3634.png"
FLORESTA = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSW0BY3YH52d4HOogtzl4XDXyawkVJeAi-5pNTHvhQZBrB-OF2i"
CORUJA = "http://www.eternit.com.br/images/files_up/original/29042015150454corujacomasasfechadasnopuleiro_emalta.jpg"
PATOS = "http://4.bp.blogspot.com/-aF5frApwsMs/UnCGJk14WEI/AAAAAAAAahs/FKS72dTtYzk/s1600/Animais-em-png-queroimagem-Cei%C3%A7a-Crispim++(12).png"
MACACO = "https://i.pinimg.com/originals/2e/75/f6/2e75f60ab1931937f8fadcca38630382.png"
FLORES = "https://banner.kisspng.com/20171127/1a3/yellow-rose-bush-png-clipart-picture-5a1bab2ea27e19.9392345015117627346656.jpg"
PASSAROS = "https://png.clipart.me/previews/272/cute-twitter-bird-vector-image-26050.png"
MUSICA = "https://images.vexels.com/media/users/3/148533/list/ab32e2a639adb5969b49b6420daf0514-boys-band-cartoon-illustration.jpg"
HEADPHONES = "https://images.vexels.com/media/users/3/144117/isolated/preview/b37cdf9a9b5ebc1554ffe1a7825939fc-fones-de-ouvido-de-msica-by-vexels.png"
VIOLAO = "http://cdn5.colorir.com/desenhos/color/201101/024b7852c59f132874fea13c36d4887f_163.png"
CHOCALHO = "https://i.pinimg.com/originals/92/fc/c2/92fcc2e8c29c17242612acef1e457bea.png"
TAMBOR = "https://images.emojiterra.com/emojione/v2/512px/1f941.png"
MUSEU = "https://cdna.artstation.com/p/assets/images/images/004/585/984/large/kamila-redkiewicz-museum.jpg?1484770586"
COROA = "https://medologia.com/assets/images/huol9FtnOB5KjNVjjM04keqhmLYKwIeyd3uEUluBXoPMxBp9J0Wex3CFqBrZt0SL4NPSV9qrNIblOg7pOwjUI6YDqr0SqT4M4Y2n1eU0KWz9saMKCGDYYf8I.png"
VASO = "http://www.fundaj.gov.br/images/stories/museu/museu3.png"
RELOGIO = "http://presidenteprudente.sp.gov.br/museu/images/2028927.png"
LUNETA = "http://www.pngpix.com/wp-content/uploads/2016/07/PNGPIX-COM-Spyglass-Telescope-PNG-Transparent-Image.png"
COZINHA = "https://image.freepik.com/vettori-gratuito/interno-cucina-moderna-piatto_6280-115.jpg "
COZINHEIRA = "http://ead.ceiprojac.com.br/Assets/Categorias/M_60371d747e33a01.png"
CADEIRA = "http://www.reformatapecaria.com.br/public/img/default/servicos-de-tapecaria/home/reforma-cadeiras-de-cozinha.png"
PANELA = "https://tramontina.com.br/public/panelas-inox/solar/img/produto.png?v=7"
FOGAO = "http://clipart.coolclips.com/480/vectors/tf05085/CoolClips_hous1104.png"
ESPORTE = "https://img3.stockfresh.com/files/d/ddraw/m/72/2405156_stock-photo-sport-characters-with-background.jpg"
BOLA = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Soccer_ball.svg/800px-Soccer_ball.svg.png"
RAQUETE = "http://padelcristalia.com/public/uploads/padelcristalia/logopala.png"
LUVAS = "https://static.vecteezy.com/system/resources/previews/000/143/644/non_2x/boxing-gloves-vector.png"
SALATEMPLO = "https://i.imgur.com/kmLevtL.jpg"
CINZA = "https://cdn.simplo7.net/static/7106/sku/tricoline-lisa-100-algodao-tricoline-lisa-100-algodao-cinza-1921-50cm-x-1-50mt--p-1502305300683.jpg"
OCE0 = "https://imgur.com/YA5Gaa3"
OCE1 = "https://imgur.com/a4RpoKz"
OCE2 = "https://imgur.com/jvJig5M"
OCE3 = "https://imgur.com/5dtIs9t"
OCE4 = "https://imgur.com/quI5Pi0"
OCE5 = "https://imgur.com/awqQCEh"
OCE6 = "https://imgur.com/SiU4uge"
OCE7 = "https://imgur.com/AHpuMyT"
OCE8 = "https://imgur.com/HUFShPV"
OCE9 = "https://imgur.com/hylc9so"
OCE10 = "https://imgur.com/CqWVaX4"
OCE11 = "https://imgur.com/uETLCuk"
wood = "https://i.imgur.com/6DB1eCQ.jpg"


class Cenatemplo():
     def __init__(self):
        self.templo = Cena(img=TEMPLO)
        self.corredor = Cena(img=CORREDOR)
        self.templo.meio = self.corredor
        self.cinza1 = Cena(img=wood)
        self.salatemplo1 = Cena(img=SALATEMPLO)
        self.cinza1.esquerda = self.salatemplo1
        self.salatemplo2 = Cena(img=SALATEMPLO)
        self.salatemplo1.direita = self.corredor
        #self.quebra_cabeca_oceano = Cena(img=OCE0,img=OCE1,img=OCE2,img=OCE3,img=OCE4,img=OCE5,img=OCE6,img=OCE7,img=OCE8,img=OCE9,img=OCE10,img=OCE11)
        
        oceano = Elemento(img=OCEANO,tit="oceano",style=dict(left=100, top=160, width=60, height=200))
        oceano.entra(self.corredor)
        oceano.vai = self.cinza1.vai
        #oceano.vai
        
        #quebra_cabeca_oceano = Elemento(img=,tit="quebra_cabeÃÂÃÂ§a_oceano",style=dict(left=100, top=160, width=60, height=200))
        quebra_cabeca_oceano = Bloco(OCEANO, 4, 4, vai=self.salatemplo1.vai)
        quebra_cabeca_oceano.entra(self.cinza1)
        Toceano = Texto(self.cinza1,"Monte o quebra cabeca e entre na sala.")
        #quebra_cabeca_oceano.vai = Toceano.vai
            
        alga = Elemento(img=ALGA,tit="alga",style=dict(left=200, top=160, width=60, height=200))
        alga.entra(self.salatemplo1)
        
        concha = Elemento(img=CONCHA,tit="concha",style=dict(left=300, top=160, width=60, height=200))
        concha.entra(self.salatemplo1)
            
        aquario = Elemento(img=AQUARIO,tit="alga",style=dict(left=100, top=160, width=60, height=200))
        aquario.entra(self.salatemplo1)
        texto = "Conte uma historia que utilize a imagem do quebra cabeca"
        texto += " com as imagens da sala e ganhe um premio"
        

        Hoceano = Texto(self.salatemplo1,'',texto)
        Hoceano.vai()

        #floresta = 
        self.templo.vai()
    
        floresta = Elemento(img=FLORESTA, tit="floresta", style=dict(left=180, top=160, width=60, height=200))
        floresta.entra(self.corredor)
        floresta.vai = self.cinza1.vai
        #oceano.vai
        
        #quebra_cabeca_oceano = Elemento(img=,tit="quebra_cabeÃÂÃÂ§a_oceano",style=dict(left=100, top=160, width=60, height=200))
        quebra_cabeca_floresta = Bloco(FLORESTA, 4, 4, vai=self.salatemplo2.vai)
        quebra_cabeca_oceano.entra(self.cinza1)
        Tfloresta = Texto(self.cinza1,"Monte o quebra cabeca e entre na sala.")
        #quebra_cabeca_oceano.vai = Toceano.vai
            
        coruja = Elemento(img=CORUJA,tit="coruja",style=dict(left=200, top=160, width=60, height=200))
        coruja.entra(self.salatemplo2)
        
        pato = Elemento(img=PATOS,tit="pato",style=dict(left=300, top=160, width=60, height=200))
        pato.entra(self.salatemplo2)
        
        flores = Elemento(img=FLORES,tit="pato",style=dict(left=300, top=160, width=60, height=200))
        flores.entra(self.salatemplo2)
        
        passaros = Elemento(img=PASSAROS,tit="passaros",style=dict(left=300, top=160, width=60, height=200))
        passaros.entra(self.salatemplo2)
            
        macaco = Elemento(img=MACACO,tit="alga",style=dict(left=100, top=160, width=60, height=200))
        macaco.entra(self.salatemplo2)
        texto = "Conte uma historia que utilize a imagem do quebra cabeca"
        texto += " com as imagens da sala e ganhe um premio"
        

        Hoceano = Texto(self.salatemplo1,'',texto)
        Hoceano.vai()

        #floresta = 
        self.templo.vai()
        
if __name__ == "__main__":
    teste = Cenatemplo()
    