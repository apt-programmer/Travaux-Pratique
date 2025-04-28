


#$$$$$$$$$$$$$$$$$$$$$$$$$ Exercice 2 $$$$$$$$$$$$$$$$$$$$$$$$$ 
def power(base,exponent=2):
    puissance = base**exponent
    return puissance if exponent > 0 else float(puissance)

print(power(5))
print(power(base=3, exponent=4))
print(power(2, exponent=5))

base = int(input("Enter la base : "))
exponent = int(input("Enter exponent : "))
print(f"Le result de {base} au puissance {exponent} ese : " , power(base,exponent))


#$$$$$$$$$$$$$$$$$$$$$$$$$ Exercice 2 $$$$$$$$$$$$$$$$$$$$$$$$$ 
def power(base,exponent=2):
    puissance = base**exponent
    return puissance if exponent > 0 else float(puissance)
f1 = power

def scale(x,factor=1.2):
    return x*factor
f2 = scale

def apply_all(funcs, value) :
    reponse = []
    for func in funcs :
        reponse.append(func(value))
    return reponse

print(apply_all((f1,f2),10))


#$$$$$$$$$$$$$$$$$$$$$$$$$ Exercice 3 $$$$$$$$$$$$$$$$$$$$$$$$$ 
def summurize(*args, **kwargs):
    precision = kwargs.get('precision', 2)
    verbose = kwargs.get('verbose', False)

    somme = round(sum(args), precision)
    moyenne = round(sum(args) / len(args), precision)

    if verbose:
        print(f"Valeurs reçues : {args}")
        print(f"Somme : {somme}")
        print(f"Moyenne : {moyenne}")   

    return f"La somme est {somme} et la moyenne est {moyenne}"

args = [5, 10, 15]
print(summurize(*args, precision=2, verbose=True))

#$$$$$$$$$$$$$$$$$$$$$$$$$ Exercice 4 $$$$$$$$$$$$$$$$$$$$$$$$$ 
def append_item(lst, item):
    lst.append(item)

def increment(n):
    n += 1
    return n

a  , b = [1, 2] , 5

print("Avant appel :")
print("a =", a) , print("b =", b)

append_item(a, 3)
increment(b)

print("Apres appel :")
print("a =", a) ,print("b =", b)

print("""a est une liste :
       objet mutable modifiés à l'intérieur d'une fonction""")
print("""b est un entier :
       objet immutable  ne changent pas l'intérieur d'une fonction""")

def append_item(lst, item):
    return lst + [item]

print(append_item(a, 3))
print( a )

#$$$$$$$$$$$$$$$$$$$$$$$$$ Exercice 5 $$$$$$$$$$$$$$$$$$$$$$$$$ 

counter = 0

def increase(n):
    global counter
    counter += n
    return counter

def local_increase(n):
    counter = 0
    counter += n
    return counter

print(f"counter = {counter}")

print("Appel à increase(5)")
print("increase = ", increase(5))
print(f"counter = {counter}")

print("local_increase = ", local_increase(3))
print(f"counter = {counter}")

print("""l'impact de global est modifie la variable globale counter
       changements  dans tout le programme  """)
print(""" on évite les variables globales parce que les fonctions qui
       dépendent de variables globales changent tjr les valeurs de sortie  """)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 