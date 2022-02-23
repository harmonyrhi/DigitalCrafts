from cgi import test
from re import T

#even or odd
test_num=input("please enter a number: ")

def even_or(test_num):
    try:
        new_num=int(test_num)
        if new_num%2==0:
            print("this number is even")
        else:
            print("this number is odd")
    except TypeError:
        print('this is not a number')

even_or(test_num)


#coin flip
import random
print('flipping a coin...')
coin_num=random.randint(1,2)
if coin_num%2==0:
    print("you got heads!")
else:
    print("you got tails!")


#diceroll
print('you rolled a die!')
die_num=str(random.randint(1,6))
print('your number is '+die_num+"!")