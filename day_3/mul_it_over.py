import re
with open("day_3/text.txt", "r") as file:
    memory = file.read()


pattern = r"mul\(\d{1,3},\d{1,3}\)"
matches = re.findall(pattern, memory)
print("matches=====",len(matches))


total_sum = 0
# Process each match
for match in matches:
    numbers = re.findall(r"\d{1,3}", match)
    result = int(numbers[0]) * int(numbers[1])
    total_sum += result

print(f"Total sum of valid 'mul' operations: {total_sum}")



#===========PART 2 ===============
mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"  # Matches valid mul instructions
do_pattern = r"do\(\)"                   # Matches do() instructions
dont_pattern = r"don't\(\)"              # Matches don't() instructions

mul_enabled = True  # By default, mul is enabled
total_sum = 0      

# Sequentially parse the memory
for match in re.finditer(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", memory):
    instruction = match.group(0)
    if instruction == "do()":
        mul_enabled = True
    elif instruction == "don't()":
        mul_enabled = False
    elif mul_enabled and re.match(mul_pattern, instruction):
        numbers = re.findall(r"\d{1,3}", instruction)
        result = int(numbers[0]) * int(numbers[1])
        total_sum += result

print(f"Total sum of enabled 'mul' operations: {total_sum}")
