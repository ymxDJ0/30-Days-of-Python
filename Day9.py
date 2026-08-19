# Day 9 : Conditionals
userAge = int(input("enter your current age (0-99):\n"))
if userAge >= 17:
    print('you are old enough to drive')
else:
    print(f'you\'ll have to wait {17-userAge} years to drive')
myAge = 17
difference = userAge - myAge
if difference > 0:
    print(f'you\'re {difference} years older than me.')
elif difference < 0:
    print(f'you\'re {difference*-1} years younger than me.')
else:
    print('we\'re the same age!')

num1 = int(input('Enter the first number (int):\n'))
num2 = int(input('Enter the second number (int):\n'))
if num1 > num2:
    print(f'{num1} is greater than {num2}')
elif num2 > num1:
    print(f'{num2} is greater than {num1}')
else:
    print('both numbers are equal.')

score = int(input('enter your score (0-100):\n'))
if score >= 90:
    print('you got an A!!')
elif score >= 80:
    print('you got a B!')
elif score >= 70:
    print('you got a C.')
elif score >= 60:
    print('you got a D...')
elif score < 60:
    print('you failed. . .')

month = input('Enter the current month:\n').capitalize()
def checkSeason(s: str):
    if s in ['September','October','November']:
        print("it's Autumn!")
    elif s in ['December','January','February']:
        print("it's Winter!")
    elif s in ['March','April','May']:
        print("it's Spring!")
    elif s in ['June','July','Augest']:
        print("it's Summer!")
    else :
        print('INVALID INPUT')

fruits = ['banana', 'orange', 'mango', 'lemon']
def addFruit(item):
    if item in fruits:
        print('that fruit is already in the list!')
    else:
        fruits.append(item)
        print(fruits)
addFruit('orange')
addFruit('apple')

person={
    'first_name': 'yamex',
    'last_name': 'phantom',
    'age': 17,
    'country': 'UAE',
    'is_married': False,
    'skills': ['JavaScript', 'Godot', 'Python'],
    }

if 'skills' in person:
    midIndex = (len(person['skills'])-1)//2
    print(person['skills'][midIndex]) # Node
    print('Python' in person['skills']) # true
    if 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        if 'React' in person['skills']:
            print('fullstack developer')
        elif 'Python' in person['skills']:
            print('backend Developer')
    elif 'React' in person['skills'] and 'JavaScript' in person['skills']:
        print('frontend developer')
    elif 'Godot' in person['skills']:
        print('game Developer')

marriage = 'is married' if person['is_married'] else 'is not married'
print(f'{person['first_name']} {person['last_name']} lives in {person['country']}.', marriage)

# Day 9 Done!