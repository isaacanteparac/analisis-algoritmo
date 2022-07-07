
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
initialPosition = 0




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
    for i in range(8):
        numberR = random.randint(1, 8)
        orientation = compass(numberR)
        if(numberR <= 4):
            numberValue = (numberR, 10, orientation)
        else:
            numberValue = (numberR, 15, orientation)
        nchromosomes[n].append(numberValue)


def chromosomeGenerator():
    global nchromosomes
    for c in range(6):
        randomGenerator(c)
        print(f"------------------------{c}----------------------------\n")
        print(f"N-RANDOM > WEIGHT > ORIENTATION")
        for p in range(len(nchromosomes[c])):
            print(f"{nchromosomes[c][p]}\n")


def main():
    print("\nGITHUB @isaacanteparac\n")
    chromosomeGenerator()


main()
