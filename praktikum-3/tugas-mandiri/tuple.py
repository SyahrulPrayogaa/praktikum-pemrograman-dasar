# =========TUPLE==================

# Membuat Tuple
mobil = ("BMW", "Tesla", "Mercedes")

# mengakses Tuple
print(mobil)
print(mobil[0])

# menambahkan Tuple
listMobil = list(mobil)
listMobil.append("Ferrari")
mobil = tuple(listMobil)
print(mobil)

# Mengubah Tuple
listMobil = list(mobil)
listMobil[0] = "Audi"
mobil = tuple(listMobil)
print(mobil)

# menghapus item Tuple
print('=======menghapus item Tuple=========')
newListCar = list(mobil)
newListCar.pop(0)
tupleCar = tuple(newListCar)
print(tupleCar)

# menghapus Tuple
del mobil
print(mobil)  # perintah ini akan error karena tuple mobil sudah tidak tersedia
