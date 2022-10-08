x = "mesin"
def myfunc():
  global x #syntax global pada baris 3 ini akan mengambil variabel yang berada diluar fungsi dan dimasukkan kedalam fungsi.
  x = "Elektro"
myfunc()
print("Teknik " + x)
