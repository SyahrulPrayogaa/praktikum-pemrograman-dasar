# program 31
import this


print("=====Program 31=====")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# program 32
print("=====Program 32=====")
x = thisdict["model"]
y = thisdict.get("model")
print(x)
print(y)

# program 33
print("=====Program 33=====")
thisdict["year"] = 2020
print(thisdict)

# program 34
print("=====Program 34=====")
for x in thisdict:
    print(x)
    print(thisdict[x])

# program 35
print("=====Program 35=====")
for x in thisdict.values():
    print(x)

# program 36
print("=====Program 36=====")
for x, y in thisdict.items():
    print(x, y)

# program 37
print("=====Program 37=====")
thisdict["color"] = "red"
print(thisdict)

# program 38
print("=====Program 38=====")
thisdict.pop("model")
print(thisdict)

# program 39
print("=====Program 39=====")
thisdict.popitem()
print(thisdict)
