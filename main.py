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

def generate_base_faits(faits):
    return [(fait, "-1") for fait in faits]

# This Function will split an array of propositions to an object of premisses & conclusions
def split_propositions(propositions):
    base_regles = []
    for proposition in propositions:
        if 'et' in proposition:
            a = proposition.strip().split(' alors ')
            b =a[0][3::].split(' et ')
            #print(f'proposition feha let ${b}')
            myDict = {"rule": propositions.index(proposition)+1, "premisse": b, "conclusion":a[1]}
            base_regles.append(myDict)
        else:
            #print(f"{proposition} 22")
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
        if (isinstance(element['premisse'],str)):
            if element['premisse'] in bf :
                declenchables.append(element)
        else:
            if all(x in bf for x in element['premisse']):
                #print(f'${element} mawjouda fel base faits')
                declenchables.append(element)
    return declenchables

def regle_prioritaire(base_regles):
    return base_regles[0]
# Press the green button in the gutter to run the script.
# This function will execute Chainage avant
def chainage_avant(base_fait,base_regle,but):
    iter = 0
    faits = generate_base_faits(base_fait)
    rd = regles_declenchables(base_fait,base_regle)

    while (but not in base_fait) and (rd!=0):

        if (len(rd) > 1 ):
            regle = regle_prioritaire(rd)
        elif (len(rd) ==1):
            regle = rd[0]

        logs = open("logs.txt","a")
        logs.writelines(f"itration :{iter} ; les regles declenchables sonts : {rd} ; la règle déclenchée est : {regle}; la conclusion : {regle['conclusion']}")
        logs.close()

        #regles = base_regle.remove(regle)
        regles = [ i for i in base_regle if not (i['rule'] == regle['rule'])]
        print(regles)
        faits.append((regle['conclusion'], regle['rule']))
        base_fait.append(regle['conclusion'])

        f = open('logs.txt', 'a')
        f.write('la nouvelle base des faits est: ' + str(base_fait) + '\n')
        f.close()

        rd = regles_declenchables(base_fait, regles)
        iter+=1
    if but in base_fait:
        print(f'${but} atteint..')
        print("la base des faits est ", base_fait)
    else:
        print(f'${but} non atteint')
        print("la base des faits est ", base_fait)


if __name__ == '__main__':
    #Read base connaissance
    p1 = read_propositions("file.txt")
    #print(split_propositions(p1))
    #Read base faits
    f = read_base_faits("base_fait.txt")
    #print(f)
    # Detecter les regles declenchables
    #print(regles_declenchables(f, split_propositions(p1)))

    #appliquer chainage avant
    chainage_avant(f,split_propositions(p1),"pingouin")

