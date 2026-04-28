import random

def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for indice in range(len(array)):
        #gerar um número aleatório para a nova posição do elemento
        novaposicao = random.randint(0, len(array) - 1)
        #trocar o elemento da posição atual com o elemento da nova posição
        array[indice], array[novaposicao] = array[novaposicao], array[indice]
    print("Array embaralhado:", array)

if __name__ == "__main__":
    main()