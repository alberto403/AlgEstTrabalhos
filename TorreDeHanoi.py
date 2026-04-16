# Algoritimo para solucionar o problema da Torre de Hanoi
def torre_de_hanoi(n, origem, destino, auxiliar, mov, inicial=False):
    """Move n discos da torre de origem para a torre de destino usando a torre auxiliar"""
    if inicial:
        print("Estado inicial:")
        printar_torres(origem, destino, auxiliar)
    if n == 1:
        disco = origem.pop()
        destino.append(disco)
        mov['count'] += 1
        print(f"Movimento {mov['count']}")
        input("Pressione ENTER para continuar...")
        printar_torres(origem, destino, auxiliar)
    else:
        torre_de_hanoi(n - 1, origem, auxiliar, destino, mov)
        disco = origem.pop()
        destino.append(disco)
        mov['count'] += 1
        print(f"Movimento {mov['count']}")
        input("Pressione ENTER para continuar...")
        printar_torres(origem, destino, auxiliar)
        torre_de_hanoi(n - 1, auxiliar, destino, origem, mov)

def criar_disco(tamanho):
    """Cria a representação visual de um disco"""
    return f"({'_' * tamanho}|{'_' * tamanho})"

def printar_torres(origem, destino, auxiliar):
    """Imprime as torres de forma visual com discos empilhados e pinos alinhados"""
    # Encontrar o maior disco para calcular largura máxima
    todos_discos = origem + destino + auxiliar
    max_disco = max(todos_discos) if todos_discos else 1
    largura = len(criar_disco(max_disco))
    
    # Encontrar a altura máxima necessária
    altura_max = max(len(origem), len(destino), len(auxiliar))
    
    print("\n")
    # Imprimir de cima para baixo
    for nivel in range(altura_max - 1, -1, -1):
        # Origem
        if nivel < len(origem):
            disco_str = criar_disco(origem[nivel])
        else:
            disco_str = "|".center(largura)
        print(disco_str, end="  ")
        
        # Destino
        if nivel < len(destino):
            disco_str = criar_disco(destino[nivel])
        else:
            disco_str = "|".center(largura)
        print(disco_str, end="  ")
        
        # Auxiliar
        if nivel < len(auxiliar):
            disco_str = criar_disco(auxiliar[nivel])
        else:
            disco_str = "|".center(largura)
        print(disco_str, end="  ")
        
        print()
    

    print("Origem".center(largura + 2), "Destino".center(largura + 2), "Auxiliar".center(largura + 2), "\n")

def main():
    numero_de_discos = int(input("Digite o número de discos: "))
    origem = list(range(numero_de_discos, 0, -1))
    destino = []
    auxiliar = []
    mov = {'count': 0}
    torre_de_hanoi(numero_de_discos, origem, destino, auxiliar, mov, inicial=True)
    print(f"Total de movimentos: {mov['count']}")

if __name__ == "__main__":
    main()