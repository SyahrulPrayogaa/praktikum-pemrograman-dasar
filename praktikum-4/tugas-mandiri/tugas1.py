# Program Menghitung Panjang Sisi Miring Segitiga Siku-Siku

import math


alas = int(input("Masukkan Nilai Alas Segitiga : "))
tinggi = int(input("Masukkan Nilai Tinggi Segitiga : "))


sisiMiring = math.sqrt(pow(alas, 2)+pow(tinggi, 2))

print("Panjang Sisi Miring dari Segitiga adalah : ", round(sisiMiring, 3))
