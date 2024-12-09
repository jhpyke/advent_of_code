import re

with open('./2024/03/data/input.txt', 'r') as f:
    instructions = f.read()

mul_pattern = re.compile('mul\(\d*,\d*\)')
matches = re.findall(mul_pattern, instructions)

total = 0
for match in matches:
    digits = re.findall(r'\d+', match)
    product = int(digits[0]) * int(digits[1])
    total += product

print(total)

# Part 2

do_pattern = re.compile('do\(\)')
dont_pattern = re.compile('don\'t\(\)')

def instruction_searcher(instructions: str, starting_index=0) -> str:
    if starting_index is not None:
        index = starting_index
        latest_index = starting_index
        try:
            next_dont = re.search(dont_pattern, instructions[index+1:]).span()[0] + starting_index+1
            next_do = re.search(do_pattern, instructions[(index+1):]).span()[0] + starting_index+1
        except AttributeError:
            return "0"
        if next_do < next_dont:
            instruction = instructions[index:next_do]
            print(instruction)
            latest_index = next_do
        else:
            instruction = instructions[index:next_dont]
            print(instruction)
            latest_index = next_do
        return instruction + instruction_searcher(instructions, latest_index)
    else:
        return "0"
    
active_instructions = instruction_searcher(instructions, 0)

matches = re.findall(mul_pattern, active_instructions)

total = 0
for match in matches:
    digits = re.findall(r'\d+', match)
    product = int(digits[0]) * int(digits[1])
    total += product

print(total)

# Answer is too low, giving up for now.