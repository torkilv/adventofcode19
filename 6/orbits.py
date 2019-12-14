from collections import defaultdict

orbits = {}

for a,b in map(lambda s: s.split(")"),open("input", "r")):
    orbits[b.strip()] = a

counter = 0

for sat in orbits.keys():
    counter += 1
    while orbits[sat] in orbits.keys():
        counter += 1
        sat = orbits[sat]
        
print(counter)
