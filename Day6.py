# Day 6 : Tuples
# Exercise Level 1
empty = ()
brothers = ('omyx','arwr')
sisters = ('jena',) # for some reason this doesn't work with the comma at the end.
siblings = brothers+sisters
print(siblings)
print(f'I have {len(siblings)} siblings!')
family_members = siblings + ("father","mother")
print(family_members)

# Exercise Level 2
siblings = family_members[:-2]
father_mother = family_members[-2:]
print(siblings,father_mother)

fruit = ('apple','orange','mango','strawberry','banana')
vegetables = ('tomato','potato','cucumber')
animalProducts = ('milk','beef','eggs')
foodStuff_tp = fruit + vegetables + animalProducts
print(foodStuff_tp)
foodStuff_lt = list(foodStuff_tp)
print(foodStuff_lt)
middleIndex = (len(foodStuff_lt)-1)//2
print(foodStuff_lt[middleIndex]) # the list and tuple are interchangable, both will give the same answer here.
print(foodStuff_lt[:3])
print(foodStuff_lt[-3:])
del foodStuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries) # false
print('Iceland' in nordic_countries) # true
# day 6 done!