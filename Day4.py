# Day 4 : Strings
question1 = ["Thirty","Days","Of","Python"]
print(' '.join(question1))
question2 = ["Coding","For","All"]
print(" ".join(question2))
company = "Coding for All" # left the "for" uncapitalized for .title() testing 
print(company)
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[:6])
print(company.index("Coding")) # find() also works
print(company.replace("Coding","Python"))
question12 = "Python for Everyone"
print(question12.replace("Everyone","All"))
print(company.split(' '))
question14 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(question14.split(','))
print("Coding For All"[0]) # C
print("Coding For All"[-1]) # l
print("Coding For All"[10]) # [space]
# ok we did all the easy ones (:
def abbreviate(sentence: str):
    # first we split the sentence into each word
    wordList = sentence.split(" ")
    # then we take the first letter of each word (wether you count 'for' as a word is up to prefence i think)
    abb = ''
    for i in wordList:
        abb += i[0].upper() # we make sure it's uppercase
        abb += '.' # we add the '.' to split the letters (obviously)
    return abb
question18 = "Python For Everyone"
print(abbreviate(question18))
question19 = "Coding For All"
print(abbreviate(question19))
# nevermind these are easy too
print("Coding For All".index("C"))
print("Coding For All".index("F"))
print("Coding For All People".rfind('I'))
question23 = 'You cannot end a sentence with because because because is a conjunction'
print(question23.find("because")) # 31
print(question23.index("because"))
print(question23.rfind("because")) # 47
print(question23[31:47+len("because")]) # we use the answers from the previous 2 exercises
# 31 is the start of the first 'because' and 47 is the start of the last 'because' (which only includes the first 2)
# we add the length of 'because' to include the last 'because' (47 is the index it STARTS at)
print("Coding For All".startswith("Coding")) # true
print("Coding For All".startswith("coding")) # false since 'coding' is not capitalized
question30 = '   Coding For All      '
print(question30.strip())
question31 = ['30DaysOfPython','thirty_days_of_python']
for i in question31:
    condition = i.isidentifier()
    print(f"{i}\t{condition}") # wow a string of only special string characters, never seen that before
question32 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(question32)) # pretty sure this is what they meant with 'hash with a space string'
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")
radius = 10
area = 3.14 * radius ** 2
# print("The area of a circle with radius %d is %.0f meters square." % (radius,area))
print("The area of a circle with radius {} is {:.0f} meters square.".format(radius,area)) # the exercise specifies using the method
# now for the last one
a = 8
b = 6
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b:.2f}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")

# day 4 done :D