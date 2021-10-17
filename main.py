# This is a sample Python script.
import re
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def read_file(filename):
    file = open(filename,"r")
    propositions = file.readlines()
    file.close()
    return propositions

def split_propositions(propositions):
    base_regles = []
    for proposition in propositions:
        print(f"{proposition} 22")
        res = re.findall(r'\w+', proposition)
        myDict = {"premisse": res[1], "conclusion": res[3]}
        base_regles.append(myDict)
    return base_regles
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p1 = read_file("file.txt")
    print(split_propositions(p1))

