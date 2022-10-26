vokalKecil = "aiueo"
kecil = "abcdefghijklmnopqrstuvwxyz"
besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
vokalBesar = "AIUEO"

# kalimat = str(input("Masukkan Kalimat Yang Ingin di Enkripsi: "))
kalimat = "Aku Cinta Padamu"
listKalimat = list(kalimat)
for x in listKalimat:
    if x in vokalKecil:
        index = kecil.find(x) + 1
        newIndex = listKalimat.index(x)
        if x == ' ':
            listKalimat[newIndex] = ' '
        else:
            listKalimat[newIndex] = kecil[index]
    elif x in vokalBesar:
        index = besar.find(x) + 1
        newIndex = listKalimat.index(x)
        if x == ' ':
            listKalimat[newIndex] = ' '
        else:
            listKalimat[newIndex] = besar[index]

result = ''.join(listKalimat)
print("Kalimat Sebelum Enkripsi")
print(kalimat)
print("==========================")
print("Kalimat Sesudah Enkripsi")
print(result)
