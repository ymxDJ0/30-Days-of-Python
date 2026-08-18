# Day 8 : Dictionaries
dog = {}
dog['name'] = 'skit'
dog['age'] = 4
dog['legs'] = 4
dog['color'] = 'white gray'
dog['breed'] = 'husky'
print(dog)

student = {}
student['first_name'] = 'yamex'
student['last_name'] = 'phantom'
student['gender'] = 'male'
student['age'] = 17
student['martial status'] = False
student['skills'] = ['coding','development','drawing','math','physics']
student['country'] = 'syria'
student['city'] = 'damascus'
student['address'] = None
print(student)
print(len(student)) # 9
print(student['skills'])
print(type(student['skills']))
student['skills'].append('writing')
print(student.keys())
print(student.values())
print(student.items())
del student['address']
del dog
# Day 8 Done!