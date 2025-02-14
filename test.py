import random

random_number= random.randint(1, 10)

for i in range(1, random_number):
    for j in range(1, i+1):
        print(j, end='')
    print()
