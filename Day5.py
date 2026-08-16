# Day 5 - lists
# Exercises Level 1
emptyList = list()
filledList = [1,'apple',45,3.2,'number4',4-4j,[1,2]]
print(len(filledList)) # 7
print(filledList[0]) # (1)
print(filledList[-1]) # [1,2]
middleIndex = (len(filledList)-1) // 2 # will output 3
print(filledList[middleIndex]) # 3.2

mixed_data_types = ['yamen',17,178,False,'address'] # not typing my address
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
print(len(it_companies))
ITmidIndex = (len(it_companies)-1) // 2
print(it_companies[0],it_companies[ITmidIndex],it_companies[-1])
it_companies.pop(-1)
print(it_companies)
it_companies.append("AssemblyAI")
it_companies.insert(5,'y2AI')
it_companies[0] = it_companies[0].upper()
print('#'.join(it_companies))
print('Google' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[:3])
print(it_companies[-3:])
ITmidIndex = (len(it_companies)-1) // 2 # find the new middle index
print(it_companies[ITmidIndex])
it_companies.pop(0)
it_companies.pop(ITmidIndex-1) # we subtract 1 since we removed the first item
it_companies.pop()
it_companies.clear()
print(it_companies)
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)
full_stack = front_end + back_end
reduxIndex = full_stack.index('Redux')
full_stack.insert(reduxIndex,'Python')
full_stack.insert(reduxIndex,'SQL')
print(full_stack)

# Exercises Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages[0]) # since we sorted it this is now the min age
print(ages[-1]) # # and this is now the max age
middleAgeIndex = (len(ages)-1) // 2
median = ages[middleAgeIndex]
sum = 0
for i in ages:
    sum += i
average = sum/len(ages)
print(average)
range = ages[0] + ages[-1]
print(abs(ages[0]-average),abs(ages[-1]-average))

import countries # importing the countries.py list 

middleIndex = (len(countries.countries)-1) // 2
print(countries.countries[middleIndex])
middleLength = len(countries.countries) // 2 # if the length is odd then one of the two half would have 1 more country
firstHalf = countries.countries[:middleLength].copy()
secondHalf = countries.countries[middleLength:].copy()
print(firstHalf)
print(secondHalf)

question3 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
China, Russia, USA, *scandic = question3
print(scandic)

# Day 5 done!