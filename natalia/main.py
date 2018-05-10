# henrietta.natalia.main.py
verbos_altos = ["ger", "atrit", "roÃÂÃÂ§", "direcion", "friccion", "elev", "decid", "faz", "concl", "us",
                "remanej" ,"erg", "suspend", "ate", "esfreg", "trisc"] 
#verbos_altos ==  3
verbos_medios = ["bat", "gir", "coloc", "manipul", "mov", "surg", "peg", "levant", "bat"]
#==  2

verbos_fracos = ["rod", "bot", "sub", "pux", "form", "tent", "clic", "abaix", "mex", "encost", "rel"] 
#==  1

verbos = [123, verbos_altos,verbos_medios,verbos_fracos]

def avaliar(you):
    for they in you:
        if isinstance(they,list):
            print("da uma elevada:")
        else:
            return False
    
avaliar(verbos)
    
    
    
    