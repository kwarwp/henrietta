# henrietta.stacy.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, INVENTARIO, STYLE
from browser import alert
from soraya.main import Bloco
STYLE["width"] = 800
STYLE["height"] = "600px"

TEMPLO = "http://3.bp.blogspot.com/-UsnGAupu3XM/VHvU2M5BHUI/AAAAAAAAdCE/UKbq_5dTM7k/s1600/IMG_6098.JPG"
CORREDOR = "http://i.muyinteresante.com.mx/dam/sociedad/historia/17/03/8/rabbit-hole-700-year-old-secret-knights-templar-cave-network-8-58c006f4a30df__880.jpg.imgo.jpg"
OCEANO = "https://i.imgur.com/NRi5i6d.jpg"
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
SALATEMPLO1 = "https://i.imgur.com/kmLevtL.jpg"
CINZA = "https://cdn.simplo7.net/static/7106/sku/tricoline-lisa-100-algodao-tricoline-lisa-100-algodao-cinza-1921-50cm-x-1-50mt--p-1502305300683.jpg"
WOOD = "https://i.imgur.com/6DB1eCQ.jpg"
palavras_obrig = ["peix", "aqu", "conch", "ocea", "alg", "flore", "coruj", "passar", "pat", "mac", "flores", "musi",
                  "head", "tamb", "vio", "choc", "muse", "coro", "vas", "relo", "lun", "coz", "cozinhe", "cad", "pan",
                  "fog", "esport", "bol", "raq", "luv"]


class Corredor:
    _corredor = None
    _templo = None
    def __init__(self):
        self.singleton_corredor()

    @staticmethod
    def singleton_corredor():
        self.cena = Cena(img=CORREDOR)
        self.cena.direita = Corredor._templo
        self.cena.esquerda = Corredor._templo
        Corredor._corredor = self
        Corredor.singleton_corredor = lambda *_: None

    @staticmethod
    def singleton_templo():
        Corredor._templo = Cena(img=TEMPLO)
        Corredor._templo.meio = Corredor._corredor
        Corredor.singleton_templo = lambda *_: None

    @property
    def vai(self):
        return self.cena.vai

    def elemento(self, **kwargs):
        elemento = Elemento(**kwargs)
        elemento.entra(self.cena)
        elemento.vai = kwargs["vai"]

