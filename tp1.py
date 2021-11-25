from chainage_avant import chainage_avant
from utils import lire_fait, lire_regle, print_base_f, print_base_r

if __name__ == "__main__":
    base_fait = list()
    base_regle = list()
    but = str()
    while True:
        print(
            "q: quit\nf: changer base des faits\nr: changer base des regles\nb: but\np: parametre\ne: executer"
        )
        text = input("> ")
        if text == "q":
            break
        elif text == "f":
            base_fait = lire_fait()
            print_base_f(base_fait)
        elif text == "r":
            base_regle = lire_regle()
            print_base_r(base_regle)
        elif text == "b":
            but = input("Saisir vote but: ")
        elif text == "p":
            print("Base des faits:")
            print_base_f(base_fait)
            print("Base des regles:")
            print_base_r(base_regle)
            print("But: ", but)
        elif text == "e":
            chainage_avant(base_fait, base_regle, but)
