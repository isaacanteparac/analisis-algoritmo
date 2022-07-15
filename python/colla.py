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
    for ind in range(len(population)):
        for indexArr in range(len(population[ind])):
            n = population[ind][indexArr]
            if(n == 1):
                #print(individual_)
                population[ind][indexArr] = [n, "n"]#arriba
            elif(n == 2):
                population[ind][indexArr] = [n, "s"]#abajo
            elif (n == 3):
                population[ind][indexArr] = [n, "e"]#derecha
            elif (n == 4):
                population[ind][indexArr] = [n, "o"]#izquierda
            elif (n == 5):
                population[ind][indexArr] = [n, "ne"]# ARRIBA DERECHA
            elif (n == 6):
                population[ind][indexArr] = [n, "no"]  # ARRIBA IZQUIERDA
            elif (n == 7):
                population[ind][indexArr] = [n, "se"]  # ABAJO DERECHA
            elif (n == 8):
                population[ind][indexArr] = [n, "so"]  # ABAJO IZQUIERDA
    print(population)


def cropped(bPosition, insideB):
    global box
    print(f"bposition {bPosition}, insideB {insideB}")
    position = box[bPosition][insideB]
    if(position == 8 or position == 4):
      return False
    elif(position >= 2):
      return False
    elif(position == 9):
      return False
    else:
      return True
   

def think():
    global population, boxPosition, insideBox
    for ind in range(len(population)):
        for indexArr in range(len(population[ind])):
            orientation = population[ind][indexArr][1]
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
        print(f"{i}{box[i]}")
    print("\n")
    
  
def main():
    #randomGenerator()
    compass()

    think()

print(population)
main()
