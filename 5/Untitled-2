from collections import defaultdict
from itertools import product

memory = map(int, open("input", "r").read().split(","))
history = defaultdict(lambda: [])
def add(memory, p): 
    
    memory[memory[p + 3]] = memory[memory[p + 2]] + memory[memory[p + 1]]
    return -1

def mul(memory, p):
        memory[memory[p + 3]] = memory[memory[p + 2]] * memory[memory[p + 1]]
        return -1

def stop(memory, p):
    return memory[0]

instructions = {
    1: add,
    2: mul,
    99: stop
}


def execute_program(instruction_pointer, memory):
    instruction = instructions[memory[instruction_pointer]]

    try: 
        result = instruction(memory, instruction_pointer)
    except:
        return -1
    if result >= 0:
        return result
   
    return execute_program(instruction_pointer+4, memory)

for pair in product(range(10000), repeat=2):
    memory[1] = pair[0]
    memory[2] = pair[1]
    result = execute_program(0, memory[:])
    print(pair, result)
    if result == 19690720:
        exit()



