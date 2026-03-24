# A variavel grafo representa o grafo do problema, onde as linhas representam pessoas
# e as colunas as relaçoes de cada pessoa com as outras
grafo = [[1,0,0,0,0,0,0,0,0,0],
         [1,1,0,0,0,0,0,0,0,0],
         [1,0,1,0,0,0,0,0,0,0],
         [1,0,0,1,0,0,0,0,0,0],
         [1,0,0,0,1,0,0,0,0,0],
         [1,0,0,0,0,1,0,0,0,0],
         [1,0,0,0,0,0,1,0,0,0],
         [1,0,0,0,0,0,0,1,0,0],
         [1,0,0,0,0,0,0,0,1,0],
         [1,0,0,0,0,0,0,0,0,1]]

# Verifica se grafo é uma variavel adequada
def verificacao_grafo (grafo):
    for indice, pessoa in enumerate (grafo):
        # verifica se o grafo é uma matriz quadrada
        if len (pessoa) != len (grafo):
            return 1
        # verifica se todos os termos da diagonal central são 1 (cada pessoa conhece ela mesma)
        elif pessoa [indice] != 1:
            return 2
    return 0

# Função recebe a variavel grafo e retorna o indice da possivel celebridade
def candidato_celebridade (grafo):
    candidato = 0
    for indice, pessoa in enumerate (grafo):
        # se a pessoa não conhece o candidato ela se torna o candidato
        if pessoa [candidato] == 0:
            candidato = indice
    return candidato

def verificar_candidato (grafo, candidato):
    for pessoa in grafo:
        # verifica se pessoa conhece o candidato
        if pessoa [candidato] == 0:
            return False
    # verifica se o candidato conhece alguem
    for indice, conhecido in enumerate (grafo [candidato]):
        if indice != candidato and conhecido == 1:
            return False
    return True

def celebridade (grafo):
    verificacao = verificacao_grafo (grafo)
    if verificacao == 1:
        print ('A variavel grafo deve ser uma matriz quadrada')
    elif verificacao == 2:
        print ('Os termos da diagonal principal devem ser iguais a 1')
    else:
        candidato = candidato_celebridade (grafo)
        if verificar_candidato (grafo, candidato) == False:
            print ('Não há celebridade')
        else:
            print (f'A celebridade é a pessoa {candidato + 1}')

celebridade (grafo)