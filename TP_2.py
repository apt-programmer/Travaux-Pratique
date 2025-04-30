


# Nom : Ait Douch
# Prenom : Hicham
# Group : 1

#$$$$$$$$$$$$$$$$$$$$$$$$$ Exercice 1 $$$$$$$$$$$$$$$$$$$$$$$$$ 
def puissance(x,n) :
    if n == 1: return x
    elif n % 2 == 0: return puissance(x * x, n / 2)
    else: return x * puissance(x * x, (n - 1) / 2)

print(puissance(1,13))
print(puissance(3,2))
print(puissance(3,5))

#$$$$$$$$$$$$$$$$$$$$$$$$$ Exercice 2 $$$$$$$$$$$$$$$$$$$$$$$$$ 
def base2(n) :
    if n == 0: return [0]
    if n == 1: return [1]
    return  [n % 2] + base2(n // 2) 

print(base2(3))

def base10(a):
    
    if isinstance(a, int): 
        a = [int(digit) for digit in str(a)]
        return base10(a)

    if len(a) == 0: return 0
    return a[-1] + 2 * base10(a[:-1])

print(base10([1,1,0]))
print(base10(1111))

#$$$$$$$$$$$$$$$$$$$$$$$$$ Exercice 3 $$$$$$$$$$$$$$$$$$$$$$$$$ 
taille_list = lambda L: len(L)
sum_list = lambda L : float(sum(L))
inv_list = lambda L : list(reversed(L))
sort_list = lambda L: sorted(L)
count_item = lambda L, x: L.count(x)
index_item = lambda L, x: L.index(x) if x in L else -1

L = [3, 7, 4, 8, 3, 7, 9, 18, 3, 6]

print("Taille :", taille_list(L))   
print("Somme :", sum_list(L))       
print("Inversée :", inv_list(L))    
print("Liste triée :", sort_list(L))
print("Nombre de fois que 3 apparaît :", count_item(L, 3))
print("Indice de 7 :", index_item(L, 7))

#$$$$$$$$$$$$$$$$$$$$$$$$$ Exercice 4 $$$$$$$$$$$$$$$$$$$$$$$$$ 
def strcpy(src,dest=""):
    if len(src) == 0 : return dest
    return strcpy(src[1:], dest + src[0])
    
def strcpm(ch1,ch2) :
    if ch1 > ch2:   return 1
    elif ch1 < ch2: return -1
    else:           return 0

def anagramme(ch1, ch2) :
    if len(ch1) != len(ch2): return False
    if len(ch1) == 0:        return True
    if ch1[0] in ch2:
        ch2 = ch2.replace(ch1[0], '', 1)
        return anagramme(ch1[1:], ch2)
    return False


print(strcpy("scala"))
print(strcpm("GO","go"))
print(anagramme("Ruby","Rust"))
'''
#$$$$$$$$$$$$$$$$$$$$$$$$$ Exercice 5 $$$$$$$$$$$$$$$$$$$$$$$$$
#!1 
'''
def factorielle(n) :
    x = 1
    for i in range(n,1,-1) :
        x *= i
    return f"factorielle de {n} : {x}"

n = int(input("Entrez la valeur de a : "))
print(factorielle(n))

#!2
def divise(A,B) :
    rep = "faux"
    if (A%B) == 0 : rep = "vrai"
    return rep

A = int(input("Entrez un entier a : "))
B = int(input("Entrez un entier b : "))
print(divise(A, B))

#!3
def division(a,b):
    try  : 
        quotient = a // b
        reste = a % b 
        print(f"quostient de {a,b} est : {quotient} ")
        print(f"reste de {a,b} est : {reste} ")
    except :
        print("Erreur : division par zéro.")

a = int(input("Entrez un entier a : "))
b = int(input("Entrez un entier b : "))
division(a,b)

#!4
def est_carre_parfait(n):
    if n < 0:
        return False, None

    for i in range(n // 2 + 2):
        if i * i == n:
            return True, i
    return False , "rien"

n = int(input("Entrez la valeur de n : "))
est_carre, racine = est_carre_parfait(n)

if est_carre:
    print(f"{n} est un carré parfait. Sa racine est {racine}.")
else:
    print(f"{n} n'est pas un carré parfait.")

#!5
def est_carre_parfait(x):
    if x < 0:
        return False, None
    for i in range(x // 2 + 2):
        if i * i == x:
            return True, i
    return False, None

def carres_parfaits(liste):
    somme = 0
    produit = 1
    a_trouve = False

    for nombre in liste:
        carre, racine = est_carre_parfait(nombre)
        if carre:
            somme += racine
            produit *= racine
            a_trouve = True

    if not a_trouve:
        print("Aucun carré parfait trouvé.")
        return

    somme_est_carre, racine_somme = est_carre_parfait(somme)
    produit_est_carre, racine_produit = est_carre_parfait(produit)

    print(f"Somme des racines carrées : {somme}")
    if somme_est_carre:
        print(f"La somme {somme} est un carré parfait de racine {racine_somme}.")
    else:
        print(f"La somme {somme} n'est pas un carré parfait.")

    print(f"Produit des racines carrées : {produit}")
    if produit_est_carre:
        print(f"Le produit {produit} est un carré parfait de racine {racine_produit}.")
    else:
        print(f"Le produit {produit} n'est pas un carré parfait.")


liste = [3, 9, 14, 25, 47, 93, 4]
carres_parfaits(liste)


from math import *
def carres_parfaits(liste) :
    somme = 0
    produit = 1
    for i in liste:
         if i > 0:
            for j in range( i// 2 + 2):
                if j * j == i :
                    somme += sqrt(i)
                    produit *= sqrt(i)
    for i in range(somme//2+2) :
        if i * i == somme :
            print("la somme des racines carrées sont des carrée parfaists ")
    for i in range(produit//2+2) :
        if i * i == produit :
            print("le produit des racines carrées sont des carrée parfaists ")
            pass
    print(f"la somme des racines carrées : {somme}  ")
    print(f"le produit des racines carrées : {produit}")

liste = [3,9,14,25,47,93,4]   
carres_parfaits(liste)


#!6

def permuter(a, b):
    return b, a

def remplir_tableau():
    tableau = []
    for i in range(100):
        valeur = int(input(f"Entrez la valeur {i+1} : "))
        tableau.append(valeur)
    return tableau

def afficher_tableau(tableau):
    for i, valeur in enumerate(tableau):
        print(f"Element {i+1}: {valeur}")

def trier_tableau(tableau):
    n = len(tableau)
    for i in range(n):
        for j in range(0, n-i-1):
            if tableau[j] > tableau[j+1]:
                tableau[j], tableau[j+1] = permuter(tableau[j], tableau[j+1])
    return tableau


print("Remplissage du tableau:")
mon_tableau = remplir_tableau()
    
print("Tableau avant tri:")
afficher_tableau(mon_tableau)
    
print("Tri du tableau...")
mon_tableau_trie = trier_tableau(mon_tableau)
    
print("Tableau après tri:")
afficher_tableau(mon_tableau_trie)
'''
#!7
def calcul_cout_en_km(km):
    
    if km <= 100:
        return km * 1
    elif km <= 1000:
        return 100 * 1 + (km - 100) * 2
    else:
        return 100 * 1 + 900 * 2 + (km - 1000) * 5

def calcul_cout_forfait(jours):
    return jours * 250

def comparer_tarifs():
    print("Comparaison des tarifs de location ")
    
    jours = int(input("Entrez le nombre de jours de location : "))
    km = float(input("Entrez le nombre total de kilomètres parcourus : "))
    
    cout_km = calcul_cout_en_km(km)
    cout_forfait = calcul_cout_forfait(jours)
    
    print(f"Coût location au kilomètre: {cout_km:.2f} MAD")
    print(f"Coût forfait journalier: {cout_forfait:.2f} MAD")
    
    if cout_km < cout_forfait:
        print("La location au kilomètre est plus avantageuse !")
    elif cout_forfait < cout_km:
        print("Le forfait journalier est plus avantageux !")
    else:
        print("Les deux options ont le même coût.")

comparer_tarifs()

#!$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
