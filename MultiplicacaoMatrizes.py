def verificar_matriz(matriz):
    # Verificar se a matriz é uma lista não vazia
    if not isinstance(matriz, list) or not matriz:
        raise ValueError("A matriz deve ser uma lista não vazia.")
    
    # Verificar se todas as linhas são listas do mesmo tamanho
    num_colunas = len(matriz[0])
    for linha in matriz:
        if not isinstance(linha, list) or len(linha) != num_colunas:
            raise ValueError("Todas as linhas da matriz devem ser listas do mesmo tamanho.")

def multiplicacao_matrizes(matriz1, matriz2):
    # Verificar se as matrizes são válidas
    verificar_matriz(matriz1)
    verificar_matriz(matriz2)

    # Verificar se as matrizes podem ser multiplicadas
    if len(matriz1[0]) != len(matriz2):
        raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")

    # Inicializar a matriz resultado com zeros
    resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]

    # Realizar a multiplicação
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado


def main():
    # Derfinir matrizes
    matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    resultado = multiplicacao_matrizes(matriz1, matriz2)
    print("Resultado da multiplicação das matrizes:")
    for linha in resultado:
        print(linha)

if __name__ == "__main__":
    main()