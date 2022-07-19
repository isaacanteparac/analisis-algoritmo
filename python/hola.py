from multiprocessing.dummy import Array

from numpy import append


array = [1,2,3,4,[1,2],[3,4]]



def div():
    global array
    nElement = len(array)
    if(nElement % 2):
        opDiv = nElement/2
        array.append([])
        array.append([])
        for i in range(nElement):
            if(i <= opDiv):
                array[(nElement-2)].append = array[i]
            else:
                array[(nElement-1)],append = array[i]
        
