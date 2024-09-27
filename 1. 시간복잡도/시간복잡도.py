import random
findNumber = random.randint(1, 101)
for i in range(1, 101):
    if i==findNumber:
        print(i)
        break