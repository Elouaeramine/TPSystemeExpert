from Fait import Fait
from Regle import Regle


def lire_fait():
    file = input("Veuillez sélectionner la base des faits: ")
    f= open(file,"r")
    line =f.readline().strip()
    base_fait = list()
    while line: 
        base_fait.append(
            Fait(line,-1) 
        )
        line = f.readline().strip()
        
    f.close()
    return base_fait

def lire_regle():
    file = input("Veuillez sélectionner la base des regles: ")
    f= open(file,"r")
    line =f.readline()
    base_regle = list()
    while line : 
        aux = line.split(":")
        regle = aux[0].strip()
        premisse = aux[1][ 
            aux[1].find("si") +2 : 
            aux[1].find("alors")
        ].strip().split(' et ')
        conclusion = aux[1].split('alors')[1].strip().split("et")
        base_regle.append(
            Regle(
                regle,
                premisse,
                conclusion
            )
        )
        line =f.readline()
    f.close()
    return base_regle

def in_base(base_fait,fait):
    for i in range(0,len(base_fait)):
        if fait == base_fait[i].fait :
            return True
    return False

def test(prem,tab):
    for j in range(0,len(prem)):
        if not(prem[j] in tab):
            return False
    return True

def print_base_f(base):
    for index in range (0, len(base)):
        base[index].print_fait()
        print("----------------------")

def print_base_r(base):
    for index in range (0, len(base)):
        base[index].print_regle()
        print("----------------------")
