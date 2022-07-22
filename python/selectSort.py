import random
import time


array_ = []

def selectSort(array):
    mini = 0
    timeStart = time.time()
    for i in range((len(array)-2)):
        mini = i
        for j in range(i+1, len(array)):
            if(array[j] < array[mini]):
                mini = j
        array[mini], array[i] = array[i], array[mini]
    timeEnd = time.time()
    print(f"\nORDENAMIENTO DE ELEMENTOS\n{array}\n")
    resultTime = timeEnd - timeStart
    return resultTime

def random_(n, start, end):
    global array_
    for i in range(n):
        number = random.randint(start, end)
        array_.append(number)
    return array_

def main():
    global array_
    nElement = int(input("numero de elementos: "))
    aR = random_(nElement, 1, 100000000) 
    print(f"ARRAY DE NUMEROS RANDOMS\n{aR}")
    qS = selectSort(array_)
    print(f"TIEMPO\n{qS}")


main()
#test 1 = elementos 10 , tiempo 0.0 ms
#test 2 =  elementos 100, tiempo 0.0 ms
#test 3 = elementos 1000, tiempo 0.01558995246887207 ms
#test 4 = elementos 10000, tiempo 2.2831358909606934 ms
#test 5 = elementos 100000, tiempo 237.33878874778748 ms
#test 6 = elementos 1000000, tiempo 14,400,000 ms

#COMPLEJIDAD DE TIEOMPO O(N)

