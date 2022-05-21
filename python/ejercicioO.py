import math
import time
#import matplotlib.pyplot as plt
#import numpy as np


def oc(n:int):
    inicio = time.time()
    for i in range(n,(n * 2)):
        print(f"\n eje_1: {i}")
    fin = time.time()
    total = fin-inicio
    return total


def ejercicio2(n:int):
    inicio = time.time()
    for i in range(n):
        print(f"\neje_2: {i}")
    fin = time.time()
    total = fin-inicio
    return total


def on2(n:int):
    inicio = time.time()
    for i in range(1, n):
        for j in range(n):
            print(f"\neje_3: i={i}  and  j={j}")
    fin = time.time()
    total = fin-inicio
    return total


def o2n(n:int):
    m = int(math.pow(2, n))
    inicio = time.time()
    for i in range(m):
        print(f"\neje_4: {i}")
    fin = time.time()
    total = fin-inicio
    return total



def main():
    n = 1000
    #print(f"tiempo eje_1 {oc(n)}")
    print(f"tiempo eje_3 {on2(n)}")
    #print(f"tiempo eje_4 {o2n(n)}")


main()
