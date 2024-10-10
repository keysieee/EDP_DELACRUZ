numbers = (1, 3, 2, 4, 3, 1, 2, 5)

duplicates = []

for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1
    if count > 1 and numbers[i] not in duplicates:
        duplicates.append(numbers[i])

for num in duplicates:
    print(num)