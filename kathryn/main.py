# henrietta.kathryn.main.py
from _spy.vitollino.main import Cena, STYLE, NADA, NoEv
from _spy.vitollino.main import Texto as Text
from browser import html, doc, window
OCEANO = "https://i.imgur.com/NRi5i6d.jpg"
STYLE["width"] = 800
STYLE["height"] = "400px"



class Texto(Text):
    def __init__(self, cena=NADA, tit="", txt="", texto="..", foi=None, indo=None, **kwargs):
        super().__init__(cena=cena, tit=tit, txt=txt, foi=foi, **kwargs)
        #self.elt = Popup.POP.popup
        self.t = []
        self.cena = cena
        self.area = html.TEXTAREA(texto, Id="_TEXT_POPUP_", rows=4, style=dict(width='100%', resize=None))
        self.esconde = foi if foi else self.esconde
        self.indo = indo if indo else self.indo
        self.area.bind('keypress', self.indo)
        #cena <= self

    def esconde(self, ev=NoEv()):
        ex.preventDefault()
        ev.stopPropagation()
        return False
        ...
    @classmethod
    def put_area(cls):
        if "_TEXT_POPUP_" in doc:
            return
        Popup.POP.area = html.DIV()
        Popup.POP.div <= Popup.POP.area
        Texto.put_area = lambda *_: None

    def vai(self, ev=NoEv()):
        # self.elt = Popup.POP.popup
        ev.stopPropagation()
        self.cena.elt <= Popup.POP.popup
        Texto.put_area()
        Popup.POP.area.html = ''
        Popup.POP.area <= self.area
        Popup.POP.mostra(lambda *_: None, self.tit, self.txt)
        Popup.POP.esconde = self.esconde
        return False
        
    def sai(self, ev):
        self.area.value, '¬'.join(self.t)
        
    def indo(self, ev):
        char = ev.keyCode if ev.keyCode else ev.wich
        self.t.append('{}µ{}'.format(char,str(window.Date.now())[-5:]))

class Game:
    def __init__(self):
        #self.elt = Popup.POP.popup
        self.cena = Cena(OCEANO)
        self.t = []
        self.texto = Texto(cena=self.cena, tit="diga,", txt='com q paus a canoa?',
        foi=lambda *_:Texto(cena=self.cena, tit="score,", texto="\n".join(self.texto.sai())).vai())
        self.cena.meio.vai = self.texto.vai
        #self.cena.vai = self.texto.vai
        self.cena.vai()
        self.texto.vai()
        
    def indo(self, *_):
        self.t.append(self.texto.area.value)
        
Game()
