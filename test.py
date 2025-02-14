import random

random_number= random.randint(1, 10)

def hello(number):
    if number==random_number:
        print(f'You made it, the random number is {random_number}')
    else:
        print (f'No you looser, the random number is {random_number}')

hello(int(input('Enter the number: ')))