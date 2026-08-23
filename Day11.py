# Day 11 : Functions
# Exercises Level 1
def add_two_numbers(x,y):
    return x + y
def area_of_circle(r):
    return 3.14 * (r**2)
def add_all_sums(l: list[int]):
    sum = 0
    for i in l:
        sum+= int(i)
    return sum
def convert_celcuis_to_farhrenhiet(c):
    return (c*(9/5))+32
def check_season(month: int):
    if month in [9,10,11]:
        return "Autumn"
    elif month in [12,1,2]:
        return "Winter"
    elif month in [3,4,5]:
        return "Spring"
    elif month in [6,7,8]:
        return "Summer"
def print_list(l: list):
    for i in l:
        print(i)
def reverse_list(l: list):
    newlist = []
    for i in l:
        newlist.insert(0,i)
    return newlist
print(reverse_list([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))  # ["C", "B", "A"]
def capitalize_list_items(l: list[str]):
    for i in l:
        index = l.index(i)
        item = i.capitalize()
        l.pop(index)
        l.insert(index,item)
#-
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]
def add_item(l: list,item):
    new = l.copy()
    return new.append(item)
print(add_item(food_stuff, 'Meat')) # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
print(add_item(numbers, 5)) # [2, 3, 7, 9, 5]
def remove_item(l: list,item):
    if item not in l:
        return l
    new = l.copy()
    new.remove(item)
    return new
print(remove_item(food_stuff, 'Mango')) # ['Potato', 'Tomato', 'Milk'];
print(remove_item(numbers, 3)) # [2, 7, 9]
def sum_of_numbers(r: int):
    sum = 0
    for i in range(0,r+1,1):
        sum += i
    return sum
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
def sum_of_odds(r: int):
    sum = 0
    for i in range(0,r+1,1):
        if i%2 != 0:
            sum += i
    return sum
def sum_of_evens(r: int):
    sum = 0
    for i in range(0,r+1,1):
        if i%2 == 0:
            sum += i
    return sum

# Exercise Level 2
def evens_and_odds(r: int):
    oddCount = 0
    evenCount = 0
    for i in range(0,r+1):
        if i%2==0:
            evenCount+= 1
        else:
            oddCount+= 1
    return f'there are {oddCount} odd numbers in the range\nthere are {evenCount} even numbers in the range'
print(evens_and_odds(100))
# odds are 50.
# evens are 51.
def factorial(x: int):
    product = 1
    for i in range(1,x+1):
        product *= i
    return product
def is_empty(a):
    return a is None
#-
def mean(l: list[float]):
    sum = 0
    for i in l:
        sum += i
    return sum/len(l)
def median(l: list[float]):
    midIndex = (len(l)-1)//2
    if len(l)%2 == 0:
        return (l[midIndex]+l[midIndex+1])/2
    else:
        return l[midIndex]
def mode(l: list[float]):
    modeItem = l[0]
    for i in l:
        if l.count(i) > l.count(modeItem):
            modeItem = i
    return {modeItem:l.count(modeItem)}
def calc_range(l: list[float]):
    sortedList = l.copy()
    sortedList.sort()
    return sortedList[-1]-sortedList[0]
def variance(l: list[float]):
    listMean = mean(l)
    sum = 0
    for i in l:
        sum += (i-listMean)**2
    return sum/len(l)
def calculate_std(l: list[float]):
    return variance(l)**0.5
def greet(name='Guest'):
    print('Hello,',name,'!')
greet() # "Hello, Guest!
greet("Alice") # "Hello, Alice!"
def show_args(**args):
    message = 'Recieved: '
    for i in args:
        message+= f' {i}: {args[i]},'
    message = message[:-1]
    print(message)
show_args(a=1,b=2,c=3)
def checkPrime(num: int):
    if num <= 0: # According to google, 0 and negatives aren't primes
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
def is_unique(l: list):
    return len(l) == len(set(l))
def same_type(l:list):
    for i in l:
        if type(i) != type(l[0]):
            return False
    return True

import keyword
def valid_var(x: str):
    if not x.isidentifier():
        return False
    if keyword.iskeyword(x):
        return False
    return True

from countries_data import data as CD
def top10Langs():
    langData = {}
    for i in CD:
        for l in i['languages']:
            if l not in langData:
                langData[l] = 0
            langData[l] += i['population']
    languageValues = list(langData.values())
    languageValues.sort(reverse=True)
    del languageValues[10:]
    topLang = []
    for i in languageValues:
        for n in langData:
            if langData[n] == i:
                topLang.append(n)

def top10Population():
    populations = {}
    for i in CD:
        populations[i['name']] = i['population']
    popValues = list(populations.values())
    popValues.sort(reverse=True)
    del popValues[10:]
    topCountries = []
    for i in popValues:
        for n in populations:
            if populations[n] == i:
                topCountries.append(n)

# Day 11 Done!