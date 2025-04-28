import random
import pyfiglet
from termcolor import colored

roulette = [i for i in range(37)]

budget_initial = 1000
budget = budget_initial
tours = 0

titre = pyfiglet.figlet_format("ROULETTE")
print(colored(titre, "green"))
print("#" * 52)
print("Bienvenue au jeu de roulette simplifié !")
print(f"Votre budget initial est de {budget} MAD.")
print("Essayez de maximiser vos gains. Bonne chance !")
print("#" * 52)

while budget > 0:
    print(f"Votre budget actuel est de {budget} MAD.")

    while True:
        try:
            choix_numero = int(input("Sur quel numéro souhaitez-vous parier (0-36) ? "))
            if 0 <= choix_numero <= 36:
                break
            else:
                print("Entrée invalide. Veuillez choisir un numéro entre 0 et 36.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier.")

    while True:
        try:
            mise = int(input("Combien souhaitez-vous miser ? "))
            if 1 <= mise <= budget:
                break
            else:
                print(f"Montant invalide. Veuillez miser un montant compris entre 1 et {budget} MAD.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un montant en chiffres.")

    print("La roue tourne...")
    resultat = random.choice(roulette)
    print(f"Et s'arrête sur le numéro {resultat} !")

    tours += 1
    if resultat == choix_numero:
        gain = mise * 35
        budget += gain
        print(f"Bravo ! Vous avez gagné {gain} MAD.")
    else:
        budget -= mise
        print(f"Dommage ! Vous avez perdu {mise} MAD.")

    print(f"Votre budget actuel est de {budget} MAD.")

    if budget == 0:
        print("Vous n'avez plus d'argent pour continuer.")
        break

    continuer = input("Souhaitez-vous continuer à jouer ? (oui/non) ").strip().lower()
    if continuer != "oui":
        break

print("Merci d'avoir joué !")
print(f"Votre budget final est de {budget} MAD.")
print(f"Nombre total de tours joués : {tours}")
print(colored(pyfiglet.figlet_format("À bientôt !"), "green"))


