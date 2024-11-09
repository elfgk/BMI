# BMI Hesaplayıcı 🧮

Bu uygulama, kullanıcının vücut kitle indeksini (BMI) ve ideal kilosunu hesaplamasına yardımcı olan bir Tkinter tabanlı Python uygulamasıdır. Boy ve kilo değerlerini girerek kullanıcı, BMI sonucunu ve sağlık kategorisini görebilir. Ayrıca, cinsiyet seçimine göre ideal kilo hesaplaması da yapılmaktadır.

## Özellikler

- **BMI Hesaplama**: Kullanıcının BMI değerini hesaplar ve BMI kategorisini belirler.
- **İdeal Kilo Hesaplama**: Kullanıcının cinsiyetine göre ideal kilosunu hesaplar.
- **Geçmiş Hesaplamalar**: Önceki hesaplamalar listelenir ve geçmiş sonuçlar saklanır.
- **Renkli ve Etkileşimli Arayüz**: Pembe ve yeşil renklerle kullanıcı dostu bir arayüz sunar.

## Gereksinimler

- Python 3.x
- Tkinter (Python ile birlikte gelir)

## Kurulum ve Çalıştırma

1. Python yüklü değilse [Python'u indirip yükleyin](https://www.python.org/downloads/).
2. Uygulamayı başlatmak için terminalde aşağıdaki komutu çalıştırın:
   ```bash
   python bmi_hesaplayici.py

**Kullanım**
-Boyunuzu ve kilonuzu girin.

-Cinsiyetinizi seçin.

-Hesapla butonuna basarak BMI değerinizi ve kategorinizi görebilirsiniz.

-İdeal kilo hesaplaması için İdeal Kilo butonunu kullanın.

-Geçmiş hesaplamaları görmek için Öncekiler butonuna basabilirsiniz.


**Özet**
BMI Değerleri:

<18.5: Aşırı zayıf

18.5 - 24.9: Normal kilolu

25 - 29.9: Hafif şişman

30 - 34.9: Orta derece şişman (1. derece)

35 - 39.9: Ağır derece şişman (2. derece)

40: Çok ağır derecede şişman (3. derece)



**İdeal Kilo Hesaplama:**

Erkek: 50 + 2.3 * (boy / 2.54 - 60)

Kadın: 45.5 + 2.3 * (boy / 2.54 - 60)
