# Day 13 - List comprehension
# Exercises Level 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([i for i in numbers if i <= 0]) # getting only negatives and zero
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([number for row in list_of_lists for number in row]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print([(i,i**0,i**1,i**2,i**3,i**4,i**5) for i in range(11)])
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print([[pair[0][0].upper(),pair[0][0].upper()[:3],pair[0][-1].upper()] for pair in countries])
print([{'country': pair[0][0].upper(), 'city':pair[0][-1].upper()} for pair in countries])
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print([' '.join(pair[0]) for pair in names])

find_slope = lambda x1,y1,x2,y2 : (y2-y1)/(x2-x1)
find_intercept = lambda x,y,m : y - (m*x)

print(find_slope(2,5,3,7)) # 2.0
print(find_intercept(2,5,2)) # 1
# Day 13 Done