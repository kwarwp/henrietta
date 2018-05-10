# henrietta.natalia.main.py
from operator import eq
verbos_altos = ["ger", "atrit", "roÃÂÃÂ§", "direcion", "friccion", "elev", "decid", "faz", "concl", "us",
                "remanej" ,"erg", "suspend", "ate", "esfreg", "trisc"] 
verbos_altos ==  3
verbos_medios = ["bat", "gir", "coloc", "manipul", "mov", "surg", "peg", "levant", "bat"]
verbos_medios ==  2

verbos_fracos = ["rod", "bot", "sub", "pux", "form", "tent", "clic", "abaix", "mex", "encost", "rel"] 
verbos_fracos ==  1
verbos = [321,eq (3, verbos_altos),eq(2,verbos_medios),eq(1,verbos_fracos)]

def avaliar(you):
    for they in you:
        if isinstance(they,int):
            print("da uma elevada:", you.index("{}"))
        else:
             print(False)
    
avaliar(verbos)
    
    
    
    