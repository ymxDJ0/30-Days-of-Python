# Lever 1
# Day 2: 30 Days of python programming
first_name = "ymx"
last_name = "phantom"
full_name = first_name+" "+last_name
country = "syria"
age = 17
year = 2026
is_married = False # ok why are the questions so specific?
is_true = True
is_light_on = True
var1,var2,var3 = 1,2,3

# Level 2
for i in [first_name,last_name,full_name,country,age,year,is_married,is_true,is_light_on,var1,var2,var3]:
    print(type(i))
print(len(first_name))
difference = len(last_name)-len(first_name)
print(difference if difference>=0 else difference*-1) # to guarantee a positive answer
num_one, num_two = 5,4
total = num_one+num_two
print(total)
diff = num_one-num_two
print(diff)
product = num_one*num_two
print(product)
division = num_one/num_two
print(division)
remainder = num_two%num_one
print(remainder)
exp = num_one**num_two
print(exp)
floor_division = num_one//num_two
print(floor_division)
radius = 30 # in meters
area_of_circle = 3.14 * (radius**2)
circumference = 3.14*2*radius

radius = int(input("enter the radius of the new circle:\n"))
print("the area is",str(3.14 * (radius**2)))

first_name = input("enter your first name:\n")
last_name = input("enter you last name:\n")
country = input("enter the country you are from")
age = input("enter your age right now:\n") # no need for the int() function since we aren't gonna use these variables
