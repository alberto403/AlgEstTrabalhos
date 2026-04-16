def bin_sort(array):
    if len(array) <= 1:
        return array

    # Encontrar o número máximo para determinar o número de dígitos
    max_value = max(array)
    if max_value == 0:
        return array

    # Determinar o número de dígitos do maior número
    num_digits = 0
    temp = max_value
    while temp > 0:
        num_digits += 1
        temp //= 10

    # Para cada dígito (começando do menos significativo)
    for digit in range(num_digits):
        # Criar 10 buckets (0-9) para este dígito
        buckets = [[] for _ in range(10)]

        # Distribuir os números nos buckets baseado no dígito atual
        for num in array:
            # Extrair o dígito na posição atual
            digit_value = (num // (10 ** digit)) % 10
            buckets[digit_value].append(num)

        # Reconstruir o array a partir dos buckets
        array = []
        for bucket in buckets:
            array.extend(bucket)

    return array

def main():
    array = [75, 84, 36, 68, 18, 9, 99, 98, 15, 75, 30, 45, 60, 72, 81, 27, 54, 63, 12, 21]
    print("Array original:")
    print(array)
    array_ordenado = bin_sort(array)
    print("Array ordenado:")
    print(array_ordenado)

if __name__ == "__main__":
    main()