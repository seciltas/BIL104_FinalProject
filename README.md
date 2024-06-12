### Proje README Dosyası

## Proje Adı
Personel ve Hasta Yönetim Sistemi

## Proje Açıklaması
Bu proje, bir hastanedeki personel (doktor, hemşire ve diğer personel) ile hastaların bilgilerini yönetmek için tasarlanmıştır. Python programlama dili ve Pandas kütüphanesi kullanılarak geliştirilmiştir. Proje, personel ve hastaların çeşitli özelliklerini saklar ve üzerinde bazı analizler yapar.

## Gereksinimler
Bu proje aşağıdaki Python paketlerini gerektirir:
- pandas

Ayrıca aşağıdaki dosyalar ve class'lar gereklidir:
- `Personel.py`: Personel sınıfını içerir.
- `Doktor.py`: Doktor sınıfını içerir.
- `Hemsire.py`: Hemşire sınıfını içerir.
- `Hasta.py`: Hasta sınıfını içerir.

## Kurulum
Gerekli paketleri yüklemek için aşağıdaki komutu kullanın:
```bash
pip install pandas
```

## Kullanım
Projenin ana dosyasını çalıştırarak personel ve hasta bilgilerini ekleyebilir, düzenleyebilir ve analiz edebilirsiniz.

### Sınıflar ve Yöntemler

#### Personel Sınıfı (Personel.py)
- `Personel`: Personel bilgilerini temsil eder.
  - Özellikler: `personel_no`, `ad`, `soyad`, `departman`, `maas`
  - Yöntemler: `get_personel_no()`, `get_ad()`, `get_soyad()`, `get_departman()`, `get_maas()`

#### Doktor Sınıfı (Doktor.py)
- `Doktor`: Doktor bilgilerini temsil eder ve `Personel` sınıfından türetilmiştir.
  - Ek Özellikler: `uzmanlik`, `deneyim_yili`, `hastane`
  - Ek Yöntemler: `get_uzmanlik()`, `get_deneyim_yili()`, `get_hastane()`

#### Hemşire Sınıfı (Hemsire.py)
- `Hemsire`: Hemşire bilgilerini temsil eder ve `Personel` sınıfından türetilmiştir.
  - Ek Özellikler: `calisma_saati`, `sertifika`, `hastane`
  - Ek Yöntemler: `get_calisma_saati()`, `get_sertifika()`, `get_hastane()`

#### Hasta Sınıfı (Hasta.py)
- `Hasta`: Hasta bilgilerini temsil eder.
  - Özellikler: `hasta_no`, `ad`, `soyad`, `dogum_tarihi`, `hastalik`, `tedavi`
  - Yöntemler: `get_hasta_no()`, `get_ad()`, `get_soyad()`, `get_dogum_tarihi()`, `get_hastalik()`, `get_tedavi()`

