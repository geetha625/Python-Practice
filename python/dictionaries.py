#thisdict={
#    "brand":"ford",
#    "model":"mustang",
#    "year":1964
#}
#print(thisdict)

#thisdict={
#    "brand":"ford",
#    "model":"mustang",
#    "year":1964
#}
#print(thisdict["brand"])

#1.create a dictionary
#student={
#    "name":"geetha",
#    "age":19,
#    "course":"CSE"
#}
#print(student)

#2.print type
#student={
#    "name":"geetha",
#    "age":19,
#    "course":"CSE",
#}
#print(type(student))

#3.duplicate keys
#d={"a":10,"b":20,"a":30}
#print(d)         the last entered value is stpred for a

#4.mixed data types
#dict={
#    "marks":80,
#    "name":"geetha",
#    "subjects":("maths","physics","chemistry")
#}
#print(dict)

#5.empty dictionary
#dict={
#}
#dict.update({"name":"geetha","age":19,"section":"A"})
#print(dict)

#6.dictionary length
#dict={
 #   "name":"geetha",
 #   "age":19,
 #   "section":"csm",
 #   "roll num":51,
 #   "college":"GNIT"
#}
#print(len(dict))

#7.check mutable nature
#dict={
#    "name":"geetha"
#}
#dict["name"]="chinnari"
#print(dict)

#8.dictionary vs list
   #dictionay is better because we assign particular student with their marks but we cant do that in lists 

#9.real life example
#dict={
#    "username":" ",
#    "password":" ",
#    "email":" "
#}
#print(dict)

#10.nested basic
#students={
#    "s1":{"name":"geetha","marks":90},
#    "s2":{"name":"chinnari","marks":85}
#}
#print(students)

#11.
#mobile={
#    "brand":"samsung",
#    "price":22000,
#    "features":["flexible,full storage"]
#}
#print(mobile)

#access items

#student={"name":"geetha","age":19,"course":"CSE"}
#print(student["name"])

#student={"name":"geetha","age":19}
#print(student.get("age"))
#print(student.get("marks"))

#d={"a":1,"b":2,"c":3}
#print(d.keys())

#d={"a":10,"b":20}
#print(d.items())

#d={"a":10,"b":20}
#print(d.values())

#print all keys and values
#d={"maths":90,"physics":80,"chem":85}
#print(d.get("maths"))
#print(d.get("physics"))
#print(d.get("chem"))

#check if key exists
#d={"name":"geetha","age":19}
#if "course" in d:
#    print("yes")
#else:
#    print("no"))

#d={"a":10,"b":20}
#key="c"
#print(d.get(key))

#d={"a":10,"b":20}
#key="c"
#print(d["c"])

#d={"x":1,"y":2}
#print("x" in d)
#print(1 in d)

#dict={
#   "brand":"ford",
#   "model":"mustang",
#   "year":1964
#}
#dict["year"]=2018
#print(dict)

#dict={
#    "brand":"ford",
#    "model":"mustang",
#    "year":1964
#}
#dict.update({"year":2020})
#print(dict)

#dict={
#    "brand":"ford",
#    "model":"mustang",
#    "year":1964
#}
#dict["color"]="red"
#print(dict)

#dict={
#    "brand":"ford",
#    "model":"mustang",
#    "year":1964
#}
#dict.pop("model")
#print(dict)

#dict={
   # "brand":"ford",
  #  "model":"mustang",
 #   "year":1964
#}
#dict.popitem()
#print(dict)

#dict={
 #   "brand":"ford",
 #   "model":"mustang",
 #   "year":1964
#}
#del dict["brand"]
#print(dict)

#dict={
#    "brand":"ford",
#    "model":"mustang",
#    "year":1964
#}
#del dict
#print(dict)

#dict={
#    "brand":"ford",
#    "model":"mustang",
#    "year":1964
#}
#dict.clear()
#print(dict)

#practice questions

#d={"a":1}
#d.pop("b")
#print(d)

#d={"a":1,"b":0,"c":3,"d":0}
#d.pop("b")
#d.pop("d")
#print(d)

#change items
#1.change the value of "math" from 90 to 100
#marks={"math":90,"phy":80}
#marks["math"]=100
#print(marks)

#Q2.Increase all values in a dictionary by 10.
#d = {"a":10, "b":20}
#for k in d:
#    d[k]+=10
#print(d)

#🔹 Add Items
#Q3Add a new key "chem" with value 85.
#d={}
#d["chem"]=85
#print(d)

#Q4Merge two dictionaries:
#d1 = {"a":1, "b":2}
#d2 = {"c":3}
#d1.update(d2)
#print(d1)

#Q5.Add a key only if it doesn’t already exist.
#d={
#    "a":1,"b":2
#}
#if "c" not in d:
#    d["c"]=3
#print(d)

