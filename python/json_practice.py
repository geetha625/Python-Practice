''' json.loads() - convert str to python '''
import json
txt='{"name":"geetha","age":20}'
data=json.loads(txt)
print(data)
print(type(data))
print(data["name"])

''' json.dumps() - convert python to str '''
import json
data={
    "name":"geetha",
    "age":20
}
txt=json.dumps(data)
print(txt)
print(type(txt))

import json
text='{"name":"ravi","age":21,"city":"hyd"}'
data=json.loads(text)
print(data)
print(data["city"])
# OUTPUT :
#{'name': 'ravi', 'age': 21, 'city': 'hyd'}
#hyd

import json
student={
    "name":"geetha",
    "marks":92
}
data=json.dumps(student)
print(data)
print(type(data))
# OUTPUT :
# {"name": "geetha", "marks": 92}
 # <class 'str'>
 
 # count no of keys
txt='{"a":10,"b":20,"c":30,"d":40}'
data=json.loads(txt)
print(len(data))      # 4

# access nested json
txt='''
{
    "student":{
         "name":"anu",
         "marks":85
    }
}'''
data=json.loads(txt)
print(data["student"]["name"])

# add new key and convert back
txt='{"name":"rahul","age":22}'
data=json.loads(txt)
data.update({"city":"delhi"})
txt=json.dumps(data)
print(txt)                # {"name": "rahul", "age": 22, "city": "delhi"}

# sum nums from json
txt='{"nums":[10,20,30,40]}'
data=json.loads(txt)
numbers=data["nums"]
total=sum(numbers)
print(total)         # 100
# using for loop
txt='{"nums":[10,20,30,40]}'
data=json.loads(txt)
total=0
for num in data["nums"]:
    total+=num
print(total)              # 100

# filter data
txt='''
{
    "students":[
    {"name":"A","marks":80},
    {"name":"B","marks":60},
    {"name":"C","marks":90}
    ]
}'''
data=json.loads(txt)
for student in data["students"]:
    if student["marks"]>75:
        print(student["name"])
# OUTPUT : A C

# json str vth indentation
data={
    "name":"geetha",
    "skills":["python","SQL"]
}
txt=json.dumps(data,indent=4)
print(txt)
# OUTPUT :
{
    "name": "geetha",
    "skills": [
        "python",
        "SQL"
    ]
}

txt = '''
{
    "company": {
        "employees": [
            {"name": "Ravi", "salary": 50000},
            {"name": "Anu", "salary": 65000},
            {"name": "Kiran", "salary": 45000}
        ]
    }
}
'''
data=json.loads(txt)
employees=data["company"]["employees"]
highest=max(employees,key=lambda emp:emp["salary"])
print(highest["name"])             # anu

import json
txt='''
    {
      "company":{
           "employees":[
                    {"name":"ravi","salary":50000},
                    {"name":"anu","salary":65000},
                    {"name":"kiran","salary":45000},
                    {"name":"meena","salary":70000}
           ]
      }
    }
'''
data=json.loads(txt)
employees=data["company"]["employees"]
#lowest=min(employees,key=lambda emp:emp["salary"])  
#print(lowest["name"])                 # kiran
#print(len(employees))           # 4
#for employee in employees:
#    if (employee["salary"])>50000:
#        print(employee["name"])                   # anu meena
sort=sorted(employees,key=lambda emp:emp["salary"])


