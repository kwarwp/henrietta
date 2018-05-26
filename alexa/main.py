#O algoritimo a seguir tem por intuito valorar as sentencas geradas pelos usuarios da FonoComp Game

DEBUG = False
# As variaveis a seguir remetem a ao arranjo de cada frase

ES1 = "SVO"
ES2 = "VSO"
ES3 = "VOS"
ES4 = "SOV"
ES5 = "OSV"
ES6 = "OVS"
IMP = "VO"

SYNTAX = [ES6, ES5, ES4, ES3, ES2, ES1]
_ = False

SUJEITO = {"eu", "jornal", "elefante"}
VERBO = {"fui", "pesquei", "colhi", "fiz", "peguei", "pegar", "nada"}
OBJETO = {"oculos", "galho", "lupa", "lama"}
TAGGER = {tag: clazz for tag, clazz in zip(list("SVO"), (SUJEITO, VERBO, OBJETO))}

PONTUA = "!,.?:"

historia = "eu  fui  ao  barco ontem! pesquei dois peixes e depois de pegar um galho fiz fogo."+\
"No rio, um elefante nadava na lama"


def responde(tree, item=SUJEITO, item1=VERBO, item2=OBJETO):
    # quebra em frases, toda a pontucao vira quebr de linha
    def remarcador_recursivo(_tree, pontua):
        _tree = _tree.replace(pontua.pop(), '\n')
        return remarcador_recursivo(_tree, pontua) if pontua else _tree

    tree = remarcador_recursivo(tree, list(PONTUA))
    print("remarcador_recursivo:", tree) if DEBUG else _
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
    print("responde marcador:", tree_with_branches_and_tagged_berries) if DEBUG else _
    # vamos passar a janela de 2, dar dois pontos se encontrar IMP
    
    
    count =sum([2 for branch in twbatb for  (a, _), (b, _) in zip(branch, branch[1:]) if a+b in IMP])
    print("implicit:", count) if DEBUG else _
    # vamos passar a janela de 3, dar  pontos correspondendo ÃÂÂÂÃÂÂÂÃÂÂÂÃÂÂÂ  posiÃÂÂÂÃÂÂÂÃÂÂÂÃÂÂÂ§ÃÂÂÂÃÂÂÂÃÂÂÂÃÂÂÂ£o que o synt. estiver no SYNTAX
    count +=sum([pt+1 for branch in twbatb for  (a, _), (b, _), (c, _) in zip(branch, branch[1:], branch[2:])
              for pt, syntagma in enumerate(SYNTAX) if a+b+c in syntagma])
    print("plus syntax:", count) if DEBUG else _
    
    def def_sintax():
               print("syntax", [a+b+c for branch in twbatb for  (a, _), (b, _), (c, _) in zip(branch, branch[1:], branch[2:])
                        for pt, syntagma in enumerate(SYNTAX) if a+b+c in syntagma])  if DEBUG else _
    return count

if __name__ == "__main__":
    #main()
    #Bloco(oce, 3, 3)
    DEBUG = True
    print("TAGGER", TAGGER)
    print("contagem:", responde(historia,SUJEITO, VERBO, OBJETO))
   


"""
SUJEITO = ["eu"]
VERBO = ["peg", "Tris", "colh", "rel", "bat"]
OBJETO = ["o oculos", "a pedr", "cascalhos", "galho", "arvore", "lupa", "raios solares"]

ESTRUTURA1 = [SUJEITO + VERBO + OBJETO]
ESTRUTURA2 = [VERBO + SUJEITO + OBJETO]
ESTRUTURA3 = [VERBO + OBJETO + SUJEITO]
ESTRUTURA4 = [SUJEITO + OBJETO + VERBO]
ESTRUTURA5 = [OBJETO + SUJEITO + VERBO]
ESTRUTURA6 = [OBJETO + VERBO + SUJEITO]
IMPLICITO = [VERBO + OBJETO]"""

    
    