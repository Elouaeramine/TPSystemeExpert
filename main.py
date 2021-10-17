# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def read_file(filename):
    file = open(filename,"r")
    print(file.readlines())
    propositions = file.readlines()
    file.close()
    return propositions


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_file("file.txt")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
