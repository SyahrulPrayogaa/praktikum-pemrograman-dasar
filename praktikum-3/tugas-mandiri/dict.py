# =========Dictionary==================

# Membuat Dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# mengakses Dictionary
print('=========Mengakses Dictionary=========')
print(car.get("brand"))
for x in car:
    print(x)
    print(car[x])

# menambahkan Dictionary
print('=========Menambahkan Dictionary=========')
car["color"] = "Blue"
print(car)

# Mengubah Dictionary
print('=========Mengubah Dictionary=========')
car["year"] = 2022
print(car)

# menghapus item Dictionary
print('=========Menghapus Dictionary=========')
car.popitem()
print(car)
