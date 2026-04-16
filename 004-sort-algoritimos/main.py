import time
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from insert_sort import insert_sort

nomes = [
    "Mariana", "Carlos", "Beatriz", "Felipe", "Juliana",
    "Roberto", "Amanda", "Lucas", "Fernanda", "Diego",
    "Patricia", "Gustavo", "Camila", "Henrique", "Larissa",
    "Thiago", "Vanessa", "Eduardo", "Natalia", "Bruno",
    "Renata", "Rodrigo", "Leticia", "Marcelo", "Sabrina",
    "Andre", "Claudia", "Leonardo", "Priscila", "Rafael"
]

print("Lista original:")
print(nomes)
print()

inicio = time.perf_counter()
resultado_bubble = bubble_sort(nomes.copy())
tempo_bubble = time.perf_counter() - inicio

inicio = time.perf_counter()
resultado_merge = merge_sort(nomes.copy())
tempo_merge = time.perf_counter() - inicio

inicio = time.perf_counter()
resultado_insert = insert_sort(nomes.copy())
tempo_insert = time.perf_counter() - inicio

print("Lista ordenada:")
print(resultado_bubble)
print()
print(f"Bubble Sort:    {tempo_bubble:.6f}s")
print(f"Merge Sort:     {tempo_merge:.6f}s")
print(f"Insert Sort:    {tempo_insert:.6f}s")
