import random
numbers =[]
for i in range(0,20):
    random_number =random.randint(0,100)
    numbers.append(random_number)

    for n in numbers:
        print(n)

        if 20 in numbers:
            print("I found 20")
        else:
            print("20 is not found")