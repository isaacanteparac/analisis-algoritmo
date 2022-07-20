import math, time
import numpy as np
import matplotlib.pyplot as plt

#TITLE: en microsegundos 10-100-1000-10000
exeOneMS =    [0.009778499603271484, 0.008004903793334961, 0.06985855102539062, 0.6598141193389893]
exeTwoMs =    [0.0009701251983642578, 0.009868144989013672, 0.12217259407043457, 0.8857107162475586]
exeThreeMs =  [0.014400720596313477, 0.645766019821167, 199.96634888648987, 3861.21884393692]
exeFourth =    [0.07676959037780762, None, None, None]


#TITLE: en segundos  10----100---1000--10000
exeOneSeg =     [9.77, 8.00, 6.98, 6.59]
exeTwoSeg =     [9.70, 9.86, 1.22, 8.85]
exeThreeSeg =   [1.44, 6.45, 3.33, 0.00019]
exeFourthSeg =  [7.67, None, None, None]

bigO = ["1 es O(n)", "2 es O(", "3 es o(n**2)", "4 es O(2**n)"]


#TITLE: decorador que calcula el tiempo de ejecucion
def executionTime(function):
    def totalTime(*args):
        start = time.time()
        run = function(*args)
        stop = time.time()
        print(f"execution time: {(stop - start)}")
        return run
    return totalTime


#TITLE: ejercicio 1
@executionTime
def exe1(n: int):
    for i in range(n, (n * 2)):
        print(f"\n eje_1: {i}")


#TITLE: ejercicio 2
@executionTime
def exe2(n: int):
    for i in range(n):
        print(f"\neje_2: {i}")


#TITLE: ejercicio 3
@executionTime
def exe3(n: int):
    for i in range(1, n):
        for j in range(n):
            print(f"\ni={i}  and  j={j}")


#TITLE: ejercicio 4
@executionTime
def exe4(n: int):
    m = int(math.pow(2, n))
    for i in range(m):
        print(f"\neje(4-{n}): {i}")


#TITLE: graficar
def graf(name, array_):
    fig, ax = plt.subplots()
    data = [0, 10, 100, 1000, 10000]
    exeTime = [0]+array_
    plt.plot(data, exeTime, marker='o', linestyle='--', color='g')
    plt.xlabel('data')
    plt.ylabel('time')
    plt.title(name)
    fig


#TITLE: muestra por consola que tipo de BIG O es
def printResult(arrayO):
    for f in arrayO:
      print(f"El ejercicio {f}\n")

def table():
    global exeOneSeg, exeTwoSeg, exeThreeSeg, exeFourthSeg
    print(f"\n      | ejercicio 1 | ejercicio 2 | ejercicio 3 | ejercicio 4 |")
    print(f"10    |    {exeOneSeg[0]}     |    {exeOneSeg[1]}      |    {exeOneSeg[2]}     |    {exeOneSeg[3]}     |")
    print(f"100   |    {exeTwoSeg[0]}      |    {exeTwoSeg[1]}     |    {exeTwoSeg[2]}     |    {exeTwoSeg[3]}     |")
    print(f"1000  |    {exeThreeSeg[0]}     |    {exeThreeSeg[1]}     |    {exeThreeSeg[2]}     |    {exeThreeSeg[3]}  |")
    print(f"10000 |    {exeFourthSeg[0]}     |    {exeFourthSeg[1]}     |    {exeFourthSeg[2]}     |    {exeFourthSeg[3]}     |")


def main():
    global exeOneSeg, exeTwoSeg, exeThreeSeg, exeFourthSeg, bigO
    n = 10000
    # exe1(n)
    # exe2(n)
    # exe3(n)
    # exe4(n)
    #printResult(bigO)
    #graf("ejercicio 1", exeOneSeg)
    #graf("ejercicio 2", exeTwoSeg)
    #graf("ejercicio 3", exeThreeSeg)
    #graf("ejercicio 4", exeFourthSeg)
    table()



main()
