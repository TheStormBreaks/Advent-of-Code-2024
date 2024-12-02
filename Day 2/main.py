file = open("Day 2/input.txt", "r")
reports = [list(map(int, line.split())) for line in file.readlines()]
file.close()

def safe(report):
    increasing = all(report[i+1] - report[i] >= 1 and report [i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(report[i] - report[i + 1] >= 1 and report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

safe_count = 0
for report in reports:
    if safe(report):
        safe_count += 1

print(f"Number of safe reports: {safe_count}")



