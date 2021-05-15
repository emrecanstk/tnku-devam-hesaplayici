from selenium import webdriver
import tkinter as tk,time
from tkinter import messagebox

form = tk.Tk()
form.title("İkinci Dönem Devam Yüzdesi 1.1")
form.geometry("400x350+500+150")

baslik = tk.Label(text="Devam Yüzdesi Hesaplayıcı",font="Calibri 14").place(x=10,y=10)
yonerge = tk.Label(text="ALMS'ye girerken kullandığınız kullanıcı adı ve şifreyi giriniz.",font="Calibri 9").place(x=10,y=50)

text_kullanici_adi = tk.Label(text="Kullanıcı adı:")
text_sifre = tk.Label(text="Şifre:")
text_kullanici_adi.place(x=10,y=90)
text_sifre.place(x=10,y=110)

giris_kullanici_adi = tk.Entry()
giris_kullanici_adi.place(x=85,y=90)
giris_sifre = tk.Entry(show="•")
giris_sifre.place(x=85,y=110)

def hesapla():
    messagebox.showinfo(title="Hatırlatma",message="Chrome kendiliğinden kapanana kadar bekleyiniz!\n\n  Tekirdağ Namık Kemal Üniversitesi\n\n  Devam etmek için: Tamam")
    driver = webdriver.Chrome()
    driver.get("https://lms.nku.edu.tr/Account/LoginBefore")
    time.sleep(2)
    
    giris1 = driver.find_element_by_xpath('//*[@id="UserName"]')
    giris1.click()
    giris1.send_keys(giris_kullanici_adi.get())

    driver.find_element_by_xpath('//*[@id="btnLoginName"]').click()
    time.sleep(2)

    giris2 = driver.find_element_by_xpath('//*[@id="Password"]')
    giris2.click()
    giris2.send_keys(giris_sifre.get())
    driver.find_element_by_xpath('//*[@id="btnLoginPass"]').click()
    time.sleep(2)

    url = "https://lms.nku.edu.tr/Activity/Index?id=3D56E622B273372EE3D14C6FE43DF84E"
    driver.get(url)
    time.sleep(2)

    katilimlar = driver.find_elements_by_css_selector('.label.label-success')

    canli_yuzdeler,tekrar_yuzdeler = [],[]
    for i in katilimlar:
        katilim = i.text
        if "Canl" in katilim:
            c_ayriklar = katilim.split('%')
            canli_yuzdeler.append(int(c_ayriklar[1]))
        if "Tekr" in katilim:
            t_ayriklar = katilim.split('%')
            tekrar_yuzdeler.append(int(t_ayriklar[1]))

    driver.close()
    canli_sonuc = sum(canli_yuzdeler)/len(canli_yuzdeler)
    tekrar_sonuc = sum(tekrar_yuzdeler)/len(tekrar_yuzdeler)
    toplam_sonuc = canli_sonuc + tekrar_sonuc
    text_yuzde1 = tk.Label(text="Canlı Katılım: %",bg="Gray",font="Calibri 11").place(x=230,y=90)
    text_yuzde2 = tk.Label(text="Tekrar Katılım: %",bg="Gray",font="Calibri 11").place(x=230,y=110)
    text_yuzde3 = tk.Label(text="Toplam Katılım: %",bg="Gray",font="Calibri 11").place(x=230,y=130)
    text_canli_sonuc = tk.Label(text=round(canli_sonuc,2),bg="Gray",font="Calibri 11").place(x=325,y=90)
    text_tekrar_sonuc = tk.Label(text=round(tekrar_sonuc,2),bg="Gray",font="Calibri 11").place(x=334,y=110)
    text_toplam_sonuc = tk.Label(text=round(toplam_sonuc,2),bg="Gray",font="Calibri 11").place(x=341,y=130)

giris_yap_buton = tk.Button(text="Hesapla",command=hesapla)
giris_yap_buton.place(x=120,y=140)

nasil_calisir1 = tk.Label(text="Nasıl Çalışır?",font="Calibri 11").place(x=10,y=180)
nasil_calisir2 = tk.Label(text="Bu dönem girdiğiniz derslerin katılım yüzdelerini tek tek toplar",font="Calibri 9").place(x=10,y=204)
nasil_calisir3 = tk.Label(text="ve ortalamasını alır.",font="Calibri 9").place(x=10,y=220)
nasil_calisir4 = tk.Label(text="En güncel chrome sürümüne (90.0.4430) sahip olmalısınız.",font="Calibri 9").place(x=10,y=236)
gelistirici = tk.Label(text="-------------- Emre Can Satık --------------",font="Arial 9").place(x=90,y=280)
universite = tk.Label(text="Tekirdağ Namık Kemal Üniversitesi",font="Arial 10").place(x=90,y=300)
bolum = tk.Label(text="Yabancı Diller Yüksekokulu",font="Arial 8").place(x=126,y=320)

form.mainloop()