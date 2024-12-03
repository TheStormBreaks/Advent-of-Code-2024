import re

# Read the corrupted memory input from a file
with open("Day 3\input.txt", "r") as file:
    input_string = file.read()

# Use regex to identify valid mul(X, Y) instructions and conditional statements
mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
do_pattern = re.compile(r'do\(\)')
dont_pattern = re.compile(r"don't\(\)")


# Variables to track state and total sum
is_enabled = True  # Mul instructions are initially enabled
total_sum = 0

# Process the input sequentially
index = 0
while index < len(input_string):
    # Check for do() instruction
    if do_pattern.match(input_string, index):
        is_enabled = True
        index += len("do()")
    # Check for don't() instruction
    elif dont_pattern.match(input_string, index):
        is_enabled = False
        index += len("don't()")
    # Check for mul(X, Y) instruction
    elif mul_match := mul_pattern.match(input_string, index):
        if is_enabled:  # Process only if enabled
            X = int(mul_match.group(1))
            Y = int(mul_match.group(2))
            total_sum += X * Y
        index += len(mul_match.group(0))
    else:
        # Skip any unrecognized or invalid characters
        index += 1

# Output the final result
print("Total sum of enabled mul instructions:", total_sum)



""" import re

# Read the corrupted memory input from a file
with open("Day 3\input.txt", "r") as file:
    input_string = file.read()

# Use a regular expression to match only valid mul(X, Y) patterns inside parentheses
matches = re.findall(r'mul\((\d+),(\d+)\)', input_string)



# Initialize a variable to store the sum of the results
total_sum = 0

# Process each match and calculate the result of the multiplication
for match in matches:
    X = int(match[0])
    Y = int(match[1])
    total_sum += X * Y

# Output the final result
print("Total sum of valid mul instructions:", total_sum)


"""