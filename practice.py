# age = 29
# height = 5.8 
# name = "abhishek"
# student = True
# print("My name is " + name + ", my age is " + str(age) + " and my height is " + str(height) + " feet.")
# print("Am I a student? " + str(student) )
# print(type(age))    
# print(type(height))
# print(type(name))
# print(type(student))
# print(len(name))
# print(len(str(height)))
# print(len(str(age)))
# print(len(str(student)))

# add = lambda f: f + 50
# print(add(100))
# check= lambda i: i in "aeiou"
# print(check('a'))

# x = ['$12.5' , '$45.6' , '$78.9' , '$23.4' , '$56.7']

# convert = map(lambda p: float(p.replace('$','')), x)
# print(list(convert))    

# y= [120 , 450 , 780 , 230 , 560]

# filter_1= filter(lambda p: p>=200 ,y)
# print(list(filter_1))   

# students = [ ['maria', 85] ,['kumar', 90], ['max', 60]] 

# #print(list(filter(lambda row: row[0].startswith("m"), students)))
# print(sorted(students , key= lambda s:s[1], reverse=True))
# employees = [
#     {'id': 101, 'name': 'Asha',  'dept': 'IT',      'salary': 60000},
#     {'id': 102, 'name': 'Rahul', 'dept': 'HR',      'salary': 45000},
#     {'id': 103, 'name': 'Meera', 'dept': 'Finance', 'salary': 70000},
# ]

# high_salary_employees = filter(lambda e: e['salary'] > 50000, employees)
# for emp in high_salary_employees:
#     print(emp)  


# sorted_employees = sorted(employees, key=lambda e: e['salary'], reverse=True)
# for emp in sorted_employees:
#     print(emp)


#example_file = open ("exmp.txt", "w")

#text = "Abhishek"

#number_of_spaces = len(text) - len(text.strip())
#is_clean = len(text) == len(text.strip())

#print("number of spaces:", number_of_spaces)
#print("is my data clean:",is_clean )

# year = "2026-02-10"

# print("feb" in year)

# print (year.endswith(str(10)))

# print (year.startswith(str(2026)))

#change the date format from "2026-02-10" to "10-feb-2026"
# date_parts = year.split("-")
# name = input("Enter your name: ").capitalize()

# age = int(input("Enter your age: "))
# print("Hello " + name)
# if age >= 18:
#     print('you are an adult')
# else:
#     print('you are a minor')

# function to greet user
# def greet(name= input("Enter your name: ").capitalize()):
#     return "Hello, " + name + "!"   
# print(greet())
# function to check grade based on marks
# marks = int(input("Enter your marks: "))

# if marks >=90:
#     print("grade a".upper())
# elif marks >=80 and marks <90:
#     print("grade b".upper())
# elif marks >=70 and marks <80:
#     print("grade c".upper())
# elif marks >=60 and marks <70:
#     print("grade d".upper())
# else:
#     print("grade f".upper())

# check even or odd
# num = int(input("Enter a number: "))

# if num %2 ==0:
#     print("Number is even")
# else:
#     print("Number is odd")

# password = input("Enter Your Password: ")
# if  len(password) <8:
#     print("Password is too short")
# elif not any(char.isdigit() for char in password):
#     print("Password must contain at least one digit")  
# elif not any(char.isupper() for char in password):
#     print("Password must contain at least one uppercase letter")
# elif not any(char.islower() for char in password):
#     print("Password must contain at least one lowercase letter")
# else:
#     print("Password is strong")

# price = int(input("enter total price:"))

# if price > 500:
#     discount = price*0.10
#     final_price = price - discount
#     print("final price after discount is:", final_price)
# else:
#     print("no discount applicable. final price is:", price)

# age = int(input("Enter your age: " ))
# has_license = input("Do you have a driving license? (yes/no): ").lower()
# if age >= 18 and has_license == 'yes':
#     print("You are eligible to drive.")        
# else:
#     print("You are not eligible to drive.")
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for day in days:
    if day ==["Saturday","Sunday"]:
     break
    print(day)
print("hello")

    