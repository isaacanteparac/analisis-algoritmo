#!pip install deap


import warnings
warnings.simplefilter("ignore")
import random
from deap import base
from deap import creator
from deap import tools

box = [[8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
       [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 7, 0, 0, 4, 0, 0, 0, 0, 10, 0, 8],
       [8, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
       [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8], ]

INDIVIDUAL_SIZE = 10
POPULATION = 6
#POSICION DE BOX
boxPosition = 4
insideBox = 2


#CREACION DE TIPOS
creator.create("fitnessMax", base.Fitness, weights = (1.0,))
creator.create("Individual", list, fitness = creator.fitnessMax)

#INICIALIZADORES
toolbox = base.Toolbox()

#GENERA ATRIBUTOS ALEATOREOS
toolbox.register("attr_bool", random.randint, 1, 8)

#ESCTRUCTURA DE INICIALIZADOR
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, INDIVIDUAL_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

#ARRAY POBLACION
population = toolbox.population(POPULATION)

def compass():
    global population
    for popul in range(len(population)):
      n = population[popul]
      if(n == 1):
          population[popul] = [n, "n"]#arriba
      elif(n == 2):
          population[popul] = [n, "s"]#abajo
      elif (n == 3):
          population[popul] = [n, "e"]#derecha
      elif (n == 4):
          population[popul] = [n, "o"]#izquierda
      elif (n == 5):
          population[popul] = [n, "ne"]# ARRIBA DERECHA
      elif (n == 6):
          population[popul] = [n, "no"]  # ARRIBA IZQUIERDA
      elif (n == 7):
          population[popul] = [n, "se"]  # ABAJO DERECHA
      elif (n == 8):
          population[popul] = [n, "so"]  # ABAJO IZQUIERDA

def cropped(bPosition, insideB):
    global box
    position = box[bPosition][insideB]
    if(position == 8 or position == 4):
      return False
    elif(position >= 2):
      return False
    elif(position == 10):
      return True
    else:
      return True

def think():
    global population, boxPosition, insideBox
    for popul in range(len(population)):
        print(population[popul])
        for ind in range(len(population[popul])):
            orientation = "n"
            walking(orientation)
        #boxGet()


def walking(orientation):
    global box, boxPosition, insideBox
    if(orientation == "n"):
        boxPosition -= 1
        #if()
        box[boxPosition][insideBox] += 1
        print(f"{orientation} box{boxPosition}:{insideBox}")
    elif(orientation == "s"):
        boxPosition += 1
        box[boxPosition][insideBox] += 1
        print(f"{orientation} box{boxPosition}:{insideBox}")
    elif(orientation == "e"):
        insideBox += 1
        box[boxPosition][insideBox] = 1
        print(f"{orientation} box{boxPosition}:{insideBox}")
    elif(orientation == "o"):
        insideBox -= 1
        box[boxPosition][insideBox] += 1
        print(f"{orientation} box{boxPosition}:{insideBox}")
    elif(orientation == "no"):
        boxPosition -= 1
        insideBox -= 1
        box[boxPosition][insideBox] += 1
        print(f"{orientation} box{boxPosition}:{insideBox}")
    elif(orientation == "ne"):
        boxPosition -= 1
        insideBox += 1
        box[boxPosition][insideBox] += 1
        print(f"{orientation} box{boxPosition}:{insideBox}")
    elif(orientation == "so"):
        boxPosition += 1
        insideBox -= 1
        box[boxPosition][insideBox] += 1
        print(f"{orientation} box{boxPosition}:{insideBox}")
    elif(orientation == "se"):
        boxPosition += 1
        insideBox += 1
        box[boxPosition][insideBox] += 1
        print(f"{orientation} box{boxPosition}:{insideBox}")

def boxGet():
    global box
    for i in range(len(box)):
        print(f"{box[i]}")
    box = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
           [0, 7, 0, 0, 4, 0, 0, 0, 0, 3, 0],
           [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ]
  
def main():
    compass()
    think()

main()
