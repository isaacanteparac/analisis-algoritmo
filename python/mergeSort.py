import random


array = []
newArray = []
nDiv = 0
nPosition = 0
nElement = 0


def divN():
    global newArray, array, nDiv
    countElementArray = len(array)
    for d in range(nDiv):
        newArray.append([])
    opDiv = countElementArray/nDiv
    addElement(opDiv, 0, array, 0, countElementArray)


def divTwo():
    global newArray, nDiv, nPosition, nElement
    newArray.append([])
    countElement = len(newArray[nPosition])
    #pair = countElement%2
    print(f"positon de NEW ARRAY = {nPosition}")
    if (nElement == countElement):
        print(countElement)
        nPosition +=1
        print(f"positon de NEW ARRAY = {nPosition}")
    else:
        #if ( pair == 0):
        div = countElement/2
        div = int(div)
        if(nPosition <= nDiv):
            addElement(3, -1, newArray[nPosition], nElement, (nElement+1))
        nElement += 1
                
        """else:
            print("impar")
            div = countElement/3
            div = (int(div)+1)
            print(div)
            if(nPosition <= nDiv):
                addElement(4, -1, newArray[nPosition], nElement, (nElement+1))"""
        
        divTwo()
       

    

def addElement(nElementArray, startPosition, arrays, forStart, forEnd):
    global newArray
    position = startPosition
    count = 0
    for ca in range(forStart, forEnd):
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