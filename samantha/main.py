
SUJEITO = ["eu", "jornal", "elefante"]
VERBO = ["fui", "pesquei", "colhi", "fiz","peguei","pegar"]
OBJETO = ["oculos", "galho", "lupa"]

historia = "eu  fui  ao  barco ontem! pesquei dois peixes e depois de pegar um galho fiz fogo."



def responde(item, item2, item3, tree):

    branch = tree.split()

    """for amora in branch:
         if set(SUJEITO)| set(VERBO) | set(OBJETO)  in branch:
             print("yuha")
         else:
             print("putz")"""

    for amora in item:
        if amora in branch:
            print("eba:" + amora )

        else:
            del branch[amora]

    for amora in item2:
        if amora in branch:
            print("eba:" + amora)
            #print("eba:" and amora)

        else:
            del branch[amora]

    for amora in item3:
        if amora in branch:
            print("eba:" + amora )

        else:
            del branch[amora]

responde(SUJEITO, VERBO, OBJETO, historia)