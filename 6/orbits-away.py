from collections import defaultdict

orbits = {}

for a,b in map(lambda s: s.split(")"),open("input", "r")):
    orbits[b.strip()] = a

counter = 0

YOU_orbits = []

orbit = "YOU"

while orbits[orbit] in orbits.keys():
    YOU_orbits.append(orbits[orbit])
    orbit = orbits[orbit]


SAN_orbits = []
orbit = "SAN"
while orbits[orbit] in orbits.keys():
    SAN_orbits.append(orbits[orbit])
    orbit = orbits[orbit]

for orbit in YOU_orbits:
    if orbit in SAN_orbits:
        print(YOU_orbits.index(orbit) + SAN_orbits.index(orbit))
        break

