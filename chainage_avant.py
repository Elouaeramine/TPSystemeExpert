from Fait import Fait
from utils import in_base, test


def chainage_avant(base_fait, base_regle, fait):
    tab_fait = list()
    # creation d'un tableau de fait
    for i in range(0, len(base_fait)):
        tab_fait.append(base_fait[i].fait)

    while not (in_base(base_fait, fait)):
        nb_fait = len(tab_fait)
        for i in range(0, len(base_regle)):

            prem = base_regle[i].premisse
            if test(prem, tab_fait):
                for k in range(0, len(base_regle[i].conclusion)):
                    base_fait.append(
                        Fait(base_regle[i].conclusion[k], base_regle[i].regle)
                    )
                    tab_fait.append(base_regle[i].conclusion[k].strip())

                base_regle.remove(base_regle[i])
                # print(tab_fait)
                break
        if nb_fait == len(tab_fait):
            break
    if fait in tab_fait:
        print(fait + " établi")
    else:
        print(fait + " non-établi")
