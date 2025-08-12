import mergesort as mg
import random
from time import process_time
# Contagem de Operações:

# Algoritimo MergeSort:

print("Iniciando MergeSort...")
MAX = 10000
for num in range(1, MAX):
    data = [random.randint(0,MAX*10) for x in range(MAX)]

start = process_time()
mg.mergeSort(data)
end = process_time()
t = end-start

print(f"Tempo para ordenar {MAX} elementos: {t} s")

# Algoritimo QuickSort:

# Algoritimo BubbleSort: