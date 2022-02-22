from ast import While
from dis import code_info
from tracemalloc import stop

coin_amount=-1
another="yes"
#creates variables for the loop

while another=="yes":
    coin_amount+=1
    print("You have "+str(coin_amount)+" coins.")
    another=input("Would you like another coin? ")
    another=another.lower()
else:
    print("bye")
    stop