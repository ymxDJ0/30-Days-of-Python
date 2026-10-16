# Day 14 - Higher-Order functions (hardest one for me yet)
# -so a "closure" is a function that defines a function inside it, with the resulting function changing based on parameters of the outer function.
def multiplyClosure(m: int): # creates a multiply function based on the "m" parameter.
    def mult(n: float):
        return float(m)*n
    return mult
multFive = multiplyClosure(5)
multSix = multiplyClosure(6) # testing if multiple closure results can exist at a time.
print(multSix(7)) # 42.0
print(multFive(10)) # 50.0
# -a "decorater" is a function/order that addes functionality to another function?
def greeting():
    return "welcome to python"
def uppercaseDecorater(function):
    def wrapper():
        func = function() # the example in the course uses a "wrapper" function nested inside the decorater 
        make_upper = func.upper() # which allows the result of this decorater to be used as a
        return make_upper # function instead of only getting the result
    return wrapper

# we can use this decorater by either manually creating a variable like this
Ugreeting = uppercaseDecorater(greeting)
print(Ugreeting()) # WELCOME TO PYTHON

# or using an "@" symbol when defining the function
@uppercaseDecorater
def greeting2():
    return "this should be in uppercase"
print(greeting2()) # THIS SHOULD BE IN UPPERCASE

# we can also apply multiple decorators at the same time
def splitStringDecorator(function):
    def wrapper():
        func = function()
        return func.split()
    return wrapper

@splitStringDecorator
@uppercaseDecorater # they are applied bottom-up, so the nearest decorator is used first
def greeting3():
    return "wow this is a list"
print(greeting3()) # ["WOW","THIS","IS","A","LIST"]

# this next part showcases how a decorator with parameters might work
def deco_with_parameters(function):
    def wrapper_with_params(p1,p2,p3):
        function(p1,p2,p3)
        print("I live in {}".format(p3))
        # no "return" in the wrapper since the functions here simply print
    return wrapper_with_params

@deco_with_parameters
def introduction(p1,p2,p3): # i assume in actual use cases you use "**args" for functions with decorators that take parameters? still don't see how these are practical
    print("Hi, my name is {} {}".format(p1,p2))
introduction('first','last','country')

# Exersices Level 1
# the built in higher-order functions are map, filter and reduce
# -map(function, iteratable) applies the function to each element in the iteratable and return a 'map object' that can be turned into a list with the results
example = [1,2,3,4,5]
def addTwo(n: int):
    return n + 2
print(list(map(addTwo,example))) # [3,4,5,6,7]

# -filter(function, iteratable) applies the function to each element, and expects a boolean result from the function that decides if the element stay or not
def is_even(n:int):
    if n%2 ==0:
        return True
    return False
print(list(filter(is_even,example))) # [2,4]

# -reduce(function, iteratable) applies the function while going through the list, with the function taking both the current item and the result of the last
#   function as a result, basically accumelating a big result containing every element (this is like merging a list of strings or adding all the numbers in a list) 
from functools import reduce
def multiply(x,y): 
    return x*y # i would usually use a lambda here but for sake of clarity i won't
print(reduce(multiply,example)) # 120

# in summary, a higher-order function is any function that uses other functions as objects (parameters, results etc..), decorators and closures are applications
# of higher-order functions, and map, filter and reduce are notable built-in higher-order functions

# didn't really understand exercise 3, ill come back to it . . . eventually

#-
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in countries: print(i)
for i in names: print(i)
for i in numbers: print(i)

Ucountries = list(map(lambda x: x.upper(), countries))
print(Ucountries)
squares = list(map(lambda x: x**2, numbers))
print(squares)
Unames = list(map(lambda x: x.upper(), names))
print(Unames)
#-
def land_filter(x: str):
    if 'land' in x:
        return False
    return True
print(list(filter(land_filter,countries)))
def char_check(x: str):
    if len(x) == 6:
        return False
    return True
print(list(filter(char_check,countries)))
def letter_limit(x: str): # the exercise use "letters" instead of "characters" in the wording so i assume six unique characters.
    letterList = []
    for i in x:
        if not i in letterList:
            letterList.append(i)
        if len(letterList) >= 6:
            return False
    return True
print(list(filter(letter_limit,countries)))
def e_start(x: str):
    if x[0] == 'E':
        return False
    return True
print(list(filter(e_start,countries)))
print(list(filter(letter_limit,list(filter(e_start,countries)))))
#-
def get_string_lists(x: list):
    newlist = []
    for i in x:
        if type(i) is str:
            newlist.append(i)
    return newlist
print(get_string_lists(["a",2,3.4,"bc",True])) # ["a","bc"]
def sum(x,y):
    return x+y
print(reduce(sum,numbers)) # 55
def concatenate(x,y):
    if len(x) <= 1:
        return y
    if y != countries[-1]: # hard-coding this specific part
        x += ", {}".format(y)
    else:
        x += " and {} are north European countries".format(y)
    return x 
print(reduce(concatenate,countries)) # Estonia, Finland, Sweden, Denmark, Norway and Iceland are north European countries
from countries import countries as countryList
def categorize_countries(pattern: str):
    result = filter(lambda x: True if pattern in x else False, countryList)
    return list(result)
print(categorize_countries("land"))
def start_letter_leaderboard(l: list):
    result = {}
    for i in l:
        if i[0] in result:
            result[i[0]] += 1
        else:
            result[i[0]] = 1
    return result # not sure how this exercise relates to higher-order functions but oke (o-o)
print(start_letter_leaderboard(countryList))
def get_first_ten_countries(x: list): # i guess?
    return x[:10]
def get_last_ten_countries(x: list):
    return x[-10:]
print(get_first_ten_countries(countryList))
print(get_last_ten_countries(countryList))
#-
from countries_data import data
# using a smaller piece of data from the larger data file for quick lookup
def sortData(key: str):
    templist = []
    for i in data:
        templist.append(i[key])
    templist.sort()
    templist2 = []
    for i in templist[:10]:
        for j in data:
            if j[key] == i:
                templist2.append(j)
    return templist2
print(sortData("name"))
print(sortData("capital"))
print(sortData("population"))

# Day 14 - Done