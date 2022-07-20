import random


array = []
newArray = []
nDiv = 0


def div():
    global nDiv
    global newArray, array
    countElementArray = len(array)
    print(countElementArray)
    for d in range(nDiv):
        newArray.append([])
    pair = countElementArray % 2
    opDiv = countElementArray/nDiv
    print(f"opt value {opDiv}")
    if(pair == 0):
        addElement(countElementArray, opDiv)
    else:
        opDiv = int(opDiv)
        print(opDiv)
        addElement(countElementArray, opDiv)



def addElement(countArray, nElementArray,):
    global newArray, array
    position = 0
    count = 0
    for ca in range(countArray):
        if(count < nElementArray):
            newArray[position].append(array[ca])
            count +=1
        else:
            count = 0
            position +=1
            newArray[position].append(array[ca])



def randomGenerator(nElements, nStart, nEnd):
    global array
    for e in range(nElements):
        nRandom = random.randint(nStart, nEnd)
        array.append(nRandom)
    return array


def main():
    global nDiv
    nDiv = int(input("numero de elemtos a dividir: "))
    nRandoms = int(input("numero de elementos randoms: "))
    nStart = int(input("numero inicial: "))
    nEnd = int(input(f"numero de rango final, mayor a {nStart}: "))
    print(f"{randomGenerator(nRandoms,nStart,nEnd)}")
    div()
    print(newArray)


main()