from utils import test


def chainage_arriere(base_fait,base_regle,but,trace=list()):
    tr = list()
    for b in but :
        if b in base_fait:
            tr.append('-1')
            continue
        for regle in base_regle:
            tr.append(regle.regle)
            if b in regle.conclusion:
                if test(regle.premisse,base_fait):
                    base_fait.append(b)
                    #print(b)
                    break
                else:
                    trace = chainage_arriere(base_fait,base_regle,regle.premisse,tr)
                    if not(trace == list()):
                        base_fait.append(b)
                        tr.append(trace)
                    else:
                        tr.remove(regle.regle)
                        
            else :
                tr.remove(regle.regle)
                #break
    return tr