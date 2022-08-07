

from asyncio.windows_events import NULL


rgb = ["red", "green", "blue"]

westernAustralia = rgb
northernTerritory = rgb
southAustralia = rgb
queensland = rgb
newSouthWales = rgb
victoria = rgb
tasmania = rgb

map_ = []


def value():
    global rgb, map_
    for i in range(7):
        map_.append(rgb)
    return map_



def tour():
    global map_
    print(f"TOUR")
    for t in range(len(map_)):
        print(f"{t} : {colors(1,t)}")


def colors(colorConst, element):
    global map_, rgb
    for i in range(len(map_[element])):
        if(i != colorConst):
            map_[element][i] = None
        else:
            continue
    return map_[element]

def main():
    value()
    tour()

main()
