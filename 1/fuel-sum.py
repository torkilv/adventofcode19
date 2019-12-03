def calculate_fuel(mass):
    return (mass/3) - 2

print(sum(map(calculate_fuel, map(int, open("input-1", "r").readlines()))))