# henrietta.natalia.main.py
historia = "eu friccionei a pedra e gerou fogo"
verbos_altos = ["ger", "atrit", "roÃÂÃÂÃÂÃÂ§", "direcion", "friccion", "elev", "decid", "faz", "concl", "us",
                "remanej" ,"erg", "suspend", "ate", "esfreg", "trisc"] 
verbos_altos ==  3
verbos_medios = ["bat", "gir", "coloc", "manipul", "mov", "surg", "peg", "levant", "bat"]
verbos_medios ==  2

verbos_fracos = ["rod", "bot", "sub", "pux", "form", "tent", "clic", "abaix", "mex", "encost", "rel"] 
verbos_fracos ==  1
verbos = [ (3,verbos_altos),(2,verbos_medios),(1,verbos_fracos)]

def avaliar(you):
    pontuacao = 0
    for peso,verbo in verbos:
        for prefixo in verbo:
            pontuacao += peso if prefixo in you else 0 
    return pontuacao
    
            
    
print(avaliar(historia))
    
    
    
    