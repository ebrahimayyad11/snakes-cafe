print('**************************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below     **')
print('**')
print('** To quit at any time, type "quit" **')
print('**************************************')

menu = ['Wings','Cookies','Spring Rolls','Salmon','Steak','Meat Tornado','A Literal Garden','Ice Cream','Cake','Pie','Coffee','Tea','Unicorn Tears']

counter = [0,0,0,0,0,0,0,0,0,0,0,0,0]

print("\n \nAppetizers  \n" + "-------\n" + menu[0] + "\n"+ menu[1] + "\n"+ menu[2] + "\n")


print("\nEntrees  \n" + "-------\n" + menu[3] + "\n"+ menu[4] + "\n"+ menu[5] + "\n"+ menu[6] + "\n")


print("\nDesserts  \n" + "-------\n" + menu[7] + "\n"+ menu[8] + "\n"+ menu[9] + "\n")


print("\nDrinks  \n" + "-------\n" + menu[10] + "\n"+ menu[11] + "\n"+ menu[12] + "\n")


print('***********************************')
print('** What would you like to order? **')
print('***********************************\n')


order = input("> ")

new_menu = []

for i in menu:
    new_menu.append(i.lower())


def full_order():
    print('Your order: \n \n')
    for index,value in enumerate(counter):
        if value > 0:
            print("{}: {}".format(menu[index],value))



def newOrder(order):
    if order.lower() in new_menu:
        value = counter[new_menu.index(order)]
        value += 1
        counter[new_menu.index(order)] = value
        full_order()
        New = input("""Do you want anything else? 
        
        > """)
        newOrder(New)
    elif order.lower() == 'quit':
        print("Thanks for visiting Snakes Cafe!")
        return

    else:
        New = input("""We don't have this order in our menu
        Do you want any thing else:

        > """)
        newOrder(New)


newOrder(order)