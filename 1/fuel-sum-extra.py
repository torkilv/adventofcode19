def calculate_fuel(mass):
    fuel_mass = (mass/3) - 2
    if fuel_mass > 0:
        return  fuel_mass + calculate_fuel(fuel_mass)
    else:
        return 0

print(sum(map(calculate_fuel, map(int, open("input-1", "r").readlines()))))