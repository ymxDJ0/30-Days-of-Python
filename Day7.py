# Day 7 : Sets
# -Exercise Level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(len(it_companies)) # 7
it_companies.add('Twitter')
it_companies.update(['OpenAI','Anthropic'])
it_companies.remove('Facebook')
# it_companies.remove('Apple') raises an error because the item isn't in the set
it_companies.discard('Apple') # discard() doesn't raise an error in that case

# -Exercise Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B)) # this would just be (B) since its a superset of A
print(A.intersection(B)) # this would jus be (A) since its a subset of B
print(A.issubset(B)) # true
print(A.isdisjoint(B)) # false because they share elements
print(B.symmetric_difference(A)) # {27,28}
del A
del B
del it_companies # might aswell ¯\_(ツ)_/¯

# -Exercise Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
ageSet = set(age)
print(len(age),len(ageSet)) # 8, 5 
# the list is bigger since it keeps duplicates while the set deletes them
string = 'hello' # a group of letters/symbols which are ordered, indexed and all slices are the same type (string)
exampleList = ['apple',23,4.5] # a group of items from different data types that are indexed and ordered, is modifiable and allows duplicates
exampleTup = ('apple','banana',23,2.4) # a group of items from different data types that are indexed and ordered, can't be modified and allows duplicates
exampleSet = {'apple','orange',34002} # a group of items from different data types that aren't indexed nor ordered, is modifiable, doesn't allow duplicates

sentence = 'I am a teacher and I love to inspire and teach people'
words = sentence.split(' ')
words = set(words)
print('the sentence contains',len(words),'unique words.')
# Day 7 Done!