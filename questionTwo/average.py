import random

listEle = []
def randomList(amount):
    while amount > 0:
        listEle.append(random.randint(1,10))
        amount -= 1
    return listEle

def averageList():
    sum  = 0
    for i in range(len(listEle)):
        sum += listEle[i]

    return sum / len(listEle)

def getListLen():
    return len(listEle)
