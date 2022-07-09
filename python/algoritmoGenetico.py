
from asyncio.windows_events import NULL
from operator import le
import random

box = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
       [0, 7, 0, 0, 4, 0, 0, 0, 0, 3, 0],
       [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]

nchromosomes = [[], [], [], [], [], []]

start = box[3][1]
boxPosition = 3
insideBox = 1




def compass(n):
    if(n == 1):
        return "N"
    elif (n == 2):
        return "S"
    elif (n == 3):
        return "E"
    elif (n == 4):
        return "O"
    elif (n == 5):
        return "NE"
    elif (n == 6):
        return "NO"
    elif (n == 7):
        return "SE"
    elif (n == 8):
        return "SO"
    else:
        return "ERROR"


def randomGenerator(n):
    global nchromosomes
    for i in range(10):
        numberR = random.randint(1, 8)
        orientation = compass(numberR)
        if(numberR <= 4):
            numberValue = [numberR, 10, orientation, NULL]
        else:
            numberValue = [numberR, 15, orientation, NULL]
        nchromosomes[n].append(numberValue)
    think(n)


def chromosomeGenerator():
    global nchromosomes
    for c in range(6):
        randomGenerator(c)
        print(f"------------------------{c}----------------------------\n")
        print(f"N-RANDOM > WEIGHT > ORIENTATION > VALUE")
        for p in range(len(nchromosomes[c])):
            print(f"{nchromosomes[c][p]}")

def think(subArray):
    global nchromosomes, boxPosition, insideBox
    for p in range(len(nchromosomes[subArray])):
        orientation = nchromosomes[subArray][p][2]
        walking(boxPosition, insideBox, orientation, subArray, p)
    boxGet()
    

def walking(boxPosition, insideBox, orientation, subChromosome, position):
    global box, nchromosomes
    if(orientation == "N"):
        boxPosition-=1
        box[boxPosition][insideBox] = 1
        print(f"{orientation} box{boxPosition}:{insideBox}")
        nchromosomes[subChromosome][position][3] +=1
    elif(orientation == "S"):
        boxPosition +=1
        box[boxPosition][insideBox] += 1
        nchromosomes[subChromosome][position][3] +=1
    elif(orientation == "E"):
        insideBox+=1
        box[boxPosition][insideBox] = 1
        nchromosomes[subChromosome][position][3] +=1
    elif(orientation == "O"):
        insideBox-=1
        box[boxPosition][insideBox] = 1
        nchromosomes[subChromosome][position][3] +=1
    elif(orientation == "NO"):
        boxPosition -=1
        insideBox-=1
        box[boxPosition][insideBox] = 1
        nchromosomes[subChromosome][position][3] +=1
    elif(orientation == "NE"):
        boxPosition -=1
        insideBox+=1
        box[boxPosition][insideBox] = 1
        nchromosomes[subChromosome][position][3] +=1
    elif(orientation == "SO"):
        boxPosition +=1
        insideBox-=1
        box[boxPosition][insideBox] = 1
        nchromosomes[subChromosome][position][3] +=1
    elif(orientation == "SE"):
        boxPosition +=1
        insideBox+=1
        box[boxPosition][insideBox] = 1
        nchromosomes[subChromosome][position][3] +=1
    
    





def boxGet():
    global box
    for i in range(len(box)):
       print(f"{box[i]}")


def main():
    print("\nGITHUB @isaacanteparac\n")
    chromosomeGenerator()


main()
