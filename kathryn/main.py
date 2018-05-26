# henrietta.kathryn.main.py
from _spy.vitollino.main import Cena, STYLE, NADA, NoEv, Popup
from _spy.vitollino.main import Texto as Text
from browser import html, doc, window, alert
OCEANO = "https://i.imgur.com/NRi5i6d.jpg"
STYLE["width"] = 800
STYLE["height"] = "400px"


class Plotter:
    def __init__(self, cena, tit=""):

        canvas = html.CANVAS()
        cena  <= canvas
        self.ctx = canvas.getContext("2d")
        self.tit = tit

        self.dataset = []
        self.axis()

        ## After doing this I saw that this could be achieved using
        ## translate(0,canvas.height); scale(1,-1);
        ## https://developer.mozilla.org/en-US/docs/HTML/Canvas/Tutorial/Transformations

    def change_ref_system(self, x, y):
        return (20 + x * 8, 240 - y * 20)
    
    
    def draw_line(self, x1, y1, x2, y2, linethick=3, color="black"):
        self.ctx.beginPath()
        self.ctx.lineWidth = linethick
        self.ctx.moveTo(x1, y1)
        self.ctx.lineTo(x2, y2)
        self.ctx.strokeStyle = color
        self.ctx.stroke()
    
    
    def axis(self, color="black", linethick=3):
        # Draw of x axis
        self.draw_line(20, 120, 240, 120, linethick=linethick, color=color)
        # Draw of y axis
        self.draw_line(20, 20, 20, 120, linethick=linethick, color=color)
        
    
    def figure_title(self):
        self.ctx.clearRect(410, 0, 400, 30)
        self.ctx.fillStyle = "gray"
        self.ctx.font = "bold 16px Arial"
        self.ctx.fillText(self.tit, 410, 20)
    
    
    def title_update(self, ev):
        self.figure_title()
    

    
    def graph(self, absiss, data):
        self.dataset.append((absiss, data))
        if len(self.dataset) == 1:
            x, y = self.change_ref_system(absiss, data)
            self.draw_line(x, y, x, y, linethick=3, color="blue")
        else:
            x1, y1 = self.change_ref_system(*self.dataset[-2])
            x2, y2 = self.change_ref_system(*self.dataset[-1])
            self.draw_line(x1, y1, x2, y2, linethick=3, color="blue")

    def plot(self, x, y):
        [self.graph(_x, _y) for _x, _y in zip(x, y)]



class Texto(Text):
    def __init__(self, cena=NADA, tit="", txt="", texto=None, foi=None, indo=None, **kwargs):
        super().__init__(cena=cena, tit=tit, txt=txt, foi=foi, **kwargs)
        #self.elt = Popup.POP.popup
        self.t = []
        self.cena, self.area = cena, html.DIV()
        if texto is not None:
            self.area = html.TEXTAREA(texto, Id="_TEXT_POPUP_", rows=4,
                style=dict(width='100%', resize=None))
            self.area.bind('keypress', self.indo)
        self._esconde = foi if foi else lambda:None
        self.indo = indo if indo else self.indo
        #cena <= self

    def _esconde(self, ev=NoEv()):
        ex.preventDefault()
        ev.stopPropagation()
        self._esconde()
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
        
    def sai(self, ev=NoEv()):
        j = '{}'.format(chr(172))
        t = self.area.value if self.area else ''
        return t, j.join(self.t)
        
    def indo(self, ev=NoEv()):
        char = ev.keyCode if ev.keyCode else ev.which
        self.t.append('{}{}{}'.format(chr(char),chr(181),str(window.Date.now())[-5:]))

class Game:
    def __init__(self):
        #self.elt = Popup.POP.popup
        self.cena = Cena(OCEANO)
        self.t = []
        foi=lambda *_:Texto(cena=self.cena, tit="score", txt="\n".join(self.texto.sai())).vai()
        #foi=lambda *_: alert("\n".join(self.texto.sai()))
        self.texto = Texto(cena=self.cena, tit="diga, com q paus a canoa?", texto="",
        foi=foi) #lambda *_:alert(self.texto.sai()[0])) #"\n".join(self.texto.sai())))
        self.cena.meio.vai = self.texto.vai
        #self.cena.vai = self.texto.vai
        self.cena.vai()
        # self.texto.vai()
        
    def indo(self, *_):
        self.t.append(self.texto.area.value)

Game()
