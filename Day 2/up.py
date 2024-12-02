
# Read the reports from the file
with open("Day 2/sample.txt", "r") as file:
    reports = [list(map(int, line.split())) for line in file.readlines()]

# Function to check if a report is safe
def is_safe(report):
    increasing = all(report[i + 1] - report[i] >= 1 and report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(report[i] - report[i + 1] >= 1 and report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

# Count safe reports
safe_count = 0
for report in reports:
    if is_safe(report):
        safe_count += 1

# Output the result
print(f"Number of safe reports: {safe_count}")


# Function to check if a report can be made safe by removing one level
def is_safe_with_dampener(report):
    if is_safe(report):  # Check if the report is already safe
        return True

    # Try removing each level one at a time
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1:]  # Create a new report without the i-th level
        if is_safe(new_report):  # Check if the modified report is safe
            return True

    return False

# Count safe reports with the dampener rule
safe_count = 0
for report in reports:
    if is_safe_with_dampener(report):  # Check if the report is safe with the dampener
        safe_count += 1

# Output the result
print(f"Number of safe reports with dampener: {safe_count}")


