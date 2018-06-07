# henrietta.libby.main.py
class A:
    def __init__(self):
        self.templo = False
    def entra(self):
        self.templo = True
        
    def sai(self):
        self.templo = False
        
musica = A()
oceano = A()
floresta = A()
print("musica:{}, oceano:{}, floresta:{}".format(musica.templo, oceano.templo, floresta.templo))