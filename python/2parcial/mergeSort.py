import random


array = []
newArray = []
nDiv = 0
nPosition = 0
nElement = 0
subArray = 0
div = 2


def divN():
    global newArray, array, nDiv
    countElementArray = len(array)
    for d in range(nDiv):
        newArray.append([])
    opDiv = countElementArray/nDiv
    addElement(opDiv, 0, array, countElementArray)


def divTwo():
    global newArray, nDiv, nPosition, nElement, subArray, div
    for i in range(len(newArray)):
        countElement = len(newArray[i])
        if (subArray > div or subArray == 0):
            newArray.append([])
            subArray = 1
            nElement = 0


        if (nElement == countElement):
            #nPosition +=1
            nElement = 0

        if(i <= nDiv):
            addElement(countElement, -1, newArray[i], countElement)
            nElement += 1
            subArray +=1
            divTwo()

    

def addElement(nElementArray, startPosition, arrays, range_):
    global newArray
    position = startPosition
    count = 0
    for ca in range(range_):
        if(count < nElementArray):
            newArray[position].append(arrays[ca])
            count +=1
        else:
            position +=1
            newArray[position].append(arrays[ca])
            count = 0



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
    divN()
    print(newArray)
    divTwo()
    print(newArray)


    


main()

#se define los array 
#lo que hace es divir los elementos en elementos iguales
#luego dentro de cada arreglo se van hacer divisiones
#el dfs es recursivo y tiene un punto de parada

#EXAMEN HACER EL CODIGO 