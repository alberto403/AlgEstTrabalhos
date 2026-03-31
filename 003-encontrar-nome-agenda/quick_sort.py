# Algoritmo de ordenação Quick Sort
# Complexidade O(n log n) no melhor caso, O(n^2) no pior caso
def quick_sort(array : list, low : int, high : int) -> list:

    if high - low < 1:
        return array
    
    pivot_index = partition(array=array, low=low, high=high)

    # Ordena antes do pivot
    quick_sort(array, low, pivot_index-1)

    # Ordena depois do pivot
    quick_sort(array, pivot_index + 1, high)
    
    


def partition(array : list, low : int, high : int) -> int:
    pivot = array[high]
    i = low - 1 # ponteiro dos menores que o pivot
    
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            temp_value = array[i]
            array[i] = array[j]
            array[j] = temp_value

    # Coloca o pivot na posicao certa
    new_pivot_index = i + 1
    temp_value = array[new_pivot_index]
    array[new_pivot_index] = pivot
    array[high] = temp_value

    return new_pivot_index

def main():
    array = ["Ze","Carlos", "Ana", "Bruno", "Diana", "Eduardo"]
    quick_sort(array=array, low=0, high=len(array)-1)
    print(array)

if __name__ == "__main__":
    main()
     
        
