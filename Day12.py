# Day 12 : Modules
# - custom module
from mymodule import generate_full_name as full_name, printEmotocon as emotocon
emotocon()
print(full_name('yamen','estef'))

# - os module
import os
dirList = os.listdir()
'''target = 'testFolder'
if target in dirList:
    os.rmdir(target)
else:
    os.mkdir(target)
    os.chdir(target)'''
print(os.getcwd())

# - Sys module
import sys
# sys.argv is a list of the arguments provided when running this script
# argv[0] is always the script name.
print('the file name is',sys.argv[0])
#print(f'hi {sys.argv[1]} welcome to {sys.argv[2]}')
print(sys.maxsize)
print(sys.path)
print(sys.version)
# sys.exit(), same functionality as exit()

# - Statistics module
from statistics import mean,median,mode,stdev
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages)) #21.0909
print(median(ages)) #22
print(mode(ages)) #20
print(stdev(ages)) #6.1066

# - Math module
import math
print(math.pi)
print(math.sqrt(3))
notZero = math.cos(math.pi/2) # the answer is extremely close to zero but not exactly
print(math.floor(notZero)) # so i round down
#print(round(notZero)) # or use the round function

# - String module
import string as st
print(st.ascii_letters) # all letters, capital and small
print(st.digits) # all numbers 0-9
print(st.punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# - Random module
from random import random, randint
print(random()) # random value between 0 and 1 (1 excluded) 
print(randint(2,5)) # random int between the two arguments

# Exercises Level 1
def random_user_id(length = 5):
    id = ''
    for i in range(length):
        key = randint(0,1)
        if key == 0:
            id += st.ascii_letters[randint(1,len(st.ascii_letters))-1]
        else:
            id += st.digits[randint(1,len(st.digits))-1]
    return id
#print(random_user_id())
def user_id_gen_by_input():
    length = int(input('How many letters?\n'))
    times = int(input('How many times?\n'))
    ids = []
    for i in range(times):
        ids.append(random_user_id(length=length))
    return '\n'.join(ids)
#print(user_id_gen_by_input())
def rgb_color_gen():
    return f'rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})'
#print(rgb_color_gen())

# Exercises Level 2
def hexa_color_gen():
    keys = 'ABCDEF0123456789'
    result = ''
    for i in range(6):
        result += keys[randint(1,len(keys))-1]
    return result
def list_of_hexa_color(n: int):
    result = []
    for i in range(n):
        result.append(hexa_color_gen())
    return result
def list_of_rgb_color(n: int):
    result = []
    for i in range(n):
        result.append(rgb_color_gen())
    return result
def generate_colors(type: str, number: int):
    if type == 'rgb':
        print(list_of_rgb_color(number))
    elif type == 'hexa':
        print(list_of_hexa_color(number))
generate_colors('hexa', 3)
generate_colors('hexa', 1)
generate_colors('rgb', 3)
generate_colors('rgb', 1)

# Exercises Level 3
def shuffle_list(base: list):
    shuffled = []
    for i in range(len(base)):
        shuffled.append('00')
    for i in base:
        index = randint(0,len(base)-1)
        shuffled.insert(index,i)
    while '00' in shuffled:
        shuffled.remove('00')
    return shuffled
#print(shuffle_list(['a','b','c','d','e','f']))
def rand_list():
    new = []
    key = [1,2,3,4,5,6,7,8,9,0]
    for i in range(7):
        item = key[randint(1,len(key))-1]
        key.remove(item)
        new.append(item)
    return new
print(rand_list())
# Day 12 Done !