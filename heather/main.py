""" Este algoritmo tem por intuito valorar as sentenÃ§as usuÃ¡rios da FonoComp Game"""

SUJEITO = ["eu"]
VERBO = ["peg", "Tris", "colh", "rel", "bat"]
OBJETO = ["o oculos", "a pedr", "cascalhos", "galho", "arvore", "lupa", "raios solares"]

""" As variÃ¡veis: SUJEITO, VERBOS e OBJETOS remetem aos elementos que se esperam na construÃ§Ã£o das 
  sentenÃ§as no game. De inÃ­cio tomamos por relevante frases simples (sujeito + verbo + objeto)."""

ESTRUTURA1 = [SUJEITO + VERBO + OBJETO]
ESTRUTURA2 = [VERBO + SUJEITO + OBJETO]
ESTRUTURA3 = [VERBO + OBJETO + SUJEITO]
ESTRUTURA4 = [SUJEITO + OBJETO + VERBO]
ESTRUTURA5 = [OBJETO + SUJEITO + VERBO]
ESTRUTURA6 = [OBJETO + VERBO + SUJEITO]
IMPLICITO = [VERBO + OBJETO]
# estes aqui ajudam
ES1 = "SVO"
ES2 = "VSO"
ES3 = "VOS"
ES4 = "SOV"
ES5 = "OSV"
ES6 = "OVS"
IMP = "VO"

SYNTAX = [ES6, ES5, ES4, ES3, ES2, ES1]

""" As variÃ¡veis: ESTRUTURAX referem-se Ã s sentenÃ§as alvo, ou seja, as que deseja coletar.
     ESTRUTURA1 = Eu peguei o oculos. 3pts
     ESTRUTURA2 = Peguei eu o oculos. 2pts
     ESTRUTURA3 = Peguei o oculos eu. 1pts
     ESTRUTURA4 = Eu o oculos peguei. 1pts
     ESTRUTURA5 = O oculos eu peguei. 2pts
     ESTRUTURA6 = O oculos peguei eu. 1pts
     IMPLICITO  = Peguei o oculos.    3pt
"""

ESTRUTURAX = dict(E1="\u0053" + "\u0056" + "\u004F",
                  E2="\u0056" + "\u0053" + "\u004F",
                  E3="\u0056" + "\u004F" + "\u0053",
                  E4="\u0053" + "\u004F" + "\u0056",
                  E5="\u004F" + "\u0053" + "\u0056",
                  E6="\u004F" + "\u0056" + "\u0053",
                  IM = "\u0056" + "\u004F")

# S = U + 0053
# V = U+0056
# O = U+


"""
SUJEITO = ["eu", "fui", "jornal"]

historia = "eu  fui  ao  barco ontem"



def responde(item, tree):
     """  # FunÃ§Ã£o responsÃ¡vel por encontrar a estrutura, parear com a estrutura alvo, apontar o elemento nÃ£o 
# encontrado e valorar a sentenÃ§a.

# Type: param: object(item: list; tree: string)
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
VERBO = {"fui", "pesquei", "colhi", "fiz", "peguei", "pegar", "nada"}
OBJETO = {"oculos", "galho", "lupa", "lama"}
TAGGER = {tag: clazz for tag, clazz in zip(list("SVO"), (SUJEITO, VERBO, OBJETO))}
print("TAGGER", TAGGER)

PONTUA = "!,.?:"

historia = "eu  fui  ao  barco ontem! pesquei dois peixes e depois de pegar um galho fiz fogo."+\
"No rio, um elefante nadava na lama"


def responde(item, item2, item3, tree):
    # quebra em frases, toda a pontucao vira quebr de linha
    def remarcador_recursivo(_tree, pontua):
        _tree = _tree.replace(pontua.pop(), '\n')
        return remarcador_recursivo(_tree, pontua) if pontua else _tree

    tree = remarcador_recursivo(tree, list(PONTUA))
    print("remarcador_recursivo:", tree)
    # agora que todos os pontos viraram quebra de pagina (\n), podemos quebrar em frases
    # aproveitamos para quebrar cada frase em palavras
    tree_with_branches_and_berries = twbb = [branch.split() for branch in tree.split('\n')]
    tegged = []
    anytag = set(SUJEITO) | set(VERBO) | set(OBJETO)
    # vamos colocar as tags nas classes gramaticais
    tree_with_branches_and_tagged_berries = twbatb =[
        [(tag, amora) for amora in branch for tag, samples in TAGGER.items()
        if any(sample in amora for sample in samples)]
        for branch in tree_with_branches_and_berries]
    print("responde marcador:", tree_with_branches_and_tagged_berries)
    # vamos passar a janela de 2, dar dois pontos se encontrar IMP
    count =sum([2 for branch in twbatb for  (a, _), (b, _) in zip(branch, branch[1:]) if a+b in IMP])
    print("implicit:", count)
    # vamos passar a janela de 3, dar  pontos correspondendo à posição que o synt. estiver no SYNTAX
    count +=sum([pt+1 for branch in twbatb for  (a, _), (b, _), (c, _) in zip(branch, branch[1:], branch[2:])
                for pt, syntagma in enumerate(SYNTAX) if a+b+c in syntagma])
    print("plus syntax:", count)
    print("syntax", [a+b+c for branch in twbatb for  (a, _), (b, _), (c, _) in zip(branch, branch[1:], branch[2:])
                for pt, syntagma in enumerate(SYNTAX) if a+b+c in syntagma])

    """    for amora in branch:
         if amora   in branch:
             print("yuha")
         else:
             print("putz")

for amora in item:
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

    
    
    

