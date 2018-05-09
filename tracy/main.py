# henrietta.tracy.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE
from _spy.vitollino.main import INVENTARIO as inv
from browser import alert
STYLE["width"] = 600

TEMPLO = "http://3.bp.blogspot.com/-UsnGAupu3XM/VHvU2M5BHUI/AAAAAAAAdCE/UKbq_5dTM7k/s1600/IMG_6098.JPG"
CORREDOR = "http://i.muyinteresante.com.mx/dam/sociedad/historia/17/03/8/rabbit-hole-700-year-old-secret-knights-templar-cave-network-8-58c006f4a30df__880.jpg.imgo.jpg"
OCEANO = "https://freeclipartspot.com//storage/upload/ocean-clip-art/ocean-clip-art-51.jpg"
ALGA = "https://i.pinimg.com/originals/70/68/5f/70685fa634c3bb82a8eb5771a0a869ed.png"
CONCHA = "http://www.mat.uc.pt/~picado/conchas/imagens/p10.png"
AQUARIO = "https://www.tenstickers.pt/autocolantes-decorativos/img/preview/autocolante-decorativo-infantil-peixe-aquario-3634.png"

class Estados:
    def __init__(self):
        oceano = Cena(OCEANO)
        oceano.vai()
        
        
if __name__ == "__main__":
    Estados()
        