# henrietta.courtney.main.py
class Templo:
    def __init__(self):
        self._esta_no_templo = False
    def entra(self):#essa é a ordem
        self._esta_no_templo = True
        
    def sai(self):#isso se chama metodo
        self._esta_no_templo = False
        
    def entrou(self):#isso se chama metodo pra saber se entrou
        return self._esta_no_templo #retorne o valor de self templo
        
class EntradaDoTemplo(Templo):
    def __init__(self):#redefinindo em particular o init
        super().__init__()
    
        
        
musica = Templo()
oceano = Templo()
floresta = Templo()
floresta.entra()
oceano.entra()
entrada = EntradaDoTemplo()
print("musica:{}, oceano:{}, floresta:{}, entrada:{}".format( #chaves significa lacuna
        musica.entrou(), oceano.entrou(), 
        floresta.entrou(), entrada.entrou()
        )
        #crianças escreva na lacuna se o menino entrou ou não