class Templo(Corredor):
    def __init__(self):
        super().__init__()
        #Corredor()
        Corredor.singleton_templo()
        _salas = {"salatemplo{}".format(n+1): SalaTemplo(tema, x, y) for n, (tema, x, y) in enumerate([
            [OCEANO, 2, 2],
            [FLORESTA, 3, 3],
            [MUSICA, 4, 4],
            [MUSEU, 5, 5],
            [COZINHA, 5, 5],
            [ESPORTE, 6, 6]
        ])}
        _salas.update(corredor=Corredor._corredor)
        # [print(s, v) for s, v in _salas.items()]
        # return
        _design =[
            ('corredor', dict(vai=_salas['corredor'].vai, img=COZINHA, tit="cozinha",
                              style=dict(left=680, top=160, width=60, height=200)),),
            ('corredor', dict(vai=_salas['corredor'].vai, img=ESPORTE, tit="esporte",
                              style=dict(left=760, top=160, width=60, height=200)),),
            ('corredor', dict(vai=_salas['corredor'].vai, img=FLORESTA, tit="floresta",
                              style=dict(left=180, top=160, width=60, height=200)),),
            ('corredor', dict(vai=_salas['corredor'].vai, img=MUSEU, tit="museu",
                              style=dict(left=600, top=160, width=60, height=200)),),
            ('corredor', dict(vai=_salas['corredor'].vai, img=MUSICA, tit="musica",
                              style=dict(left=260, top=160, width=60, height=200)),),
            ('corredor', dict(vai=_salas['corredor'].vai, img=OCEANO, tit="oceano",
                              style=dict(left=100, top=160, width=60, height=200)),),
            ('salatemplo1', dict(vai=_salas['salatemplo1'].vai, img=ALGA, tit="alga",
                                 style=dict(left=200, top=160, width=60, height=200)),),
            ('salatemplo1', dict(vai=_salas['salatemplo1'].vai, img=AQUARIO, tit="alga",
                                 style=dict(left=100, top=160, width=60, height=200)),),
            ('salatemplo1', dict(vai=_salas['salatemplo1'].vai, img=CONCHA, tit="concha",
                                 style=dict(left=300, top=160, width=60, height=200)),),
            ('salatemplo2', dict(vai=_salas['salatemplo2'].vai, img=CORUJA, tit="coruja",
                                 style=dict(left=200, top=160, width=60, height=200)),),
            ('salatemplo2', dict(vai=_salas['salatemplo2'].vai, img=FLORES, tit="pato",
                                 style=dict(left=300, top=160, width=60, height=200)),),
            ('salatemplo2', dict(vai=_salas['salatemplo2'].vai, img=MACACO, tit="macaco",
                                 style=dict(left=100, top=160, width=60, height=200)),),
            ('salatemplo2', dict(vai=_salas['salatemplo2'].vai, img=PASSAROS, tit="passaros",
                                 style=dict(left=300, top=160, width=60, height=200)),),
            ('salatemplo2', dict(vai=_salas['salatemplo2'].vai, img=PATOS, tit="pato",
                                 style=dict(left=300, top=160, width=60, height=200)),),
            ('salatemplo3', dict(vai=_salas['salatemplo3'].vai, img=CHOCALHO, tit="chocalho",
                                 style=dict(left=100, top=160, width=60, height=200)),),
            ('salatemplo3', dict(vai=_salas['salatemplo3'].vai, img=HEADPHONES, tit="Headphones",
                                 style=dict(left=50, top=160, width=60, height=200)),),
            ('salatemplo3', dict(vai=_salas['salatemplo3'].vai, img=TAMBOR, tit="tambor",
                                 style=dict(left=300, top=130, width=30, height=200)),),
            ('salatemplo3', dict(vai=_salas['salatemplo3'].vai, img=VIOLAO, tit="violao",
                                 style=dict(left=200, top=160, width=60, height=200)),),
            ('salatemplo4', dict(vai=_salas['salatemplo4'].vai, img=COROA, tit="coroa",
                                 style=dict(left=50, top=160, width=60, height=200)),),
            ('salatemplo4', dict(vai=_salas['salatemplo4'].vai, img=LUNETA, tit="luneta",
                                 style=dict(left=300, top=130, width=60, height=200)),),
            ('salatemplo4', dict(vai=_salas['salatemplo4'].vai, img=RELOGIO, tit="relogio",
                                 style=dict(left=100, top=160, width=60, height=200)),),
            ('salatemplo4', dict(vai=_salas['salatemplo4'].vai, img=VASO, tit="vaso",
                                 style=dict(left=200, top=160, width=60, height=200)),),
            ('salatemplo5', dict(vai=_salas['salatemplo5'].vai, img=CADEIRA, tit="cadeira",
                                 style=dict(left=200, top=160, width=60, height=200)),),
            ('salatemplo5', dict(vai=_salas['salatemplo5'].vai, img=COZINHEIRA, tit="cozinheira",
                                 style=dict(left=50, top=160, width=60, height=200)),),
            ('salatemplo5', dict(vai=_salas['salatemplo5'].vai, img=FOGAO, tit="fogao",
                                 style=dict(left=300, top=130, width=60, height=200)),),
            ('salatemplo5', dict(vai=_salas['salatemplo5'].vai, img=PANELA, tit="panela",
                                 style=dict(left=100, top=160, width=60, height=200)),),
            ('salatemplo6', dict(vai=_salas['salatemplo6'].vai, img=BOLA, tit="bola",
                                 style=dict(left=50, top=160, width=60, height=200)),),
            ('salatemplo6', dict(vai=_salas['salatemplo6'].vai, img=LUVAS, tit="luvas",
                                 style=dict(left=200, top=160, width=60, height=200)),),
            ('salatemplo6', dict(vai=_salas['salatemplo6'].vai, img=RAQUETE, tit="raquete",
                                 style=dict(left=300, top=130, width=60, height=200)),),
        ]
        for sala, design in _design:
            _salas[sala].elemento(**design)
        Corredor._templo.vai()
        #_salas['salatemplo6'].vai()

class SalaTemplo(Corredor):
    def __init__(self, tema, x=2, y=2):
        super().__init__()
        self.tabuleiro = Cena(img=WOOD)
        self.cena = Cena(img=SALATEMPLO1)
        self.tabuleiro.esquerda = self.cena
        self.cena.direita = Corredor._templo
        quebra_cabeca = Bloco(tema, x, y, vai=self.cena.vai)
        quebra_cabeca.entra(self.tabuleiro)
        tsala = Texto(self.tabuleiro, "Monte o quebra cabeca e entre na sala.")

def ilha(prog):
    print(123456789)
    prog = prog.split('\n')
    pg_el = [ln+ent for ln, ent in zip(prog, prog[1:]) if "= Elemento(img=" in ln and "# " not in ln and ".entra(" in ent]
    pge = ["vai=_salas['{}'].vai, {})".format(l.split(".entra(self.")[1].split(")")[0],l.split("Elemento(")[1].split("))")[0]) for l in pg_el]
    pge = ["dict(vai=_salas['{}'].vai, {}),)".format(l.split(".entra(self.")[1].split(")")[0],l.split("Elemento(")[1].split("))")[0]) for l in pg_el]
    pgc = [(l.split("vai, img=")[1].split(", tit=")[0],l) for l in pge]

    pgd = ["        ({}, {}),".format(s if 'corredor' in l else l.split("vai=_salas[")[1].split("].vai,")[0],l) for s, l in pgc]

    pgs = sorted(pgd)

    for l in pgs:
        print(l)
    #[print(l) for l in pge]


if __name__ == '__main__':
    Templo()