#🔹 Remove Items
#Q6.Remove key "b" safely (no error if not present).
#d={"a":1,"c":3}
#d.pop("b",none)
#print(d)

#Q7.Remove all keys whose value is 0.
#d = {"a":1, "b":0, "c":3, "d":0}
#d={k:v for k,v in d.items() if v!=0}
#print(d)

#Q8.Delete the dictionary completely.
#d={"a":1,"b":2,"c":3}
#del d

#Q9.Remove the last inserted item from a dictionary.
#d={"a":1,"b":2,"c":3}
#d.popitem()
#print(d)

#loops
#1.print all keys
#d={"a":10,"b":20,"c":30}
#for i in d.keys():
#    print(i)

#2.print all values
#d={"a":10,"b":20,"c":30}
#for i in d.values():
#    print(i)

#3.print key value pairs in format
#d={"a":10,"b":20,"c":30}
#for x,y in d.items():
#    print(x,y)

#4.add 5 to all values using loops
#d={"a":10,"b":20,"c":30}
#for k in d:
#     d[k]=d[k]+5
#print(d)


#5.count total sum of values
#d={"a":10,"b":20,"c":30}
#count=0
#a+b+c==sum
#for i in d.values():
#    sum=count+i
#print(count)

#6.count no of keys&values
#d={"a":10,"b":20,"c":30}
#total=0
#for v in d.values():
#    total+=v
#print(total)

#7.find the key with max value
#d={"a":10,"b":20,"c":30}
#max_key=None
#max_val=-999
#for k,v in d.items():
  #  if v>max_val:
  #      max_val=v
 #       max_key=k
#print(max_key,max_val)


#8.create a new dict with squared values
#d={"a":2,"b":3}
#newd={}
#for k,v in d.items():
#    newd[k]=v*v
#print(newd)

#print all keys & values in one line
#d={"a":10,"b":20,"c":30}
#for k,v in d.items():
 #   print(k,v,end=" ")  

#find max value using loop
#d={"a":10,"b":20,"c":30}
#max_key=None
#max_value=-999
#for k,v in d.items():
#    if v>max_value:
#     max_value=v
#     max_key=k
#print(max_key,max_value)

#find min value unsing loop
#d={"a":10,"b":20,"c":30}
#min_key=None
#min_val=999
#for k,v in d.items():
#    if v <min_val:
#        min_val=v
#        min_key=k
#print(min_key,min_val)

#add 10 to all values
#d={"a":10,"b":20,"c":30}
#for k in d.keys():
#    d[k]+=10
#print(d)

#create a square dict
#a={"a":1,"b":2,"c":3}
#newd={}
#for k,v in a.items():
#    newd[k]=v*v
#print(newd)

#create a 3 dicts in a dict
#myfamily={
 #  "child1":{
  #    "name":"geetha",
   #   "year":2004
  # },
  # "child2":{
  #     "name":"swetha",
  #     "age":20
  # },
  # "child3":{
  #     "name":"swathi",
  #     "age":18
  # }
#}
#print(myfamily)

#child1={
  # "name":"geetha",
 #   "year":2004
#},
#child2={
   #    "name":"swetha",
  #     "age":20
 #  },
#child3={
   #    "name":"swathi",
  #     "age":18
 #  }
#myfamily={
   #"child1":child1,
  # "child2":child2,
 #  "child3":child3

#}
#print(myfamily)

#copy a dict and change value in new dict without affecting original
#d={"a":1,"b":2}
#newd={}
#newd=d.copy()
#newd["a"]=5
#print(newd)

#check if 2 dicts refer to the same memory
#d1={"a":1,"b":2}
#d2=d1
#print(d2)

#print all subs and marks
#student={
#    "marks":{
#        "math":75,
#        "science":87
#    }
#}
#print(student)

#increase all marks by 5
#student={
   # "marks":{
   #     "math":75,
  #      "science":87
 #   }
#}
#for sub in student["marks"]:
 #   student["marks"][sub]+=5
#print(student)

#add new sub chem=85
#student={
  #  "marks":{
 #       "math":75,
#        "science":87
#    }
#}
#student["chem"]=85
#print(student)

#find sub with highest marks
#student={
    #"marks":{
    #    "math":75,
   #     "science":87,
  #      "chem":85
 #   }
#}
#max_sub=None
#max_val=-999
#for sub,marks in student["marks"].items():
   # if marks>max_val:
  #   max_val=marks
 #    max_sub=sub
#print(max_sub,max_val)

#convert nested dict to flat dict
import copy
d1={"a":1,"b":{"x":10,"y":20}}
d2=copy.deepcopy(d1)
print(d2)








    




