# Dictionary allow you to store key value pair eg: telephone directory

d = {"tom": 7847462839, "rob": 2323242342342, "Joe": 432423423423}
print(d)
print(d["tom"])

# add into dictionary
d["sam"] =2423434546547
print(d)

# delete from dictionary
del d["sam"]
print(d)

for key in d:
    print("key:", key, "value:", d[key])

# using tuples
for k,v in d.items():
    print("key:",key, "value:",v)

print("tom" in d)
print("samir" in d)
d.clear()
print(d)

#Tuples is a list vlues ggrouped together
point = (5,9)
