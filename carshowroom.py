cars = ['bmw','audi','toyota']
cars.append('maruti')
name =input("Enter your name: ")
print("Hello " + name + ", welcome to the car showroom.")
print("Available cars are:")

for car in cars:
  print( "-" + car)
selected_car=input("please select your car: ")
if selected_car in cars:
  print("Your selected car is available. thank you for choosing us!")
else:
  print("Sorry, your selected car is not available.")   
