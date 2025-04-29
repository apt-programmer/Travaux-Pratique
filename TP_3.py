
# Nom : Ait Douch
# Prenom : Hicham
# Group : 1

#$$$$$$$$$$$$$$$$$$$$$$$$$ Exercice 1 $$$$$$$$$$$$$$$$$$$$$$$$$ 
import random
import time

def bubble_sort(L):
    n = len(L)
    for i in range(n):
        for j in range(n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]

def insertion_sort(L):
    for i in range(1, len(L)):
        key = L[i]
        j = i - 1
        while j >= 0 and L[j] > key:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key

def test_sort(sort_func, size):
    L = [random.randint(0, 10_000) for _ in range(size)]
    start = time.time()
    sort_func(L.copy())
    return time.time() - start

sizes = [100, 500, 1000]
print("Temps en second : ")
for algo in [bubble_sort, insertion_sort]:
    print(f"\n{algo.__name__}:")
    for size in sizes:
        t = test_sort(algo, size)
        print(f"Size {size}: {t:.4f}")

#$$$$$$$$$$$$$$$$$$$$$$$$$ Exercice 2 $$$$$$$$$$$$$$$$$$$$$$$$$ 
import random
def merge_sort(L):
    if len(L) <= 1:
        return L
    
    mid = len(L) // 2
    left = merge_sort(L[:mid])  
    right = merge_sort(L[mid:]) 
    
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged

L = [random.randint(0, 100) for _ in range(6)]
print("Liste originale :", L)
print("Liste triée     :", merge_sort(L))

""""
Liste triée: [1, 2, 3, 5, 7, 9]
Arbre :
merge_sort([5, 2, 9, 3, 7, 1])
├─merge_sort([5, 2, 9])
│  ├─merge_sort([5])
│  └─merge_sort([2, 9])
│     ├─merge_sort([2])
│     └─merge_sort([9])
└─merge_sort([3, 7, 1])
   ├─merge_sort([3])
   └─merge_sort([7, 1])
      ├─merge_sort([7])
      └─merge_sort([1])
"""

#$$$$$$$$$$$$$$$$$$$$$$$$$ Exercice 3 $$$$$$$$$$$$$$$$$$$$$$$$$ 
def quick_sort(L):
    if len(L) <= 1:
        return L
    pivot = L[len(L)//2]  
    left = [x for x in L if x < pivot]
    middle = [x for x in L if x == pivot]
    right = [x for x in L if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


liste_quasi_triee = [1, 2, 3, 5, 4, 6, 7]  
liste_inversee = [7, 6, 5, 4, 3, 2, 1]

print("Quasi-triée:", quick_sort(liste_quasi_triee))
print("Inversée:", quick_sort(liste_inversee))
#! Liste quasi-triée meilleur cas :  O(n log n)
#! Liste inversée pire cas avec pivot central :  O(n²)

#$$$$$$$$$$$$$$$$$$$$$$$$$ Exercice 4 $$$$$$$$$$$$$$$$$$$$$$$$$ 
import random
import time
import matplotlib.pyplot as plt

def bubble_sort(L):
    n = len(L)
    for i in range(n):
        for j in range(n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]

def insertion_sort(L):
    for i in range(1, len(L)):
        key = L[i]
        j = i-1
        while j >=0 and key < L[j]:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = key

def merge_sort(L):
    if len(L) <= 1:
        return L
    mid = len(L)//2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    return result + left + right

def quick_sort(L):
    if len(L) <= 1:
        return L
    pivot = L[len(L)//2]
    left = [x for x in L if x < pivot]
    middle = [x for x in L if x == pivot]
    right = [x for x in L if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def test_sort(sort_func, L):
    start = time.time()
    sort_func(L.copy())
    return time.time() - start

sizes = range(1000, 10001, 1000)
algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort
}


results = {name: [] for name in algorithms}
for n in sizes:
    L = [random.randint(0, 10000) for _ in range(n)]
    for name, sort_func in algorithms.items():
        time_taken = test_sort(sort_func, L)
        results[name].append(time_taken)
        print(f"{name} - Taille {n}: {time_taken:.4f}s")


plt.figure(figsize=(10,6))
for name, times in results.items():
    plt.plot(sizes, times, label=name, marker='o')

plt.xlabel("Taille de la liste (n)")
plt.ylabel("Temps d'exécution (s)")
plt.title('Comparaison des algorithmes de tri')
plt.legend()
plt.grid(True)
plt.show()

#! Tri à bulles (O(n²))      :  - Courbe caractéristique en parabole .
#! Tri par insertion (O(n²)) : -Meilleur que le tri à bulles mais reste quadratique .
#! Tri fusion (O(n log n))   : -Courbe quasi-linéaire grâce à la division récursive .
#! Tri rapide (O(n log n) )  :  -Généralement le plus rapide en pratique .

#$$$$$$$$$$$$$$$$$$$$$$$$$ Exercice 5 $$$$$$$$$$$$$$$$$$$$$$$$$ 
import random
import time
import matplotlib.pyplot as plt

def linear_search(L, x):
    return next((i for i,v in enumerate(L) if v == x), -1)

def binary_search(L, x):
    l, h = 0, len(L)-1
    while l <= h:
        m = (l + h) >> 1
        if L[m] == x: return m
        l, h = (m+1, h) if L[m] < x else (l, m-1)
    return -1

def test():
    sizes = [10**3, 10**4, 10**5]
    res = {'lin_p':[], 'lin_a':[], 'bin_p':[], 'bin_a':[]}
    
    for n in sizes:
        L = sorted(random.sample(range(n*10), n))
        x_p, x_a = L[n//2], -1
        
        t = time.perf_counter()
        for _ in range(100):
            linear_search(L, x_p)
        res['lin_p'].append((time.perf_counter()-t)/100)
        
        t = time.perf_counter()
        for _ in range(100):
            linear_search(L, x_a)
        res['lin_a'].append((time.perf_counter()-t)/100)
        
        t = time.perf_counter()
        for _ in range(100):
            binary_search(L, x_p)
        res['bin_p'].append((time.perf_counter()-t)/100)
        
        t = time.perf_counter()
        for _ in range(100):
            binary_search(L, x_a)
        res['bin_a'].append((time.perf_counter()-t)/100)
    
    plt.figure(figsize=(10,5))
    for k,c,m in zip(res.keys(), 'brgm', 'ooss'):
        plt.plot(sizes, res[k], c+'-'+m, label=k)
    plt.xscale('log'); plt.yscale('log')
    plt.xlabel('n'); plt.ylabel('temps (s)')
    plt.legend(); plt.grid(); plt.show()

test()

#$$$$$$$$$$$$$$$$$$$$$$$$$ QUESTIONS $$$$$$$$$$$$$$$$$$$$$$$$$ 
#! 1-Dans quels cas Quick Sort peut-il devenir inefficace ? Comment y remédier ?
#  utiliser un pivot aléatoire ou la médiane de trois.

#! 2-Pourquoi Merge Sort garantit‐il toujours O(n log n) alors que Quick Sort non ?
#il divise toujours le tableau en deux moitiés égales, quel que soit le contenu.

#! 3-Quelle méthode de recherche choisiriez vous pour une liste extrêmement volumineuse ?
#Quick Sort car  est rapide en moyenne
