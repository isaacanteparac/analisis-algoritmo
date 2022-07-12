
import random

box = [[8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
       [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 7, 0, 0, 4, 0, 0, 0, 0, 3, 0, 8],
       [8, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
       [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
       [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8], ]

nchromosomes = [[], [], [], [], [], []]

boxPosition = 4
insideBox = 2


def compass(n):
    if(n == 1):
        return "N"  # arriba
    elif (n == 2):
        return "S"  # abajo
    elif (n == 3):
        return "E"  # derecha
    elif (n == 4):
        return "O"  # izquierda
    elif (n == 5):
        return "NE"  # ARRIBA DERECHA
    elif (n == 6):
        return "NO"  # ARRIBA IZQUIERDA
    elif (n == 7):
        return "SE"  # ABAJO DERECHA
    elif (n == 8):
        return "SO"  # ABAJO IZQUIERDA
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


def chromosomeGenerator():
    global nchromosomes
    for c in range(6):
        randomGenerator(c)
        print(f"------------------------{c}----------------------------\n")
        print(f"N-RANDOM > WEIGHT > ORIENTATION > VALUE")
        for p in range(len(nchromosomes[c])):
            print(f"{nchromosomes[c][p]}")


def think(array_):
    global nchromosomes, boxPosition, insideBox
    for i in range(len(array_)):
        for p in range(len(array_[i])):
            orientation = nchromosomes[i][p][2]
            walking(orientation, i, p)
        boxGet()


def walking(orientation, subChromosome, position):
    global box, nchromosomes, boxPosition, insideBox
    if(orientation == "N"):
        boxPosition -= 1
        box[boxPosition][insideBox] += 1
        print(f"{orientation} box{boxPosition}:{insideBox}")
        nchromosomes[subChromosome][position][3] += box[boxPosition][insideBox]
    elif(orientation == "S"):
        boxPosition += 1
        box[boxPosition][insideBox] += 1
        print(f"{orientation} box{boxPosition}:{insideBox}")
        nchromosomes[subChromosome][position][3] += 1
    elif(orientation == "E"):
        insideBox += 1
        box[boxPosition][insideBox] = 1
        print(f"{orientation} box{boxPosition}:{insideBox}")
        nchromosomes[subChromosome][position][3] += 1
    elif(orientation == "O"):
        insideBox -= 1
        box[boxPosition][insideBox] += 1
        print(f"{orientation} box{boxPosition}:{insideBox}")
        nchromosomes[subChromosome][position][3] += 1
    elif(orientation == "NO"):
        boxPosition -= 1
        insideBox -= 1
        box[boxPosition][insideBox] += 1
        print(f"{orientation} box{boxPosition}:{insideBox}")
        nchromosomes[subChromosome][position][3] += 1
    elif(orientation == "NE"):
        boxPosition -= 1
        insideBox += 1
        box[boxPosition][insideBox] += 1
        print(f"{orientation} box{boxPosition}:{insideBox}")
        nchromosomes[subChromosome][position][3] += 1
    elif(orientation == "SO"):
        boxPosition += 1
        insideBox -= 1
        box[boxPosition][insideBox] += 1
        print(f"{orientation} box{boxPosition}:{insideBox}")
        nchromosomes[subChromosome][position][3] += 1
    elif(orientation == "SE"):
        boxPosition += 1
        insideBox += 1
        box[boxPosition][insideBox] += 1
        print(f"{orientation} box{boxPosition}:{insideBox}")
        nchromosomes[subChromosome][position][3] += 1


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
    global nchromosomes
    chromosomeGenerator()
    think(nchromosomes)


main()
