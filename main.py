import re

# This function will read a file and returns an array of propositions.
def read_propositions(filename):
    file = open(filename, "r")
    propositions = file.readlines()
    file.close()
    return propositions


# This function will read a file and returns an array of faits.
def read_base_faits(filename):
    file = open(filename, 'r')
    faits = file.readline()
    res = faits.split(',')
    file.close()
    return res


# This Function will split an array of propositions to an object of premisses & conclusions
def split_propositions(propositions):
    base_regles = []
    for proposition in propositions:
        if 'et' in proposition:
            a = proposition.strip().split(' alors ')
            b =a[0][3::].split(' et ')
            print(f'proposition feha let ${b}')
            myDict = {"rule": propositions.index(proposition)+1, "premisse": b, "conclusion":a[1]}
            base_regles.append(myDict)
        else:
            print(f"{proposition} 22")
            res = re.findall(r'\w+', proposition)
            myDict = {"rule": propositions.index(proposition)+1, "premisse": res[1], "conclusion": res[3]}
            base_regles.append(myDict)
    return base_regles

# This Function will take into params base_faits & base_connaissance and will return any rule ( déclenchable )
# the search will start from the first element in base_connaissance
def regles_declenchables(bf , bc):
    declenchables = []
    #a = [d['premisse'] for d in bc]
    for element in bc :
        if element['premisse'] in bf:
            print(f'${element} mawjouda fel base faits')
            declenchables.append(element)
    return declenchables
# Press the green button in the gutter to run the script.
# This function will execute Chainage avant
def chainage_avant(base_fait,base_regle,but):

    if but in base_fait:
        print(f'${but} atteint..')
    else:
        print(f'${but} non atteint')


if __name__ == '__main__':
    #Read base connaissance
    p1 = read_propositions("file.txt")
    print(split_propositions(p1))
    #Read base faits
    f = read_base_faits("base_fait.txt")
    print(f)
    # Detecter les regles declenchables
    print(regles_declenchables(f, split_propositions(p1)))

