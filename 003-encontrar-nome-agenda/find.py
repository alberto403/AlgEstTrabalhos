
# Encontra o indice no array, assume que a lista esta ordenada
# Complexidade O(log n)
def find(array : list, low: int, high : int, value : str) -> int | None:
        middle = (low + high) // 2

        if low > high:
            return None

        if array[middle] == value:
            return middle

        elif array[middle] > value:
            return find(array=array, low=low, high=middle-1, value=value)
        elif array[middle] < value:
            return find(array=array, low=middle+1, high=high, value=value)
        
def main():
    array = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo", "Ze"]
    name = "Ana"
    index = find(array=array, low=0, high=len(array)-1, value=name)
    if index is not None:
        print(f"{name} encontrado no indice {index}")
    else:
        print(f"{name} nao encontrado")
    
if __name__ == "__main__":
    main()
    