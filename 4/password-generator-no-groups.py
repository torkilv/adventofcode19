

def two_adjacent_same(number):
    numberString = str(number)
    for i in range(10):
        if str(i)*2 in numberString and not str(i)*3 in numberString:
            return True
    return False

def never_decrease(number):
    digits = map(int, str(number))
    return digits == sorted(digits)

def valid(number):
    return two_adjacent_same(number) and never_decrease(number)

print(len(filter(valid, range(134792, 675810))))

