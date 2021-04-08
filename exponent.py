print(2**3)  #2^3

def raiseToPower(baseNum,powerNum):
    res = 1
    for i in range(powerNum):
        res = res * baseNum
    return res

print(raiseToPower(6,2))