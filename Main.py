from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta


personel1=Personel(1,"Eyşan","TEZCAN","Temizlik",6000)
personel2=Personel(2,"Cengiz","ATAY","Güvenlik",7700)

print("\n")
print(personel1)
print(personel2)

doktor1=Doktor(101,"Levent","ATAHANLI","Acil", 25000, "Acil", 6, "Buca Kadın Doğum ve Çocuk Hastalıkları Hastanesi")
doktor2=Doktor(102,"Ela","ALTINDAĞ","Nöroloji", 25500, "Nöroloji", 6, "Buca Kadın Doğum ve Çocuk Hastalıkları Hastanesi")
doktor3=Doktor(103,"Hasan","TURAY","Ortopedi", 22500, "Ortopedi", 6, "Buca Seyfi Demirsoy Devlet Hastanesi")

print("\n")
print(doktor1)
print(doktor2)
print(doktor3)

hemsire1=Hemsire(201, "Melek", "SAĞIROĞLU", "Acil", 12000, 40, "Temel İlk Yardım", "Buca Seyfi Demirsoy Devlet Hastanesi")
hemsire2=Hemsire(202, "İlhan", "KILIÇ", "Yoğun Bakım", 10000, 40, "Yoğun Bakım Sertifikası", "Buca Seyfi Demirsoy Devlet Hastanesi")
hemsire3=Hemsire(203, "Delfin", "KAYA", "Yoğun Bakım", 9500, 40, "Yoğun Bakım Sertifikası", "Buca Kadın Doğum ve Çocuk Hastalıkları Hastanesi")

print("\n")
print(hemsire1)
print(hemsire2)
print(hemsire3)

hasta1=Hasta(301,"Mustafa", "DEMİR", "1980-10-28", "Kalp Hastalığı", ["İlaç Tedavisi", "Diyet", "Egzersiz"])
hasta2=Hasta(302,"Erdem", "YILMAZ", "1964-06-26", "Diabet", ["İnsülin", "Diyet"])
hasta3=Hasta(303,"Mehmet", "TOPAL", "1980-05-20", "Hipertansiyon", ["İlaç Tedavisi"])
print("\n")
print(hasta1)
print(hasta2)
print(hasta3)


