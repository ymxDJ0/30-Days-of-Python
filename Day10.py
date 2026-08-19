# Day 10 : loops
# Exercises Level 1
for i in range(0,11,1):
    print(i)
num = 0
while num <= 10:
    print(num)
    num += 1

for i in range(0,11,1):
    print(10-i)
num = 10
while num >= 0:
    print(num)
    num -= 1

for i in range(1,8,1):
    print('#'*i)
for i in range(1,9,1):
    message = ''
    for i in range(1,9,1): # module instructed to use 'nested loops', although there is a more optimal option
        message += '# '
    print(message)

for i in range(0,11,1):
    print(f'{i} x {i} = {i**2}')

question6 = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in question6:
    print(i)
for i in range(0,101,1): # only prints even numbers
    if i % 2 == 0:
        print(i)
for i in range(0,101,1): # only prints odd numbers
    if i % 2 != 0:
        print(i)

sum = 0
for i in range(0,101,1):
    sum += i
print('the sum of all numbers is',sum)

sumOdd = 0
sumEven = 0
for i in range(0,101,1):
    if i%2 == 0:
        sumEven += i
    else:
        sumOdd += i
print(f'the sum of all evens is {sumEven} and the sum of all odds is {sumOdd}')

from countries import countries
landList = []
for i in countries:
    if 'land' in i:
        landList.append(i)

fruitList = ['banana', 'orange', 'mango', 'lemon']
for i in range(0,len(fruitList)): # using range instead of iterating on the list to avoid errors since i'm modifying it in the loop
    fruitList.insert(0,fruitList.pop(i))
print(fruitList)

from countries_data import data as CD
languages = []
for i in CD:
    for l in i['languages']:
        if l not in languages:
            languages.append(l)
print('there are',len(languages),'languages!') # 112

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
print(topLang) # the 10 most spoken languages in the world according to the data provided
#print(languageValues)

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
print(topCountries)

# Day 10 Done! (hardest one by far)