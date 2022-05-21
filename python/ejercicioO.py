import math

def ejercicio1(n):
    for i in range(n, n*1):
        print(f"\nHey - I'm busy looking at: {i}")
        #constante o(c)

def ejercicio2(n):
    print()
    for i in range(n):
        print(f"\nHey - I'm busy looking at: {i}")
        


def ejercicio3(n):
    print("o(2n)")
    for i in range(1, n):
      for j in range(n):
        print(f"\nHey - I'm busy looking at: i={i} and  j={j}")


def ejercicio4(n):
    m = math.pow(2, n)
    for i in range(m):
        print(f"\nHey - I'm busy looking at: {i}")

def main():
    n = 1000
    print(f"\nHey - your input is: {n}")
    ejercicio3(n)


main()