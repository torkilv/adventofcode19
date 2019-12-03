
path1, path2 = map(lambda x : x.split(","), open("input", "r").readlines())

intersections = []



def generate_path(directions):
    starting_point = [0,0]
    steps = 0
    path = [starting_point]
    for direction in directions:
        way = direction[0]
        change = [0,0]
        if way == "U":
            change = [0,1]
        elif way == "D":
            change = [0, -1]
        elif way == "R":
            change = [1, 0]
        elif way == "L":
            change = [-1, 0]
        else:
            print("UH OH  ", direction[0])


        for i in range(int(direction[1:])):
            path.append([path[-1][0] + change[0],path[-1][1] + change[1]])
    return path[1:] 


def sortCoords(coordString):
    return sum(map(int, coordString.split(",")))
    

first_path = map(lambda x: "%i,%i" % (x[0], x[1]), generate_path(path1))
second_path = map(lambda x: "%i,%i" % (x[0], x[1]), generate_path(path2))
intersects = list(set(first_path).intersection(second_path))

sortedIntersects = sorted(intersects, key=sortCoords)

print(sortCoords(sortedIntersects[0]))
#print(first_path)