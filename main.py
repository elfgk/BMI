from tkinter import *

window= Tk()
window.title("BMI")
window.minsize(300,300)
window.config(padx=20,pady=20)
window.config(bg="white")

boy_yazisi= Label(text="Boyunuzu giriniz:")
boy_yazisi.config(bg="pink")
boy_yazisi.config(fg="green")
boy_yazisi.config(padx=20, pady=20)
boy_yazisi.pack()

boy_degeri = Entry(width= 20)
boy_degeri.pack()

kilo_yazisi= Label(text="Kilonuzu giriniz:")
kilo_yazisi.config(bg="pink")
kilo_yazisi.config(fg="green")
kilo_yazisi.config(padx=20, pady=20)
kilo_yazisi.pack()

kilo_degeri= Entry(width= 20)
kilo_degeri.pack()

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
        sonuc_degeri.config(text=f"BMI: {bmi:.2f}")

    except ValueError:
        sonuc_degeri.config(text="Hatalı Giriş")

sonuc_degeri= Label(text="")
sonuc_degeri.config(bg="pink")
sonuc_degeri.config(fg="green")
sonuc_degeri.config(padx=20, pady=20)
sonuc_degeri.pack()

hesaplama_butonu= Button(text = "Hesapla", command = hesapla)
hesaplama_butonu.config(padx = 10, pady =10)
hesaplama_butonu.pack()

window.mainloop()