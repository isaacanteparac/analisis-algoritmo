
import random

from mysqlx import View
array_ = []

def quicksort_(array):
    mini = 0
    for i in range((len(array)-2)):
        mini = i
        for j in range(i+1, len(array)):
            if(array[j] < array[mini]):
                mini = j
        array[mini], array[i] = array[i], array[mini]

    return array

def random_(n, start, end):
    global array_
    for i in range(n):
        number = random.randint(start, end)
        array_.append(number)
    return array_

def main():
    global array_
    aR = random_(300, 1, 1000) 
    print(f"ARRAY DE NUMEROS RANDOMS\n{aR}")
    qS = quicksort_(array_)
    print(f"\nORDENAMIENTO DE NUMEROS\n{qS}")


main()


