from chainage_arriere import chainage_arriere
from utils import lire_fait, lire_regle, print_base_f, print_base_r, test

if __name__ == "__main__":
    base_fait = list()
    base_regle = list()
    trace = list()
    but = str()
    while True:
        print(
            "f: Changer base des faits\nr: Changer base des regles\nb: Saisir but\np: Afficher les parametres\nt: Afficher la trace\ns: Sauvgarder la trace\ne: Executer\nq: Quitter\n"
        )
        text = input("> ")
        if text == "q":
            break
        elif text == "f":
            base_fait = lire_fait()
            # print_base_f(base_fait)
        elif text == "r":
            base_regle = lire_regle()
            # print_base_r(base_regle)
        elif text == "b":
            but = input("Saisir vote but: ")

        # elif text=="chainage avant: ":
        # trace = chainage_avant(base_fait,base_regle,but)

        elif text == "p":
            print("Base des faits:")
            print_base_f(base_fait)
            print("Base des regles:")
            print_base_r(base_regle)
            print("But: ", but)

        elif text == "t":
            print(trace)

        elif text == "s":
            print(trace)
            f = open("trace.txt", "w")
            tr = str(trace)
            f.write(tr)
        elif text == "e":
            tab_fait = list()
            # creation d'un tableau de fait
            for ft in base_fait:
                tab_fait.append(ft.fait)

            trace = list()
            b = list()
            b.append(but)
            # print(b)
            tr = chainage_arriere(tab_fait, base_regle, b, trace)
            if len(tr) != 0:
                print("But atteint")
                trace = tr
            else:
                print("But non atteint")
