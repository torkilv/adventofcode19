from collections import defaultdict
from itertools import product

memory = map(int, open("input", "r").read().split(","))
history = defaultdict(lambda: [])

def readMemory(memory, position, mode):
    if mode:
        return memory[position]
    else:
        return memory[memory[position]]


def add(memory, p, modes): 
    memory[memory[p + 3]] = readMemory(memory, p+2, modes[1]) + readMemory(memory, p + 1, modes[0])
    return 4

def mul(memory, p, modes):
        memory[memory[p + 3]] =  readMemory(memory, p + 2, modes[1]) * readMemory(memory, p + 1, modes[0])
        return 4

def stop(memory, p, modes):
    return 0

def save(memory, p, value):
    memory[memory[p + 1]] = value
    return 2

def printValue(memory, p, modes):
    print(readMemory(memory, p+1, modes[0]))
    return 2

def jumpIfTrue(memory, p, modes):
    if readMemory(memory, p+1, modes[0]):
        return readMemory(memory, p+2, modes[1]) - p
    else: 
        return 3
def jumpIfFalse(memory, p, modes):
    if not readMemory(memory, p+1, modes[0]):
        return readMemory(memory, p+2, modes[1]) - p
    else: 
        return 3

def lessThan(memory, p, modes):
    memory[memory[p + 3]] = int(readMemory(memory, p+1, modes[0]) < readMemory(memory, p+2, modes[1]))
    return 4

def equals(memory, p, modes):
    print(p, modes)
    memory[memory[p + 3]] = int(readMemory(memory, p+1, modes[0]) == readMemory(memory, p+2, modes[1]))
    return 4


instructions = {
    1: add,
    2: mul,
    3: save,
    4: printValue,
    5: jumpIfTrue,
    6: jumpIfFalse,
    7: lessThan,
    8: equals,
    99: stop
}

def getInstructionAndModes(pointer, memory):
    value = str(memory[pointer])

    instruction = int(value[-2:])
    modes = map(int,list(value[:-2]))
    if instruction in [1, 2, 7,8]:
        while len(modes) < 3:
            modes = [0] + modes
    elif instruction in [3,4]:
        while len(modes) < 1:
            modes = [0] + modes
    elif instruction in [5,6]:
        while len(modes) < 2:
            modes = [0] + modes
    modes.reverse()

    return instruction, modes




def execute_program(instruction_pointer, memory, inputs):
    instruction, modes = getInstructionAndModes(instruction_pointer, memory)

    if instruction != 3:
        result = instructions[instruction](memory, instruction_pointer, modes)        
    else: 
        result = instructions[instruction](memory, instruction_pointer, inputs.pop())
   
    if instruction == 99:
        return result
   
 
    return execute_program(instruction_pointer + result, memory, inputs)

execute_program(0, memory, [5])