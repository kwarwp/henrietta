
""" Este algoritmo tem por intuito valorar as sentenÃ§as usuÃ¡rios da FonoComp Game"""

SUJEITO = ["eu"]
VERBO   = ["peg", "Tris","colh","rel","bat"]
OBJETO  = ["o oculos", "a pedr", "cascalhos", "galho", "arvore", "lupa", "raios solares"]

""" As variÃ¡veis: SUJEITO, VERBOS e OBJETOS remetem aos elementos que se esperam na construÃ§Ã£o das 
  sentenÃ§as no game. De inÃ­cio tomamos por relevante frases simples (sujeito + verbo + objeto)."""
  
ESTRUTURA1 = [SUJEITO + VERBO + OBJETO]
ESTRUTURA2 = [VERBO +SUJEITO + OBJETOS]
ESTRUTURA3 = [VERBO + OBJETOS+ SUJEITO]
ESTRUTURA4 = [SUJEITO + OBJETO + VERBO]
ESTRUTURA5 = [OBJETO + SUJEITO + VERBO]
ESTRUTURA6 = [OBJETO + VERBO + SUJEITO]
IMPLICITO  = [VERBO + OBJETO]

    """ As variÃ¡veis: ESTRUTURAX referem-se Ã s sentenÃ§as alvo, ou seja, as que deseja coletar.
         ESTRUTURA1 = Eu peguei o oculos. 3pts
         ESTRUTURA2 = Peguei eu o oculos. 2pts
         ESTRUTURA3 = Peguei o oculos eu. 1pts
         ESTRUTURA4 = Eu o oculos peguei. 1pts
         ESTRUTURA5 = O oculos eu peguei. 2pts
         ESTRUTURA6 = O oculos peguei eu. 1pts
         IMPLICITO  = Peguei o oculos.    3pt
    """
    
ESTRUTURAX=dict(E1 = "\U+0053" + "\U+0056" + "\U+004F",
             E2 = "\U+0056" + "\U+0053" + "\U+004F",
             E3 = "\U+0056" + "\U+004F" + "\U+0053",
             E4 = "\U+0053" + "\U+004F" + "\U+0056",
             E5 = "\U+004F" + "\U+0053" + "\U+0056",
             E5 = "\U+004F" + "\U+0056" + "\U+0053"
             IM = "\U+0056" + "\U+004F")
             
             #S = U + 0053
             #V = U+0056
             #O = U+
             
             
"""
SUJEITO = ["eu", "fui", "jornal"]

historia = "eu  fui  ao  barco ontem"



def responde(item, tree):
     """#FunÃ§Ã£o responsÃ¡vel por encontrar a estrutura, parear com a estrutura alvo, apontar o elemento nÃ£o 
     #encontrado e valorar a sentenÃ§a.
       
       #Type: param: object(item: list; tree: string)
       """
       
     
     
    branch = tree.split()
    for amora in item:
        if amora in branch:
            print("eba")
 
        else:
            print("not found:" + amora)
responde(SUJEITO, historia)


"""
            
            
            
            
            
            
            
            


SUJEITO = {"eu", "jornal", "elefante"}
VERBO = {"fui", "pesquei", "colhi", "fiz","peguei","pegar"}
OBJETO = {"oculos", "galho", "lupa"}

historia = "eu  fui  ao  barco ontem! pesquei dois peixes e depois de pegar um galho fiz fogo."



def responde(item, item2, item3, tree):

    branch = tree.split()

    for amora in branch:
         if set(SUJEITO)| set(VERBO) | set(OBJETO)  in branch:
             print("yuha")
         else:
             print("putz")

    """for amora in item:
        if amora in branch:
            print("eba:" + amora )

        else:
            print("not found:" + amora)

    for amora in item2:
        if amora in branch:
            print("eba:" + amora)
            #print("eba:" and amora)

        else:
            print("not found:" + amora)

    for amora in item3:
        if amora in branch:
            print("eba:" + amora )

        else:
            print("not found:" + amora)"""

responde(SUJEITO, VERBO, OBJETO, historia)
   
    
    
    

