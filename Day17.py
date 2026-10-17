# Day 17 - Exeption Handling
# or error handling, it's when there's functionality in an app to exit from errors gracefully or try a different method if one fails.
try:
    print(10 + '5') # even the editor is saying there's an error here, but the program avoids it and prints the other message
except: 
    print('Something went wrong')
# except blocks can also specify to handle a precise error and even take it as a variable, and you can have multiple except blocks
# there's also else blocks after try which will run if there were no exceptions
# lastly there's "finally" blocks that always run after the statements no matter the case

##Packing and Unpacking arguments in python:
# when using *args in python, the program takes an undefined number of arguments, this is used for a "sum" function that takes as many numbers as needed,
# or when unpacking variables from a list, and you can even define some variables like the first or last one excluding them from the *arg list
def sum_numbers(*args: int):
    total = 0
    for i in args:
        total += i
    return total
print(sum_numbers(1,2,3,4,5)) # 15 # i can put as many numbers as i want
one, *rest, last = [1,2,3,4,5]
print(one) # 1
print(last) # 5
print (rest) # [2,3,4]
# this can also be done in reverse which is called "spreading"
spread = [one, *rest, last]
print(spread) # this goes back to the first list and doesn't nest

##Extra Functions:
# enumerate() will turn a dictionary into a list of tuples with each tuple containing the key and value, this allows you to iterate over the dictionary 
# with a for loop that uses 2 variables
example = {"a":1,"b":2}
for i,v in enumerate(example):
    print(f"{i}: {v}")
# 0: a
# 1: b

# Zip() will merge any number different lists/tuples into a similar iteratable as enumerate(), which you can also loop over with N variables
fruits = ['mango','banana','apple']
veggies = ['tomato','pickle','pepper']
for i,v in zip(fruits,veggies):
    print(f"fruit : {i}, veggy : {v}")

# Day 17 Exercise
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*countries, es, ru = names
print(countries) # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
print(es, ru) # Estonia Russia
# Day 17 - Done!