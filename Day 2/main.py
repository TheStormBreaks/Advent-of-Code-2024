# Advent of Code 2024
# Day 1

# Read lines from the file, split each line into integers, and store them as a list of lists
file = open("Day 2/input.txt", "r")
reports = [list(map(int, line.split())) for line in file.readlines()]
file.close()

def safe(report):
    # If all consecutive diffs are bw 1 and 3 for increasing or decreasing
    increasing = all(report[i+1] - report[i] >= 1 and report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(report[i] - report[i + 1] >= 1 and report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    # A report is safe if it is either increasing or decreasing
    return increasing or decreasing


def dampner(report):
    for i in range(len(report)):
        # Create a new report by removing the element at index i
        safer_report = report[:i] + report[i + 1:]    
        if safe(safer_report):
            return True  
        return False  # if no safe report formed by removing one element


# COUNT SAFE REPORTS
safe_count = 0
for report in reports:
    if safe(report):
        safe_count += 1
print(f"Number of safe reports: {safe_count}")


# COUNT SAFE AFTER IMPLEMENTING DAMPNER
dampner_safe_counts = 0
for report in reports:
    if dampner(report):
        dampner_safe_counts += 1
print(f"Number of safe reports with dampner: ", dampner_safe_counts)