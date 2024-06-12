from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta
import pandas as pd

pd.set_option('display.width', 100000)
pd.set_option('display.max_columns', 20)  # Görüntülenen maksimum sütun sayısını da ayarlayabilirsiniz.


try:

    #personel, hasta, doktor ve hemşire için nesneler üretildi ve bilgiler __str__ metodu aracılığıyla yazdırıldı
    personel1=Personel(1,"Eyşan","TEZCAN","Temizlik",6000)
    personel2=Personel(2,"Cengiz","ATAY","Güvenlik",7700)

    print("\n")
    print(personel1)
    print(personel2)

    doktor1=Doktor(101,"Levent","ATAHANLI","Doktor", 25000, "Acil", 6, "Buca Kadın Doğum ve Çocuk Hastalıkları Hastanesi")
    doktor2=Doktor(102,"Ela","ALTINDAĞ","Doktor", 25500, "Nöroloji", 8, "Buca Kadın Doğum ve Çocuk Hastalıkları Hastanesi")
    doktor3=Doktor(103,"Hasan","TURAY","Doktor", 22500, "Ortopedi", 4, "Buca Seyfi Demirsoy Devlet Hastanesi")

    print("\n")
    print(doktor1)
    print(doktor2)
    print(doktor3)

    hemsire1=Hemsire(201, "Melek", "SAĞIROĞLU", "Hemşire", 12000, 40, "Tem. İlk Yard", "Buca Seyfi Demirsoy Devlet Hastanesi")
    hemsire2=Hemsire(202, "İlhan", "KILIÇ", "Hemşire", 10000, 38, "Yoğ Bak. Sertif.", "Buca Seyfi Demirsoy Devlet Hastanesi")
    hemsire3=Hemsire(203, "Delfin", "KAYA", "Hemşire", 9500, 35, "Yoğ. Bak. Sertif.", "Buca Kadın Doğum ve Çocuk Hastalıkları Hastanesi")

    print("\n")
    print(hemsire1)
    print(hemsire2)
    print(hemsire3)

    hasta1=Hasta(301,"Mustafa", "DEMİR", "1990-10-28", "Kalp Hastalığı", ["İlaç Tedavisi", "Diyet", "Egzersiz"])
    hasta2=Hasta(302,"Erdem", "YILMAZ", "2000-06-26", "Diabet", ["İnsülin", "Diyet"])
    hasta3=Hasta(303,"Mehmet", "TOPAL", "1980-05-20", "Hipertansiyon", ["İlaç Tedavisi"])
    print("\n")
    print(hasta1)
    print(hasta2)
    print(hasta3)


    
    #Tüm personel, doktor, hemşire ve hasta nesnelerinin özelliklerinden bir pandas DataFrame oluşturuldu.
    #(personel_no, ad,soyad, departman, maas, uzmanlik, deneyim_yili,hastane,
    #calisma_saati, sertifika,hasta_no, dogum_tarihi, hastalik, tedavi)
    data = []
    #Boş oşan değişkenlere 0 atandı.
    for personel in [personel1, personel2]:
        data.append([personel.get_personel_no(), personel.get_ad(), personel.get_soyad(), personel.get_departman(), personel.get_maas(), 0, 0, 0, 0, 0, 0, 0, 0, 0])

    for doktor in [doktor1, doktor2, doktor3]:
        data.append([doktor.get_personel_no(), doktor.get_ad(), doktor.get_soyad(), doktor.get_departman(), doktor.get_maas(), doktor.get_uzmanlik(), doktor.get_deneyim_yili(), doktor.get_hastane(), 0, 0, 0, 0, 0, 0])

    for hemsire in [hemsire1, hemsire2, hemsire3]:
        data.append([hemsire.get_personel_no(), hemsire.get_ad(), hemsire.get_soyad(), hemsire.get_departman(), hemsire.get_maas(), 0, 0, hemsire.get_hastane(), hemsire.get_calisma_saati(), hemsire.get_sertifika(), 0, 0, 0, 0])

    for hasta in [hasta1, hasta2, hasta3]:
        data.append([0, hasta.get_ad(), hasta.get_soyad(), 0, 0, 0, 0, 0, 0, 0, hasta.get_hasta_no(), hasta.get_dogum_tarihi(), hasta.get_hastalik(), hasta.get_tedavi()])

    sutun = ["personel_no", "ad", "soyad", "departman", "maas", "uzmanlik", "deneyim_yili", "hastane", "calisma_saati", "sertifika", "hasta_no", "dogum_tarihi", "hastalik", "tedavi"]

    df = pd.DataFrame(data, columns=sutun)
    

    print("DataFrame=")
    print(df)

    # Doktorları uzmanlık alanlarına göre gruplama ve sayısını yazdırma
    df_uzmanlik=df.groupby("uzmanlik")
    doktor_grup_sayisi = df_uzmanlik.size()
    print("Doktorların uzmanlık alanlarına göre gruplanmış toplam sayısı:")
    print(doktor_grup_sayisi)
   
    # 5 yıldan fazla deneyime sahip doktorların toplam sayısı
    deneyimli_doktor_sayisi = df[(df["departman"] == "Doktor") & (df["deneyim_yili"] > 5)].shape[0]
    print("5 yıldan fazla deneyime sahip doktorların toplam sayısı:", deneyimli_doktor_sayisi)

    # Hasta adına göre DataFrame’i alfabetik olarak sıralama
    siralanmis_df = df[(df['hasta_no'].notna()) & (df['hasta_no'] > 0)].sort_values(by=['ad', 'soyad'])
    print("Hasta adına göre alfabetik olarak sıralanmış DataFrame:")
    print(siralanmis_df)

    # Maasi 7000 yuksek personeller
    maas_ustunde_personel = df[df["maas"] > 7000]
    print("Maaşı 7000 TL üzerinde olan personeller:")
    print(maas_ustunde_personel) 
    # Doğum tarihi 1990 ve sonrası olan hastalar
    dogum_tarihi_ustunde_hastalar = df[df["dogum_tarihi"].apply(lambda x: int(x.split("-")[0]) if x else 0) >= 1990]
    print("Doğum tarihi 1990 ve sonrası olan hastalar:")
    print(dogum_tarihi_ustunde_hastalar)

    # Yeni DataFrame'i oluşturma (ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastalik, tedavi)
    yeni_df = df[["ad", "soyad", "departman", "maas", "uzmanlik", "deneyim_yili", "hastalik", "tedavi"]]
    print("Yeni DataFrame:")
    print(yeni_df)
except Exception as e:
    print(e)
    

