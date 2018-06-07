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
        self.corredor = CorredorDoTemplo() #significa que a entrada do templo esta conectada ao corredor
        
    def sai(self):
        Templo.sai(self) #sai do templo
        self.corredor.entra() # e entra no corredor
        
class CorredorDoTemplo(Templo):
    def __init__(self):#redefinindo em particular o init
        super().__init__()
        self.musica = SalaDoTemplo()#não vai poder ser templo pq não existem muitos templos
        self.oceano = SalaDoTemplo()
        self.floresta = SalaDoTemplo() #dever de casa entrar em alguma sala do templo, saindo do corredor
        
class SalaDoTemplo(Templo):
    def __init__(self):#redefinindo em particular o init
        super().__init__()
    
def mostra_templo():
    print("musica:{}, oceano:{}, floresta:{}, entrada:{}, corredor:{}".format(
        musica.entrou(), oceano.entrou(), 
        floresta.entrou(), entrada.entrou(), corredor.entrou())
        )
         #chaves significa lacuna
        #crianças escreva na lacuna se o menino entrou ou não        
        

#floresta.entra()
#oceano.entra()
entrada = EntradaDoTemplo()
corredor = entrada.corredor
#sala = SalaDoTemplo()
entrada.entra()
mostra_templo()
