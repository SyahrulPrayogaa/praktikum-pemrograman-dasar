# Tulislah program sederhana untuk membuktikan penggunaan operator aritmetika, operator pembanding, operator logika, operator assignment, operator identitas, dan operator keanggotaan 

# 1. Operator Aritmetika
# Menghitung Luas Segitiga
def luasSegitga():
  x = 7
  y = 10
  hasil = x*y/2
  print(hasil)

print("==================Aritmetika==================")
luasSegitga()

# 2. Operator Assignment
# Menghitung Pangkat suatu bilangan
def pangkatBilangan():
  a = 2
  a **=3
  print (a)

print("==================Assignment==================")
pangkatBilangan()

# 3. Operator Pembanding
# Mengidentifikasi apakah bilangan sama atau tidak
def pembanding():
  x = 3
  y = 3
  print (x==y)

print("==================Pembanding==================")
pembanding()

# 4. Operator Logika
# mengecek apakah bilangan ada diantara 2 buah bilangan misalnya mengecek bilangan 5 apakah benar ada diantara bilangan 1-10
def cekBilangan(angkaAwal,angkaAkhir,cariAngka):
  if(cariAngka >= angkaAwal and cariAngka <= angkaAkhir):
    print('Selamat, angka ',cariAngka,' berada diantara angka ',angkaAwal,' dan ',angkaAkhir)
  else:
    print('Maaf, angka ',cariAngka,' tidak berada diantara angka ',angkaAwal,' dan ',angkaAkhir)

print("==================Logika==================")
cekBilangan(1,7,7)

# 5. Operator Identitas
# membandingkan 2 buah objek yang sama. disini digunakan dua buah tuples untuk objek yang akan dibandingkan.
def perbandinganObjek():
  x = (5,6,7)
  y = (5,6,7)
  print (x is y)

print("==================Perbandingan==================")
perbandinganObjek()

# 6. Operator Keanggotaan
# mencari sebuah elemen dalam sebuah objek
def searchObject(x):
  data = ('mangga','pisang','jeruk')
  if(x in data):
    print(x , ' masuk kedalam anggota buah-buahan')
  else:
    print('Maaf ', x , ' tidak termasuk dalam anggota buah-buahan')

print("==================Keanggotaan==================")
searchObject('pisang')


