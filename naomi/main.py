# henrietta.naomi.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE
from _spy.vitollino.main import INVENTARIO as inv
from soraya.main import Bloco
from alexa.main import responde
from browser import alert
from kathryn.main import Plotter, Texto as Entrada
STYLE["width"] = 600
STYLE["height"] = "600px"

TEMPLO = "http://3.bp.blogspot.com/-UsnGAupu3XM/VHvU2M5BHUI/AAAAAAAAdCE/UKbq_5dTM7k/s1600/IMG_6098.JPG"
CORREDOR = "http://i.muyinteresante.com.mx/dam/sociedad/historia/17/03/8/rabbit-hole-700-year-old-secret-knights-templar-cave-network-8-58c006f4a30df__880.jpg.imgo.jpg"
OCEANO = "https://freeclipartspot.com//storage/upload/ocean-clip-art/ocean-clip-art-51.jpg"
ALGA = "https://i.pinimg.com/originals/70/68/5f/70685fa634c3bb82a8eb5771a0a869ed.png"
CONCHA = "http://www.mat.uc.pt/~picado/conchas/imagens/p10.png"
AQUARIO = "https://www.tenstickers.pt/autocolantes-decorativos/img/preview/autocolante-decorativo-infantil-peixe-aquario-3634.png"
TRANSPARENTE = "http://1.bp.blogspot.com/-eK24sreQNsg/Uvy1AT5iVSI/AAAAAAAAAGo/TRHh_nkqhVY/s1600/fundo-blog.png"
FLORESTA = "https://st.depositphotos.com/1718692/2958/i/950/depositphotos_29580473-stock-photo-stones-and-tree-roots-in.jpg"
OCULOS = "https://www.dvosky.com/media/catalog/product/cache/1/image/1200x1200/9df78eab33525d08d6e5fb8d27136e95/d/v/dvsk1003-preto-prata.png"
historia = "eu friccionei a pedra e gerou fogo"
verbos_altos = ["ger", "atrit", "roç", "direcion", "friccion", "elev", "decid", "faz", "concl", "us", "foc",
                "remanej" ,"erg", "suspend", "ate", "esfreg", "trisc", "fez", "fiz", "esfreg", "atrit", "foquei"
                "incend", "aquec", "flamej", "cort"] 
verbos_altos ==  3
verbos_medios = ["bat", "gir", "colo", "manipul", "mov", "surg", "peg", "levant", "bat", "segur", "junt"
                 "arranq", "arranc"]
verbos_medios ==  2

verbos_fracos = ["rod", "bot", "sub", "pux", "form", "tent", "cli", "abaix", "mex", "encost", "rel"] 
verbos_fracos ==  1
verbos = [ (3,verbos_altos),(2,verbos_medios),(1,verbos_fracos)]
VERBOS = verbos_altos +verbos_medios + verbos_fracos
OBJETOS = """galho graveto óculos oculos lente foco vara pedra pedregulho furo tábua tabua
 faisca faísca fagulha fumaça labareda fogaréu fogareu fogueira outra outro fumacinha rio lago riacho
 pau paus pauzinhos palito palitinho palitinhos palitos
    cascalho sol luz brilho fogo palha folha cavaco""".split()
SUJEITOS = "eu nós nos gente".split()


    
class Estados:
    def __init__(self):
        inv.inicia()
        self.floresta = floresta = Cena(FLORESTA)
        self.fantasma = Cena()
        floresta.vai()
        self.titulo = 'floresta'
        self.galhos = gag = Elemento(img=TRANSPARENTE,tit="galhos", style=dict(
            left=28, top=130, width=60, height="60px"))
        gag.entra(floresta)
        gag.vai = self.fogo_galhos
        self.pedra = aqua = Elemento(img=TRANSPARENTE,tit="pedras", style=dict(
            left=500, top=300, width=60, height="60px")) 
        aqua.entra(floresta)
        aqua.vai = self.fogo_pedra
        self.oculos = ocu = Elemento(img=OCULOS, tit="OCULOS", style=dict(
            left=28, top=130, width=60, height="60px"))
        inv.bota(self.oculos)
        ocu.vai = self.fogo_oculos
        self.grafico = Elemento(img=TRANSPARENTE, tit="GRÁFICO", style=dict(
            left=600, top=200, width=300, height="200px"))
        self.grafico.entra(floresta)    
        inv.score(casa=FLORESTA, carta='' , _level=1,
                         move="FLORESTA", ponto=0, valor=0)
        
    def pontua(self, pontos):
        resposta, grafo = pontos
        #grafo = [t for data in grafo.split(chr(172)) for _, t in data.split(chr(181))]
        grafo_ = Plotter.unpack(grafo)
        t0 = int(grafo_[0][1])
        grafo = [(int(t)-t0) // 10 for _, t in grafo_]
        _grafo = [(x, b - a) for x, (b, a) in enumerate(zip(grafo[1:], grafo))]
        _grafp = [(x, b - a + 100) for x, ((_,b), (_,a)) in enumerate(zip(_grafo[1:], _grafo))]
        plt = Plotter(self.grafico.elt, self.titulo)
        x, y = zip(*_grafo)
        plt.plot(x, y)
        x, y = zip(*_grafp)
        plt.plot(x, y, "magenta")
        paradigma, parax = avaliar(resposta)
        sintagma, sintax = responde(resposta, SUJEITOS, VERBOS, OBJETOS)
        sintax, parax = Plotter.pack(sintax), Plotter.pack(parax)
        display_paradigma = "paradigma={}::{}".format(paradigma, parax)
        plt.display(display_paradigma)
        display_sintagma = "sintagma={}::{}".format(sintagma, sintax)
        plt.display(display_sintagma )
        datapack = Plotter.pack([[c, '{0:0>6}'.format((int(t)-t0)//1)] for c, t in grafo_])
        # inv.score(casa=resposta, carta=datapack , _level=2,
                         #move=self.titulo, ponto=display_paradigma, valor=display_sintagma)

        
        
    def entrada(self, tit, cena=None, vai=None):
        vai = vai if vai else self.pontua
        self._entra = Entrada(cena=cena or self.floresta, tit=tit, texto="",
             foi=lambda *_: vai(self._entra.sai()))
        self._entra.vai()
        
    def fogo_pedra(self, *_):
        # resposta=input("Voce fez fogo usando pedras! Como vc fez?")
        self.titulo = 'Imaginário: pedras'
        self.entrada(tit="Voce fez fogo usando pedras! Como vc fez?")
        self.pedra.entra(self.fantasma)
    def fogo_galhos(self, *_):
        self.titulo = 'Imaginário: galhos'
        # resposta=input("voce fez fogo usando galhos! como vc fez?")
        self.entrada(tit="voce fez fogo usando galhos! como vc fez?")
        
        
        self.galhos.entra(self.fantasma)
        #alert(avaliar(respostas))
    def fogo_oculos(self, *_):
        # respostas=input("voce fez fogo usando oculos! como vc fez?")
        self.titulo = 'Imaginário: óculos'
        self.entrada(tit="voce fez fogo usando oculos! como vc fez?")
        
        
        self.oculos.entra(self.fantasma)
        # alert(avaliar(respostas))

def avaliar(you):
    pontuacao = 0
    pontos = [(peso, prefixo) for peso,verbo in verbos for prefixo in verbo if prefixo in you]
    pontuacao = sum(peso for peso, _ in pontos)
    '''
    for peso,verbo in verbos:
        for prefixo in verbo:
            pontuacao += peso if prefixo in you else 0 
    '''
    return pontuacao, pontos
    

    
            
    


if __name__ == "__main__":
    Estados()