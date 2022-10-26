listVocal = "aiueo"
countVocal = 0
countConsonan = 0

kalimat = "tambalakada"
for x in kalimat:
    if x in listVocal:
        countVocal += 1
    else:
        countConsonan += 1

print("Jumlah Huruf Vokal = ", countVocal)
print("Jumlah Huruf Konsonan = ", countConsonan)
