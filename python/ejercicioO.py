import math
import time


def executionTime(function):
    def totalTime(*args):
        start = time.time()
        run = function(*args)
        stop = time.time()
        print(f"execution time: {(stop - start)}")
        return run
    return totalTime


@executionTime
def oc(n:int):
    for i in range(n,(n * 2)):
        print(f"\n eje_1: {i}")


@executionTime
def ejercicio2(n:int):
    for i in range(n):
        print(f"\neje_2: {i}")


@executionTime
def on2(n:int):
    for i in range(1, n):
        for j in range(n):
            print(f"\neje_3: i={i}  and  j={j}")


@executionTime
def o2n(n:int):
    m = int(math.pow(2, n))
    for i in range(m):
        print(f"\neje_4: {i}")



def main():
    n = 1000
    ejercicio2(n)

main()
