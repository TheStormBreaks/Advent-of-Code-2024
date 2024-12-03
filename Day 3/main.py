import re


# Read the corrupted memory input from a file
with open("Day 3\input.txt", "r") as file:
    input_string = file.read()

# Match valid mul(X, Y) patterns inside parentheses and recent conditional statements
matches = re.findall(r'mul\((\d+),(\d+)\)', input_string)
mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
do_pattern = re.compile(r'do\(\)')
dont_pattern = re.compile(r"don't\(\)")

#######

is_enabled = True  
enabled_sum = 0

total_sum = 0

# Process each map for mul
for match in matches:
    X = int(match[0])
    Y = int(match[1])
    total_sum += X * Y

# Output the final result
print("Total sum of valid mul instructions:", total_sum)


# Process each input for enabled sum
