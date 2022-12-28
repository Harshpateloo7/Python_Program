import random
numbers = []
for i in range(0,20):
    random_number = random.randint(0,40)
    numbers.append(random_number)

print(numbers)

size = len(numbers)

for j in range(0,size):
        for i in range(0,size-1):
            if numbers[i] > numbers[i+1]:
                temp =numbers[i+1]
                numbers[i+1] =numbers[i]
                numbers[i] = temp
print(numbers)