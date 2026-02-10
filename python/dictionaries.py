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

d={"x":1,"y":2}
print("x" in d)
print(1 in d)