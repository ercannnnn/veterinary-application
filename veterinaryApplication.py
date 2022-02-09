def veteriner_app():
    kullanici_adi = "veterinerim"
    sifre = "012345"

    while True:
        
        kullanici_girisi = input("Kullanıcı Adını Giriniz: ")
        sifre_girisi = input("Şifrenizi Giriniz: ")

        if ((kullanici_girisi == kullanici_adi) and (sifre_girisi == sifre)):
            print("Giriş Başarılı... Hoşgeldiniz")
            break
        elif ((kullanici_girisi != kullanici_adi) and (sifre_girisi == sifre)):
            print("Kullanıcı Adı Hatalı... Lütfen Tekrar Deneyiniz...")
        elif ((kullanici_girisi == kullanici_adi) and (sifre_girisi != sifre)):
            print("Şifre Hatalı... Lütfen Tekrar Deneyiniz...")
        else:
            print("Tekrar Deneyiniz...")

    input("Devam etmek için ENTER tuşuna basınız...")

    class Hayvan:
        def __init__(self, tur, cins, isim, yas, acıklama):
            self.tur = tur
            self.cins = cins
            self.isim = isim
            self.yas = yas   
            self.acıklama = acıklama
        def bilgileri_goster(self):
            print("Hayvan türü: ",self.tur)
            print("Hayvan cinsi: ",self.cins)
            print("Hayvan ismi: ",self.isim)
            print("Hayvan yaşı: ",self.yas)
            print("Hayvan açıklama: ",self.acıklama)
    hayvan1 = Hayvan("Terrier", "Cairn Terrier", "Maskot", 3, "Ev köpeği")
    hayvan1.bilgileri_goster()
    hayvan2 = Hayvan("Heeler", "Texas Heeler", "Boncuk", 4, "Sokak köpeği")
    hayvan2.bilgileri_goster()
    hayvan3 = Hayvan("Dachshund", "Mini Dachshund", "Cesur", 5, "Bahçe köpeği")
    hayvan3.bilgileri_goster()

    class Hayvan_sahibi:
        def __init__(self, adSoyad, iletisimBilgileri, telefon, eposta, hayvani):
            self.adSoyad = adSoyad
            self.iletisimBilgileri = iletisimBilgileri
            self.telefon = telefon
            self.eposta = eposta
            self.hayvani = hayvani
        def bilgileri_goster(self):
            print("Hayvan Sahibi Adı Soyadı: ",self.adSoyad)
            print("Hayvan Sahibi İletişim Bilgileri: ",self.iletisimBilgileri)
            print("Hayvan Sahibi Telefon: ",self.telefon)
            print("Hayvan Sahibi Eposta: ",self.eposta)
            print("Sahip Olduğu Hayvan: ",self.hayvani)
    sahip1 = Hayvan_sahibi("Ali Acar", "Ankara", 5321234567, "aliacar@gmail.com", "Maskot")
    sahip1.bilgileri_goster()
    sahip2 = Hayvan_sahibi("Ayşe Yıldız", "İstanbul", 5331234567, "ayseyildiz@gmail.com", "Boncuk")
    sahip2.bilgileri_goster()
    sahip3 = Hayvan_sahibi("Veli Yılmaz", "İzmir", 5341234567, "veliyilmaz@hotmail.com", "Cesur")
    sahip3.bilgileri_goster()

while True:
    veteriner_app()
    soru=input("Arama yapmak ister misiniz? yes/no")
    if soru=="no":
        break
    elif soru=="yes":
        arama1=input("Hayvan adına göre arama yapmak ister misiniz? yes/no")
        if arama1=="yes":
            arama2=input("Bir hayvan ismi giriniz...")
            if arama2=="Maskot":
                hyvn1=("Terrier", "Cairn Terrier", "Maskot", 3, "Ev köpeği")
                print("Maskotun Bilgileri: ",hyvn1)
            elif arama2=="Boncuk":
                hyvn2=("Heeler", "Texas Heeler", "Boncuk", 4, "Sokak köpeği")
                print("Boncuğun Bilgileri: ",hyvn2)
            elif arama2=="Cesur":
                hyvn3=("Dachshund", "Mini Dachshund", "Cesur", 5, "Bahçe köpeği")
                print("Cesurun Bilgileri: ",hyvn3)
        elif arama1=="no":
            pass
        arama3=input("Hayvan sahibine göre arama yapmak ister misiniz? yes/no")
        if arama3=="yes":
            arama4=input("Bir hayvan sahibi ismi giriniz...")
            if arama4=="Ali Acar":
                shp1=("Ali Acar", "Ankara", 5321234567, "aliacar@gmail.com", "Maskot")
                print("Hayvan Sahibi Bilgileri: ",shp1)
            elif arama4=="Ayşe Yıldız":
                shp2=("Ayşe Yıldız", "İstanbul", 5331234567, "ayseyildiz@gmail.com", "Boncuk")
                print("Hayvan Sahibi Bilgileri: ",shp2)
            elif arama4=="Veli Yılmaz":
                shp3=("Veli Yılmaz", "İzmir", 5341234567, "veliyilmaz@hotmail.com", "Cesur")
                print("Hayvan Sahibi Bilgileri: ",shp3)
        elif arama3=="no":
            pass

    karar=input("Tekrar giriş yapmak ister misiniz? yes/no")
    if karar=="no":
        break
    
        


