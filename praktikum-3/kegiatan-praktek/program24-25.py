# program 24
print("=====Program 24=====")
x = ("pepaya", "mangga", "pisang")
y = list(x)
y[1] = "jambu"
x = tuple(y)
print(x)

# program 25
print("=====Program 25=====")
thistuple = ("pepaya", "mangga", "pisang")
del thistuple
print(thistuple)  # Output akan error karena thistuple sudah dihapus
