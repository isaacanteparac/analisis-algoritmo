!pip install deap


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
       [8, 0, 7, 0, 0, 4, 0, 0, 0, 0, 9, 0, 8],
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
toolbox.register("population_", tools.initRepeat, list, toolbox.individual)

#ARRAY POBLACION
individual_ = toolbox.individual()
population = toolbox.population_(POPULATION)

def compass():
    global population
    print(population)
    for ind in range(len(population)):
      for number in range(len(population[ind])):
        n = population[ind][1.2]
        print(n)
        if(n == 1):
            #print(individual_)
            population[ind] = [n, "n"]#arriba
        elif(n == 2):
            population[ind] = [n, "s"]#abajo
        elif (n == 3):
            population[ind] = [n, "e"]#derecha
        elif (n == 4):
            population[ind] = [n, "o"]#izquierda
        elif (n == 5):
            population[ind] = [n, "ne"]# ARRIBA DERECHA
        elif (n == 6):
            population[ind] = [n, "no"]  # ARRIBA IZQUIERDA
        elif (n == 7):
            population[ind] = [n, "se"]  # ABAJO DERECHA
        elif (n == 8):
            population[ind] = [n, "so"]  # ABAJO IZQUIERDA
    print(population)


def cropped(bPosition, insideB):
    global box
    print(f"bposition{bPosition}, insideB{insideB}")
    if(bPosition >= 0 and bPosition <= 9 or insideB >= 0 and insideB <= 13):
      position = box[bPosition][insideB]
      print(f"{position}")
      if(position == 9 or position == 4):
        return False
      elif(position >= 2):
        return False
      elif(position == 10):
        return True
      else:
        return True
    else:
      return False

def think():
    global population, boxPosition, insideBox
    for ind in range(len(population)):
        print(population[ind])
        for indexArr in range(len(population[ind])):
            orientation = population[ind][indexArr]
            walking(orientation)
        boxGet()


def walking(orientation):
    global box, boxPosition, insideBox
    print(orientation)
    if(orientation == "n"):
        if((boxPosition-1) >= 0):
          boxPosition -= 1
          if(cropped(boxPosition, insideBox)):
            box[boxPosition][insideBox] += 1
            print(f"{orientation} box{boxPosition}:{insideBox}")


    elif(orientation == "s"):
        if((boxPosition+1) <= 9):
          boxPosition += 1
          if(cropped(boxPosition, insideBox)):
            box[boxPosition][insideBox] += 1
            print(f"S{orientation} box{boxPosition}:{insideBox}")
  
    elif(orientation == "e"):
        if((insideBox+1) <=13 ):
          insideBox += 1
          if(cropped(boxPosition, insideBox)):
            box[boxPosition][insideBox] = 1
            print(f"{orientation} box{boxPosition}:{insideBox}")


    elif(orientation == "o"):
        if((insideBox-1) >=0 ):
          insideBox -= 1
          if(cropped(boxPosition, insideBox)):
            box[boxPosition][insideBox] += 1
            print(f"{orientation} box{boxPosition}:{insideBox}")
    
    elif(orientation == "no"):
        if((boxPosition-1) >=0 and (insideBox-1) >=0 ):
          boxPosition -= 1
          insideBox -= 1
          if(cropped(boxPosition, insideBox)):
            box[boxPosition][insideBox] += 1
            print(f"{orientation} box{boxPosition}:{insideBox}")

    elif(orientation == "ne"):
        if((boxPosition-1) >=0 and (insideBox+1) <= 13 ):
          boxPosition -= 1
          insideBox += 1
          if(cropped(boxPosition, insideBox)):
            box[boxPosition][insideBox] += 1
            print(f"{orientation} box{boxPosition}:{insideBox}")
    elif(orientation == "so"):
        if((boxPosition+1) <=9 and (insideBox+1) <= 13 ):
          boxPosition += 1
          insideBox -= 1
          if(cropped(boxPosition, insideBox)):    
            box[boxPosition][insideBox] += 1
            print(f"{orientation} box{boxPosition}:{insideBox}")
    elif(orientation == "se"):
        if((boxPosition+1) <=9 and (insideBox+1) >= 0 ):
          boxPosition += 1
          insideBox += 1
          if(cropped(boxPosition, insideBox)):
            box[boxPosition][insideBox] += 1
            print(f"{orientation} box{boxPosition}:{insideBox}")

def boxGet():
    global box
    for i in range(len(box)):
        print(f"{(i+1)}{box[i]}")
    print("\n")
    box = [[8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
       [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 7, 0, 0, 4, 0, 0, 0, 0, 9, 0, 8],
       [8, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
       [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8], ]
  
def main():
    compass()
    think()

main()
