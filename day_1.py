file = open("input.txt", "r")

list1 = []
list2 = []

for line in file:
  el1, el2 = line.split()
  list1.append(int(el1))
  list2.append(int(el2))

list1.sort()
list2.sort()

total_distance = 0

for i in range(len(list1)):
  total_distance += abs(list1[i] - list2[i])

print(total_distance)

from collections import Counter

file = open("input.txt")

list1 = []
list2 = []

for line in file:
  el1, el2 = line.split()
  list1.append(int(el1))
  list2.append(int(el2))

list2_counts = Counter(list2)

total_score = 0
for num in list1:
  total_score += num * list2_counts[num]

print(total_score)
