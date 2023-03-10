yil = int(input("Yili giriniz: "))
if (yil - 2000) % 12 == 0:
    hayvan = 'Ejderha'
elif (yil - 2000) % 12 == 1:
    hayvan = 'Yılan'
elif (yil - 2000) % 12 == 2:
    hayvan = 'At'
elif (yil - 2000) % 12 == 3:
    hayvan = 'Koyun'
elif (yil - 2000) % 12 == 4:
    hayvan = 'Maymun'
elif (yil - 2000) % 12 == 5:
    hayvan = 'Horoz'
elif (yil - 2000) % 12 == 6:
    hayvan = 'Köpek'
elif (yil - 2000) % 12 == 7:
    hayvan = 'Domuz'
elif (yil - 2000) % 12 == 8:
    hayvan = 'Sıçan'
elif (yil - 2000) % 12 == 9:
    hayvan = 'Öküz'
elif (yil - 2000) % 12 == 10:
    hayvan = 'Kaplan'
else:
    hayvan = 'Tavşan'

print("Hayvan :",hayvan)