entrada = [5,8,1,3,6]
salidad = []
mini = 0
for i in range((len(entrada)-2)):
    mini = i
    for j in range((len(entrada)-1)):
        if(entrada[j] < entrada[mini]):
            #h