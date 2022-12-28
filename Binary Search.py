import random
numbers =[]
for i in range(0,20):
    random_number = random.randint(0,40)
    numbers.append(random_number)

    numbers.sort()
    for n in numbers:
        print(n)

        size = len(numbers)
        target = int(input("Target:"))

        search_index = size // 2

        for i in range(0,size):
            if numbers[search_index] == target:
                print("Target found")
                break
            elif numbers[search_index]> target:
                search_index =search_index //2
            else:
                    search_index =search_index + (size -search_index) //2
