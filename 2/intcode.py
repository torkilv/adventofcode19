memory = map(int, open("input", "r").read().split(","))

def add(memory, p): 
    memory[memory[p + 3]] = memory[memory[p + 2]] + memory[memory[p + 1]]

def mul(memory, p):
        memory[memory[p + 3]] = memory[memory[p + 2]] * memory[memory[p + 1]]

def stop(memory, p):
    print(memory[0])
    exit()

instructions = {
    1: add,
    2: mul,
    99: stop
}
def execute_program(instruction_pointer, memory):
    instruction = instructions[memory[instruction_pointer]]

    instruction(memory, instruction_pointer)
   
    execute_program(instruction_pointer+4, memory)

execute_program(0, memory[:])
