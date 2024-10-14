from tkinter import *
pencere= Tk()
pencere.title("BMI")
pencere.minsize(600, 400)
pencere.config(bg="white")
pencere.geometry ("400x400+500+200") #sağ 500, yukarı 200

pencere.grid_rowconfigure(0, weight=1)
pencere.grid_rowconfigure(8, weight=1)
pencere.grid_columnconfigure(0, weight=1)
pencere.grid_columnconfigure(3, weight=1)

boy_yazisi= Label(text="Boyunuzu giriniz:",bg="pink",fg="green")
boy_yazisi.grid(column=1, row=1, sticky="w",padx=5, pady=5)

boy_degeri = Entry(width= 20)
boy_degeri.focus()
boy_degeri.grid(column=1,row=2,sticky="w",padx=5, pady=5)

kilo_yazisi= Label(text="Kilonuzu giriniz:",bg="pink",fg="green")
kilo_yazisi.grid(column=1,row=3, sticky="w",padx=5, pady=5)

kilo_degeri= Entry(width= 20)
kilo_degeri.grid(column=1,row=4,sticky="w",padx=5, pady=5)

metin= Label(height=1,width=20)
metin.grid(column=1,row=5,sticky="w",padx=5, pady=5)

onceki_hesaplamalar_listesi=[]
onceki_hesaplamalar_list= Listbox(pencere)
onceki_hesaplamalar_list.config(height=10, width=25)
onceki_hesaplamalar_list.grid(column=3, row=2, rowspan=6, padx=5, pady=5)

ideal_kilo_listesi=[]
ideal_kilo_list= Listbox(pencere)
ideal_kilo_list.config(height=10, width=25)
ideal_kilo_list.grid(column=4, row=2, rowspan=6, padx=5, pady=5)

def hesapla():
    if not kilo_degeri.get() or not boy_degeri.get():
        sonuc_degeri.config(text="Lütfen geçerli sayı girin")
        return
    try:
        kilo = float(kilo_degeri.get())
        boy = float(boy_degeri.get())
        if boy > 3:
            boy = boy / 100
        bmi = kilo / (boy ** 2)
        if  bmi not in onceki_hesaplamalar_listesi:
            onceki_hesaplamalar_listesi.append(bmi)
            onceki_hesaplamalar_list.insert(END, f"BMI: {bmi:.2f}")  # Hesaplamayı listbox'a ekle

            if bmi < 18.5:
                metin.config(text="Aşırı zayıfsınız")

            elif 18.5 < bmi < 24.9:
                metin.config(text="Normal kilolu")

            elif 25 < bmi < 29.9:
                metin.config(text="hafif şişman")

            elif 30 < bmi < 34.9:
                metin.config(text="orta derecede şişman(1.derece)")

            elif 35 < bmi < 39.9:
                metin.config(text="Ağır derecede şişman(2.derece)")

            elif bmi > 40:
                metin.config(text="Çok ağır derecede şişman(3.derece)")

            sonuc_degeri.config(text=f"BMI: {bmi:.2f}")

            print(onceki_hesaplamalar_listesi)

    except ValueError:
        sonuc_degeri.config(text="Hatalı Giriş")
def onceki_hesaplamalar():
    print(onceki_hesaplamalar_listesi)
def ideal_kilo():
    kilo = float(kilo_degeri.get())
    boy = float(boy_degeri.get())

    if cinsiyet.get()== "kadin":
        ideal_kilo= 45.5+2.3*(boy/2.54-60)
        if ideal_kilo not in ideal_kilo_listesi:
            ideal_kilo_listesi.append(ideal_kilo)
            ideal_kilo_list.insert(END, f"İdeal Kilo: {ideal_kilo:.2f}")
    elif cinsiyet.get()== "erkek":
        ideal_kilo = 50 + 2.3 * (boy / 2.54 - 60)
        if ideal_kilo not in ideal_kilo_listesi:
            ideal_kilo_listesi.append(ideal_kilo)
            ideal_kilo_list.insert(END, f"İdeal Kilo: {ideal_kilo:.2f}")  # ideal kiloyu listboxa ekle
    else: print("Lütfen cinsiyetinizi seçiniz")

def calistir():
    hesapla()
    ideal_kilo()

cinsiyet= StringVar()
cinsiyet.set(None)
erkek_rb = Radiobutton(pencere, text="Erkek", variable= cinsiyet, value="erkek")
erkek_rb.grid(row=1, column=2, padx=5, pady=5)
kadin_rb = Radiobutton(pencere, text="Kadın", variable= cinsiyet, value="kadin")
kadin_rb.grid(row=2, column=2, padx=5, pady=5)


sonuc_degeri=Label(text="")
sonuc_degeri.config(bg="pink",fg="green")
sonuc_degeri.grid(column=1,row=6,sticky="w",padx=5, pady=5)

hesaplama_butonu= Button(text = "Hesapla", command = calistir)
hesaplama_butonu.grid(column=1,row=7,sticky="w",padx=5, pady=5)

onceki_hesaplamalar_butonu= Button(text="Öncekiler", command = onceki_hesaplamalar)
onceki_hesaplamalar_butonu.grid(column=3,row=1,padx=5, pady=5)

ideal_kilo_butonu= Button(text="İdeal Kilo", command =ideal_kilo)
ideal_kilo_butonu.grid(column=4,row=1,padx=5, pady=5)

pencere.mainloop()