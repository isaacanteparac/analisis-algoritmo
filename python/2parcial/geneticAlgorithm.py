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
       [8, 0, 1, 0, 0, 4, 0, 0, 0, 0, 9, 0, 8],
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
continue_insideB = True
continue_positionB = True
advance_counter = 0
weightInd = 0
conuntGen = 0

#CREACION DE TIPOS
creator.create("fitnessMax", base.Fitness, weights = (1.0,))
creator.create("Individual", list, fitness = creator.fitnessMax)

#INICIALIZADORES
toolbox = base.Toolbox()
individual_ = []
population = []

#GENERA ATRIBUTOS ALEATOREOS

def GeneratorPopulation():
    global tollbox, individual_, population
    toolbox.register("attr_bool", random.randint, 1, 8)

    #ESCTRUCTURA DE INICIALIZADOR
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, INDIVIDUAL_SIZE)
    toolbox.register("population_", tools.initRepeat, list, toolbox.individual)
    individual_ = toolbox.individual()
    population = toolbox.population_(POPULATION)







def compass():
    global population
    for ind in range(len(population)):
        for indexArr in range(len(population[ind])):
            n = population[ind][indexArr]
            if(n == 1):
                population[ind][indexArr] = [n, "n", 10]#arriba
                
            elif(n == 2):
                population[ind][indexArr] = [n, "s", 10]#abajo

            elif (n == 3):
                population[ind][indexArr] = [n, "e", 10]#derecha

            elif (n == 4):
                population[ind][indexArr] = [n, "o", 10]#izquierda

            elif (n == 5):
                population[ind][indexArr] = [n, "ne", 15]# ARRIBA DERECHA

            elif (n == 6):
                population[ind][indexArr] = [n, "no", 15]  # ARRIBA IZQUIERDA

            elif (n == 7):
                population[ind][indexArr] = [n, "se", 15]  # ABAJO DERECHA

            elif (n == 8):
                population[ind][indexArr] = [n, "so", 15]  # ABAJO IZQUIERDA


def cropped(bPosition, insideB):
    global box, continue_insideB, continue_positionB
    if(bPosition <=9 and  insideB <=12):
      position = box[bPosition][insideB]

      if(position == 8 or position == 4):
        continue_insideB = False
        continue_positionB = True
        return continue_insideB

      elif(position == 2):
        continue_insideB = False
        continue_positionB = False
        clear()
        return continue_insideB

      elif(position == 9):
        continue_insideB = False
        continue_positionB = False
        return continue_insideB

      else:
        continue_insideB = True
        continue_positionB = True
        return continue_insideB
   

def think():
    global population, boxPosition, insideBox, continue_insideB, continue_positionB, advance_counter, weightInd, conuntGen
    for ind in range(len(population)):
        advance_counter = 0
        weightInd = 0
        for indexArr in range(len(population[ind])):
            orientation = population[ind][indexArr]
            if(continue_insideB):
              walking(orientation)
              weightInd += population[ind][indexArr][2]
            else:
              continue_insideB = True
              break
        if(continue_positionB):
          population[ind].append([ind, advance_counter, weightInd])
          boxGet()
          boxPosition = 4
          insideBox = 2
        else:
          break
    if(continue_positionB != True):
        print("----------------------REINICIO-------------------")
        conuntGen = 0
        main()



def walking(positionOrientation):
    global box, boxPosition, insideBox, advance_counter
    orientation = positionOrientation[1] 
    weight = positionOrientation[2]
    if(orientation == "n"):
        if((boxPosition-1) >= 0):
          boxPosition -= 1
          if(cropped(boxPosition, insideBox)):
            box[boxPosition][insideBox] += 1

    elif(orientation == "s"):
        if((boxPosition+1) <= 9):
          boxPosition += 1
          if(cropped(boxPosition, insideBox)):
            box[boxPosition][insideBox] += 1

    elif(orientation == "e"):
        if((insideBox+1) <=13 ):
          insideBox += 1
          if(cropped(boxPosition, insideBox)):
            box[boxPosition][insideBox] = 1
            advance_counter += 1
        
    elif(orientation == "o"):
        if((insideBox-1) >=0 ):
          insideBox -= 1
          if(cropped(boxPosition, insideBox)):
            box[boxPosition][insideBox] += 1

    elif(orientation == "no"):
        if((boxPosition-1) >=0 and (insideBox-1) >=0 ):
          boxPosition -= 1
          insideBox -= 1
          if(cropped(boxPosition, insideBox)):
            box[boxPosition][insideBox] += 1

    elif(orientation == "ne"):
        if((boxPosition-1) >=0 and (insideBox+1) <= 13 ):
          boxPosition -= 1
          insideBox += 1
          if(cropped(boxPosition, insideBox)):
            box[boxPosition][insideBox] += 1
            advance_counter += 1


    elif(orientation == "so"):
        if((boxPosition+1) <=9 and (insideBox+1) <= 13 ):
          boxPosition += 1
          insideBox -= 1
          if(cropped(boxPosition, insideBox)):    
            box[boxPosition][insideBox] += 1


    elif(orientation == "se"):
        if((boxPosition+1) <=9 and (insideBox+1) >= 0 ):
          boxPosition += 1
          insideBox += 1
          if(cropped(boxPosition, insideBox)):
            box[boxPosition][insideBox] += 1
            advance_counter += 1



def boxGet():
    global box
    for i in range(len(box)):
        print(f"{i}{box[i]}")
    print("\n")
    clear()



def clear():
    global box, boxPosition, insideBox
    box = [[8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
       [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 1, 0, 0, 4, 0, 0, 0, 0, 9, 0, 8],
       [8, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
       [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8], ]



def individualCompare():
    global population
    array = []
    for ind in range(len(population)):
      array.append(population[ind][-1])
    array = selectSort(array)
    indDiv(array)



def selectSort(array):
    for i in range((len(array)-1)):
        mini = i
        for j in range(i+1, len(array)):
            if(array[j][1] > array[mini][1]):
              mini = j
        array[mini], array[i] = array[i], array[mini]
    return array



def indDiv(array):
  global population, conuntGen
  genRandom = random.randint(1,10)
  print(f"poblacion vieja {population}")
  hInd1 = array[0][0]
  bInd1 = array[1][0]
  hInd2 = array[2][0]
  bInd2 = array[3][0]
  newInd1 = array[4][0]
  newInd2 = array[5][0]
  population[newInd1] = []
  population[newInd2] = []

  for i in range(10):
    if(i <= genRandom):
        head1 = population[hInd1][i]
        head2 = population[hInd2][i]
        population[newInd1].append(head1)
        population[newInd2].append(head2)
    else:
      body1 = population[bInd1][i]
      body2 = population[bInd2][i]
      population[newInd1].append(body1)
      population[newInd2].append(body2)

  population[hInd1].pop(-1)
  population[hInd2].pop(-1)
  population[bInd1].pop(-1)
  population[bInd2].pop(-1)
  conuntGen +=1

  print(f"numero de generacion {conuntGen}")
  print(f"poblacion nueva {population}")

  think()
  individualCompare()



def main():
    global continue_insideB, continue_positionB
    GeneratorPopulation()
    continue_insideB = True
    continue_positionB = True
    compass()
    think()
    individualCompare()

main()
