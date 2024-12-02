#Advent of Code 2024
#Day 1

from collections import Counter

file = open("Day 1/input.txt", "r")
lines = file.readlines()
file.close()

#List 1 for elements on left
#List 3 for elements on right
list1, list2 = [], []

#Left column == List 1 
#Right column == List 2
for line in lines:
    left, right = map(int, line.split())
    list1.append(left)
    list2.append(right)

#Arrange in order
list1.sort()
list2.sort()

#Find the difference at each position. 
#Since they are ordered, element at index 1 is the smallest number. 
distance_at_each_index = []
for a, b in zip(list1, list2):
    distance = abs(a - b)                        #distance
    distance_at_each_index.append(distance)      #list of distance
total_distance = sum(distance_at_each_index)     #sum of all the distances

#print("Difference at each index of ordered pair is: ", distance_at_each_index)
print("Total Distance: (sum of all distance at each index) ", total_distance)

#Similarity Score
similarity_score = 0
counts_righty = Counter(list2)

for number in list1:
    count_in_right = counts_righty[number]
    similarity_score += number * count_in_right  

print("similarity score: ", similarity_score)