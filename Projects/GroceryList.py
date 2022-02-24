from audioop import add
from copyreg import add_extension
from operator import indexOf
from pickle import EMPTY_DICT
from urllib import response
from venv import create



groceries={
    "bananas" : .49,
    "milk" : 4.49,
    "strawberries" : 3.99,
    "bread" : .79,
    "eggs" : .89,
    "cheese" : 2.49,
    "deodorant" : 2.99
}

publix_groceries=["bananas", "milk", "strawberries", "bread"]
kroger_groceries=["eggs", "cheese", "deodorant"]
your_list=[]
your_prices=[]
your_quantities=[]
your_tot=0
welcome=""" welcome to grocery list creator
    would you like to: 
    create a list (1) 
    view a list(2) 
    edit a current list (3)"""
#sets some preliminary variables
   
print(welcome)
request=input('please enter either 1, 2 or 3: ')
#greets and asks the user to choose

def choosening():   
    store_names=["walmart", "kroger", "publix", "target"]
    store_choice=input("are you planning on shopping at walmart, kroger, target, or publix? ").lower()
    if store_choice in store_names:
        print("great! now, let's create your shopping list for your time at " + store_choice + ".")
    else:
        print("sorry, that was not on the list")

if response==1:
    choosening()
#elif response=="edit":
#    edit()
#elif response=="add":
else:
    print("This is not a valid response")




def create(grocery_store): 
    for x in grocery_store:   
        while x in grocery_store:
            grocery_choice=input("would you like "+str(x)+"?\n").lower()
            if grocery_choice=="yes":
                while True:
                    groc_quan=input("how many?\n")
                    try: 
                        int(groc_quan)
                        your_quantities.append(groc_quan)
                        your_list.append(x)
                    except ValueError:
                        print("please enter a number")
                        continue
                    break
                break
            elif grocery_choice=="no":
                break
            else:
                print("this is not a valid entry. please type either yes or no")
#creates a list of groceries and grocery quanitities that allows for second chances

create(kroger_groceries)


for x in your_list:
    if x in groceries:
        your_prices.append(groceries[x])
#adds prices to price list based off of chosen groceries

for x in your_prices:
    loc=your_prices.index(x)
    your_tot+=x*int(your_quantities[loc])
#creates a grand total

print("great! here is your list:")
print(your_quantities)
print(your_list)
print("and this is your prospective grand total:")
print(your_tot)
