# Advent of Code 2024
# Day 1

# Open the input file for reading
file = open("Day 2/input.txt", "r")

# Read lines from the file, split each line into integers, and store them as a list of lists
reports = [list(map(int, line.split())) for line in file.readlines()]

# Close the file after reading
file.close()

# Define a function to check if a report is safe
def safe(report):
    # Check if all consecutive differences are between 1 and 3 (inclusive) for increasing order
    increasing = all(report[i+1] - report[i] >= 1 and report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    
    # Check if all consecutive differences are between 1 and 3 (inclusive) for decreasing order
    decreasing = all(report[i] - report[i + 1] >= 1 and report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    
    # A report is safe if it is either increasing or decreasing
    return increasing or decreasing

# Initialize a counter for safe reports
safe_count = 0

# Iterate through each report to count how many are safe
for report in reports:
    if safe(report):
        safe_count += 1

# Print the total number of safe reports
print(f"Number of safe reports: {safe_count}")

# Define a function to check if a report can be made safe by removing one element
def dampner(report):
    # Iterate through each index in the report
    for i in range(len(report)):
        # Create a new report by removing the element at index i
        safer_report = report[:i] + report[i + 1:]
        
        # Check if the new report is safe
        if safe(safer_report):
            return True  # Return True if a safe report can be formed
    
    return False  # Return False if no safe report can be formed by removing one element

# Initialize a counter for reports that can be made safe with a dampner
dampner_safe_counts = 0

# Iterate through each report to count how many can be made safe with a dampner
for report in reports:
    if dampner(report):
        dampner_safe_counts += 1

# Print the total number of reports that can be made safe with a dampner
print(f"Number of safe reports with dampner: ", dampner_safe_counts)