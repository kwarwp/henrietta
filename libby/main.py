# henrietta.libby.main.py
class Templo:
    def __init__(self):
        self._esta_no_templo = False
    def entra(self):
        self._esta_no_templo = True
        
    def sai(self):
        self._esta_no_templo = False
        
    def entrou(self):
        return self._esta_no_templo
        
class EntradaDoTemplo(Templo):
    def __init__(self):
        super().__init__()

        
musica = Templo()
oceano = Templo()
floresta = Templo()
floresta.entra()
oceano.entra()
entrada = EntradaDoTemplo()
entrada.entra()
print("musica:{}, oceano:{}, floresta:{}, entrada: {}".format(
        musica.entrou(), oceano.entrou(),
        floresta.entrou(), entrada.entrou()
        )
    )