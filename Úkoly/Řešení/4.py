numbers = [1, 5, 2, 4, 2, 2, 2]
numberslength = len(numbers)
group = []

for i in range(numberslength):
    for j in range(i+1, numberslength):
        group.append(sum(numbers[i:j+1]))

count = 0
grouplength = len(group)

for i in range(grouplength):
    for j in range(i+1, grouplength):
        count += group[i] == group[j]

print(count)