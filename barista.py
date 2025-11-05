#barista robot

print("hello, welcome to barista coffe house.")

name = input("what is your name?\n ")

print("hello  " + name + ", thank you so much for coming in today.\n")
menu = "Black Coffe\nLatte\nCappucino\nEspresso"
print(name + ", What would you like to have today? here is the menu.\n" + menu)
order = input()
if order == "Black Coffee":
    price = 150 
elif order == "Latte":
    price = 160
elif order == "Espresso":
    price = 120
elif order == "Cappucino":
    price = 170
else:
    print("sorry, we dont serve that here.")
    exit()

quantity = input("how many coffe do you like?\n")
print ("Price of each would be:\n" + str(price ))
total = price * int(quantity) 
print("And your total is:" +  str(total))
print("sounds good  " + name + ", we'll have your  "+ quantity + "  " + order + " ready for you in a moment." )

