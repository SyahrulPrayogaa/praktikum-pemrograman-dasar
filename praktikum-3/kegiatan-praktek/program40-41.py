# program 40
print("=====Program 40=====")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

# program 41
print("=====Program 41=====")
del thisdict
# this will cause an error because "thisdict" no longer exists.
print(thisdict)
