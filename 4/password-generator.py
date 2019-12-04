

def two_adjacent_same(number):
    prev = ""
    prev_match = False
    for i in str(number):
        if i == prev:
            prev_match = not prev_match 
        elif prev_match:
            return True
        prev = i
    return False

def never_decrease(number):
    prev = 0
    for i in str(number):
        if int(i) < prev:
            return False
        else:
            prev = int(i)

    return True

def valid(number):
    return two_adjacent_same(number) and never_decrease(number)

print(len(filter(valid, range(134792, 675810))))

