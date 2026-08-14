# Day 3 Exercises:
age = 17
height = 178 
complexNumber = 10-1j

def areaOfTriangle():
    Triangleheight = int(input("enter the height of the triangle:\n"))
    TriangleBase = int(input("enter the length of the triangle's base:\n"))
    area = 0.5 * TriangleBase * Triangleheight
    print("the area of this triangle is:",str(area))
areaOfTriangle()

def perimeterOfTriangle():
    a= int(input("enter the length of the first side:\n"))
    b= int(input("enter the length of the second side:\n"))
    c= int(input("enter the length of the third side:\n"))
    perimeter = a+b+c
    print("The perimeter of this triangle is",str(perimeter))
perimeterOfTriangle()

def rectInfo():
    width = int(input("enter the width of the rectangle:\n"))
    height = int(input("enter the height of the rectangle:\n"))
    print("area:",str(width*height))
    print("circumference:",str(2*(height+width)))
rectInfo()

def circleInfo():
    radius = int(input("enter the radius of the circle:\n"))
    print("area:",str(3.14*(radius**2)))
    print("circumference:",str(3.14*2*radius))
circleInfo()

# y = 2x-2
def y(x):
    return (2*x - 2)
def findSlope():
    x1 = 3
    x2 = 4
    FunctionSlope = (y(x2)-y(x1))/(x2-x1)
    return FunctionSlope
yIntercept = y(0)
print("yIntercept:",str(yIntercept))
# I assume the "intended" method was to use normal math assuming you worked on the function manually
for i in range(-100,100,1): # instead of changing the function itself, we can have python look for the x-intercept
    if y(i) == 0:
        print("x intercept:",str(i))
# for points (2,2) and (6,10)
p1 = [2,2] # let's make an array where index 0 is the X and index -1 is the Y 
p2 = [6,10]
def slopeAndDistance(point1: list[int],point2: list[int]):
    deltaX = point2[0]-point1[0]
    deltaY = point2[-1]-point1[-1]
    slope = deltaY/deltaX
    print("slope=",str(slope))
    distance = ((deltaY**2)+(deltaX**2))**0.5
    print("distance=",str(distance))
    return [slope,distance]
slopeAndDistance(p1,p2)
# now let's compare both slopes
difference = findSlope()-slopeAndDistance(p1,p2)[0]
print(difference)

def function2(x):
    y = x**2 + 6*x + 9
    return y
for i in range(-10,10,1):
    if function2(i)==0:
        print("x =",str(i))

print(len("python")!=len("dragon")) # should return false
if "on" in "python" and "on" in "dragon":
    print("on is in both python and dragon")
sentence = 'I hope this course is not full of jargon'
if "jargon" in sentence:
    print('the sentence contains jargon')

python = len('python')
python = float(python)
python = str(python)
print(python)

def isEven(number):
    if number%2 == 0:
        return True
    else: return False
print((7//3) == int(2.7))
print(type('10')==type(10))
print(int(9.8)==10)

def calcRate():
    hours = int(input("enter the number of hours:\n"))
    rate = int(input("enter the rate of pay per hour:\n"))
    print("pay =",str(hours*rate))
calcRate()

def calcSecondsFromYears():
    years = int(input("enter the number of years:\n"))
    print(years*12*30*24*3600)
calcSecondsFromYears()

'''Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125'''
# from what i can tell, the table is  the index/number then the number raised to 0 then to 1 .. untill the third power
for i in [1,2,3,4,5]:
    newList = []
    newList.append(i)
    for a in [0,1,2,3]:
        newList.append(i**a)
    print(newList)