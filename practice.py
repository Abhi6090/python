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

year = "2026-02-10"

print("feb" in year)

print (year.endswith(str(10)))

print (year.startswith(str(2026)))

#change the date format from "2026-02-10" to "10-feb-2026"






    
    


