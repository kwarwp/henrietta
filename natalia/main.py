# henrietta.natalia.main.py
verbos_altos = ["ger", "atrit", "roç", "direcion", "friccion", "elev", "decid", "faz", "concl", "us",
                "remanej" ,"erg", "suspend", "ate", "esfreg", "trisc"] ==  3
verbos_medios = ["bat", "gir", "coloc", "manipul", "mov", "surg", "peg", "levant", "bat"] ==  2
verbos_fracos = ["rod", "bot", "sub", "pux", "form", "tent", "clic", "abaix", "mex", "encost", "rel"] ==  1
verbos = [321,verbos_altos,verbos_medios,verbos_fracos]

def avaliar(list):
    
    for x in verbos:
        print("da uma olhada", verbos.index(verbos_altos))
    
avaliar(verbos)
    
    
    
    