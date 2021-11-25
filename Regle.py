class Regle:
    def __init__(self,regle,premisse,conclusion):
        self.regle = regle 
        self.premisse = premisse
        self.conclusion = conclusion

    def print_regle(self):
        print("reg:",self.regle)
        print("prem: ",self.premisse )
        print("conc :", self.conclusion)
