from os import system

rgb = []

westernAustralia = rgb
northernTerritory = rgb
southAustralia = rgb
queensland = rgb
newSouthWales = rgb
victoria = rgb
tasmania = rgb

map_ = []
name = ["westernAustralia",
        "northernTerritory",
        "southAustralia",
        "queensland",
        "newSouthWales",
        "victoria",
        "tasmania"]

saveColors = [(0,1,2,0,1,0,2)]
result = []


def value():
    global map_, rgb
    rgb = ["red", "green", "blue"]
    for i in range(7):
        map_.append(rgb)



def tour():
    global map_, result
    print(f"TOUR")
    print(map_)
    for t in range(len(map_)):
        o = colors(saveColors[t],t)
        print(f"{name[t]} : {o}\n")
        map_[t] = o
    print(map_)




def colors(colorConst, element):
    global map_, rgb
    for i in range(len(map_[element])):
        if(i != colorConst):
            print(i, rgb[i])
            map_[element][i] = None
        else:
            map_[element][i] = rgb[i]
        
    return map_[element]


def compare(numberColor):
    global saveColor
    if numberColor != {saveColors[0]}:
        print("hola")

def main():
    system("cls")
    value()
    tour()


main()
