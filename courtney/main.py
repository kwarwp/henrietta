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
        self.corredor = CorredorDoTemplo #significa que a entrada do templo esta conectada ao corredor
    def sai(self):
        Templo.sai(self) #sai do templo
        self.corredor.entra() # e entra no corredor
        
class CorredorDoTemplo(Templo):
    def __init__(self):#redefinindo em particular o init
        super().__init__()
        
class SalaDoTemplo(Templo):
    def __init__(self):#redefinindo em particular o init
        super().__init__()
    
        
        
musica = SalaDoTemplo()#não vai poder ser templo pq não existem muitos templos
oceano = SalaDoTemplo()
floresta = SalaDoTemplo()
floresta.entra()
oceano.entra()
entrada = EntradaDoTemplo()
corredor = CorredorDoTemplo()
sala = SalaDoTemplo()
print("musica:{}, oceano:{}, floresta:{}, entrada:{}, corredor:{}, sala: {}".format(
        musica.entrou(), oceano.entrou(), 
        floresta.entrou(), entrada.entrou(), corredor.entrou(), sala.entrou())
        )
         #chaves significa lacuna
        #crianças escreva na lacuna se o menino entrou ou não