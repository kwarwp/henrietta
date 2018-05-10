# henrietta.soraya.main.py
from _spy.vitollino.main import Cena, Elemento,STYLE, INVENTARIO
from browser import document, alert, html
STYLE["width"]=900
oce = "https://i.imgur.com/oDqeaBp.jpg"
wod = "https://i.imgur.com/6DB1eCQ.jpg"
sai = "https://i.imgur.com/oJphBx6.jpg"


class Folha:
    def __init__(self, bloco, left=0, top=0, ileft=0, itop=0,
                 size=dict(width=100, height=100)):
        self.suporte = None
        w, h = size.values()
        self.fid = fid = "folha_{}_{}".format(ileft, itop)
        self.casa = "casa_{}_{}".format(left, top)
        ileft, itop = "%dpx" % (-ileft*w), "%dpx" % (-itop*h)
        style = {'position': 'absolute', 'overflow': 'hidden',
                'background-image': 'url({})'.format(bloco.img),
                'background-position': '{} {}'.format(ileft, itop),
                'background-size': '{}px {}px'.format(*bloco.size),
        }
        style.update({k:'{}px'.format(v) for k, v in size.items() })
        style.update(left="%dpx" % (left*(w+10)), top="%dpx" % (top*(h+10)))
        self.folha = html.DIV(Id=fid, style=style, draggable=True)        
        bloco.folha <= self.folha
        self.folha.ondragstart = self.drag_start
        self.folha.onmouseover = self.mouse_over
        bloco.folhas[fid]=self
        #INVENTARIO.score(casa=self.casa, carta=self.fid, move="INIT", ponto=0, valor=0)

    def mouse_over(self, ev):
        ev.target.style.cursor = "pointer"
        return False

    def img_drag_start(self, ev):
        ev.preventDefault()
        ev.stopPropagation()
        INVENTARIO.score(casa=self.casa, carta=self.fid, move="START", ponto=0, valor=0)
        return False

    def drag_start(self, ev):
        ev.stopPropagation()
        ev.data['text'] = ev.target.id
        ev.data.effectAllowed = 'move'
        return False

    def troca(self, suporte):
        self.folha.style.left = 0
        self.folha.style.top = 0
        suporte.recebe(self, self.suporte)
        self.suporte = suporte
        self.folha.style.cursor = "auto"

class Suporte:
    def __init__(self, bloco, certa, left=0, top=0,
                 size=dict(width="25%", height="25%")):
        self.ladrilho = None
        style = {'position': "absolute", 'overflow': 'hidden',
                 'border':'1px solid MidnightBlue'}
        w, h = float(size['width'][:-1]), float(size['height'][:-1])
        style.update(size)
        style.update(left="%d%%" % (left*w), top="%d%%" % (top*h))
        self.certa = (left, top)
        self.folha = html.DIV(Id=certa.format(left, top), style=style)
        bloco.suporte <= self.folha
        self.folha.ondragover = self.drag_over
        self.folha.ondrop = self.drop
        self.bloco = bloco

    def recebe(self, folha, suporte):
        if folha:
            self.folha <= folha.folha
            self.folha.style.border=0
        else:
            self.folha.style.border='1px solid MidnightBlue'

        suporte.recebe(self.ladrilho, None) if suporte else None
        self.ladrilho = folha

    def drag_over(self, ev):
        ev.data.dropEffect = 'move'
        ev.preventDefault()
        return False

    def drop(self, ev):
        ev.preventDefault()
        ev.stopPropagation()
        src_id = ev.data['text']
        self.bloco.folhas[src_id].troca(self) 
        lugar = [int(coord) for coord in src_id.split("_")[1:]]
        certa = sum(abs(100//(2*(a-b) or 1)) for a, b in zip(self.certa, lugar))
        self.bloco.conta_pecas(certa)
        INVENTARIO.score(casa=self.certa, carta=src_id, move="DROP", ponto=certa, valor=0)

class Bloco(Elemento):
    def __init__(self, img, nx=4, ny=4, w=400, h=400, style=None, **kwargs):
        _style = dict(position="absolute", left=10, top=20,
            width=2*w+nx*10, height='%dpx'%(h+ny*10+100))
        _style.update(style) if style else None
        Elemento.__init__(self, img="",style=_style, **kwargs)
        self.repete = 0
        self.img = img
        *self.size = w, h
        self.dim = nx, ny, w, h
        self.ordem = list(range(nx*ny))
        self.tela = self.elt  # document["pydiv"]
        self.suporte = html.DIV(
            style=dict(position="absolute",
            left=10, top=20, width=w, height='%dpx'%h))
        self.folha = html.DIV(
            style=dict(position="absolute",
            left=w+20, top=20, width=w+nx*10, height='%dpx'%(h+ny*10)))
        self.contagem = html.DIV(style=dict(position="absolute",
                                 left=20, top=h+80))
        self.inicia_de_novo()

    def inicia_de_novo(self):
        #INVENTARIO.score(casa=self.img, carta=self.dim[0]*100+self.dim[1],
        #move="BLOCO", ponto=self.repete, valor=0)
        nx, ny,w, h = self.dim
        self.tela.html = self.suporte.html = self.folha.html = self.contagem.html = ""
        self.tela <= self.suporte
        self.tela <= self.folha
        self.tela <= self.contagem
        self.folhas = {}
        self.monta = lambda *_: None
        desordem = self.ordem[:]
        from random import shuffle
        shuffle(desordem)
        self.pecas_colocadas = []
        #print(list(enumerate(ordem)))
        for pos in self.ordem:
            Suporte(self, "suporte_{}_{}", pos%nx, pos//nx,
                    size=dict(width='{}%'.format(100/nx),
                    height='{}%'.format(100/ny)))
        for pos, tx in enumerate(desordem):
            Folha(self, pos%nx, pos//nx, int(tx)%nx, int(tx)//nx,
                    size=dict(width=w//nx, height=h/ny))
        self.repete += 1

    def conta_pecas(self, valor_peca):
        self.pecas_colocadas += [valor_peca//10]
        self.contagem.html = str(self.pecas_colocadas)
        if len(self.pecas_colocadas) >= len(self.folhas):
            if sum(self.pecas_colocadas)>= 20*len(self.folhas):
                alert("A resposta esta certa.")
                self.vai()
            else:
                vai = input("Tentar de novo?")
                if vai == "s":
                    self.inicia_de_novo()


class Puzzle:
    def __init__(self):
        self.cena = Cena(wod)
        self.sai = Cena(sai)
        self.puzzle = Bloco(oce, 4, 4, style=dict(left=10, top=100))
        self.puzzle.entra(self.cena)
        self.puzzle.vai = self.sai.vai
        self.cena.vai()

if __name__ == "__main__":
    #main()
    #Bloco(oce, 3, 3)
    Puzzle()