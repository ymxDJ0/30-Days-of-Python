# Day 19 - File Handling
# python has functionality for reading and writing to files of many types like .txt .json .csv etc..
filePath = 'day19.txt'
f = open(filePath,"w") # open is used to store and use the file as an object
# there are many modes for using files:
# r for 'read', reads the contents of the text file but doesn't allow editing
# w for 'write', opens the file for writing and creates the file if it doesn't exits
# a for append, adds text to the end of the file instead of clearing it like 'write'
# x for simply creating the file
# b for binary mode which allows editing images
# t for Text Default value. Text mode
f.close() # when done with the file we have to free up the memory using file.close(), this can be done automatically using 'with' statements

import os # we can manage and delete files in storage using the OS module using functions like os.path.exists() and os.remove()
if os.path.exists('day19.txt'):
    os.remove('day19.txt')

import json # we can also edit and write .json files by converting dictionaries into json with the json module.
import csv # similarly, we use the csv for .csv files
# when reading the lines of a csv file, line 0 is the headers

# Exercises Level 1:
def count_line_and_words(fPath: str):
    lineCount = 0
    wordCount = 0
    with open(fPath,'r') as f:
        for i in f.readlines():
            lineCount += 1
            wordCount += len(i.split(' '))
    print(f'{fPath}\nword count: {wordCount}\nline count: {lineCount}')
count_line_and_words('files/obama_speech.txt')
count_line_and_words('files/michelle_obama_speech.txt')
count_line_and_words('files/donald_speech.txt')
count_line_and_words('files/melina_trump_speech.txt')

def most_spoken_languages(n: int,fPath: str= 'files/countries_data.json'):
    f = open(fPath,'r+',encoding='utf8')
    Data : dict = json.load(f)
    f.close()
    language_count = {}
    for country in Data:
        for language in country['languages']:
            language_count[language] = language_count.get(language,0) + 1
    result = sorted(language_count.items(), key=lambda x : x[1],reverse=True)
    print(result[:n])
most_spoken_languages(10)

def most_populated_countries(n: int,fPath: str= 'files/countries_data.json'):
    f = open(fPath,'r+',encoding='utf8')
    Data : dict = json.load(f)
    f.close()
    populations = []
    for country in Data:
        populations.append({'country': country['name'], 'population': country['population']})
    result = sorted(populations,key= lambda x: x['population'], reverse= True)
    print(result[:n])
most_populated_countries(5)

# Exercises Level 2:
import re
def find_common_words(fPath: str,n: int):
    f = open(fPath,'r+')
    Data = re.findall(r'[A-Za-z\']{2,}',f.read())
    f.close()
    word_count = {}
    for word in Data:
        word_count[word] = word_count.get(word,0) + 1
    result = sorted(word_count.items(),key= lambda x: x[1],reverse= True)
    print(result[:n])

#find_common_words('files/obama_speech.txt',10)
#find_common_words('files/michelle_obama_speech.txt',10)
#find_common_words('files/donald_speech.txt',10)
#find_common_words('files/melina_trump_speech.txt',10)
find_common_words('files/romeo_and_juliet.txt',10)

with open('files/hacker_news.csv','r+') as f:
    pythonCount = 0
    jsCount = 0
    javaCount = 0
    for line in f.readlines():
        if 'python' in line or 'Python' in line:
            pythonCount += 1
        if 'javascript' in line or 'Javascript' in line or 'JavaScript' in line:
            jsCount += 1
        if 'Java' in line and not ('Javascript' in line or 'JavaScript' in line):
            javaCount += 1
    print(f"Python count: {pythonCount}\nJs count: {jsCount}\nJava count: {javaCount}")

# Day 19 - Done!