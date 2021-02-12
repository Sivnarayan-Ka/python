dict1 = {}
# print(type(dict1))
#keys are immutable
d2 = {"a":"fish","b":'curry',
    "12":"chicken",
    "inner_dict":{"B":"maggie","L":"rice","D":"kabab"}}
print(d2)
d3 = d2 # no new dict is created instead it is pointing to same memory
d4 = d2.copy() # shallow copy separate dict a copy of d2 is created

print(d2.keys())
print(d2.items())
d2[420] = "new value"
print(d2.values())
print(d2)
del d2[420]
print(d2)
print(d2["inner_dict"])
print(d2["inner_dict"]["L"])