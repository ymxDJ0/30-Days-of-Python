# Day 18 - Regular Expressions (using the re module)
# regular expressions are a way of looking for substrings in a large or small string, they can be modified to look for any pattern.
import re

# Exercise Level 1:
# we need to find the most common word in this
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = re.findall(r'[^ .]+',paragraph) # this will look for any groups of letters (and doesn't look for spaces or periods)
commonWords = {}
for i in words:
    if i not in commonWords:
        commonWords[i] = 1
    else:
        commonWords[i] += 1
highestCount = 0
highestWord = ''
for i in commonWords:
    if commonWords[i] > highestCount:
        highestCount = commonWords[i]
        highestWord = i
print(f"{highestWord}: {highestCount}") # "Love: 6"

question2 = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
# Extract these numbers from this whole text and find the distance between the two furthest particles.
points = re.findall(r'-?\d+',question2) # this looks for a number that might or might not have a negative before it
print(points) # ['-12', '-4', '-3', '-1', '0', '4', '8']
sortedPoints = list(map(lambda x: int(x),points)) # we turn the string points into integers and then sort them
sortedPoints.sort()
print(sortedPoints) # [-12, -4, -3, -1, 0, 4, 8]
# then we find the distance between the lowest and highest points (first and last index)
delta = sortedPoints[-1] - sortedPoints[0]
print(delta) # 20

# Exercises Level 2:
# Write a pattern which identifies if a string is a valid python variable
# python variable rules are:
varPattern = r'[_A-Za-z][A-Za-z0-9_]+' # this checks that the variable name contains only valid characters, and starts with an underscore or letter
def is_valid_variable(x: str):
    regex = re.fullmatch(varPattern,x)
    if regex == None:
        return False
    elif regex.span() != (0,len(x)): # if the span of the match doesn't cover the entire input then that means there was an invalid character somewhere
        print(regex.span())
        return False
    return True
print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True

# Exercises Level 3:
# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. 
There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. 
;I found tea@ching m%o@re interesting tha@n any other %jo@bs.
 %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(x: str): # im going to remove any character that isn't a letter, number, period, comma or question mark
    newSentence = re.sub(r'[^A-Za-z?,. ]+','',x)
    return newSentence
cleaned_text = clean_text(sentence)
print(clean_text)
def most_common_words(x: str): # we already did this earlier on
    Xwords = re.findall(r'[^ .:?,]+',x)
    commonWords = {}
    for i in Xwords:
        if i not in commonWords:
            commonWords[i] = 1
        else:
            commonWords[i] += 1
    highestThree ={}
    for i in commonWords:
        highestThree[i] = commonWords[i]
        if len(highestThree) > 3:
            lowbar = None
            for i in highestThree:
                if lowbar == None:
                    lowbar = i
                    continue
                if highestThree[i] < highestThree[lowbar]:
                    lowbar = i
            highestThree.pop(lowbar)
    print(highestThree) # there are actuall many words that take "second" place (they have 2 instances) so this might differ from method to method
most_common_words(cleaned_text)

# Day 18 - Done!