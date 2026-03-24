# A variavel votos armazena os votos dos eleitores
votos = ['A', 'B', 'A', 'C', 'A', 'D', 'A', 'E', 'A', 'F']

def maisvotado (votos):
    # saldo de votos para o candidato
    saldo = 0
    candidato = votos [0]
    for voto in votos:
        # se o voto for para o candidato é adicionado 1 ao saldo
        if voto == candidato:
            saldo += 1
        # se o voto for para outro candidato é subtraido 1 ao saldo
        else:
            saldo -= 1
            # se o saldo for negativo, atualiza o candidato mais votado
            if saldo < 0:
                candidato = voto
                saldo = 1
    return candidato

def maioriaabsoluta (votos, candidato):
    saldo = 0
    for voto in votos:
        if voto == candidato:
            saldo += 1
        else:
            saldo -= 1
    if saldo > 0:
        return 0
    else:
        return 1

def eleicao (votos):
    candidato = maisvotado (votos)
    if maioriaabsoluta(votos, candidato) == 0:
        print (f'O candidato {candidato} venceu por maioria absoluta')
    else:
        print ('Nenhum candidato venceu por maioria absoluta')

eleicao (votos)