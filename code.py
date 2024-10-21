rehber=[]
def secenekler():
    print("hoş geldiniz")
    print("1. kişi ekle")
    print("2.kişi sil")
    print("3. kişileri görüntüle")
    print("çıkış yap")

def kisiEkle():
    isim=input("isim:")
    soyisim=input("soyisim:")
    telefon=input("telefon:")
    email=input("e-mail:")
    rehber.append({"isim":isim,"soyisim":soyisim,"telefon":telefon,"email":email})
    print(f"{isim} rehbere eklendi")

def kisiSil():
    kisiNo=int(input("silmek istediğiniz kişinin numarasını giriniz:"))
    if 1<=kisiNo<len(rehber)+1:
        silinenKisi=rehber.pop(kisiNo-1)
        print("silme işlemi başarılı")
    else:
        print("girdiğiniz numaraya uygu kişi kaydı bulunamadı.")

def kisiGoster():
    if not rehber: print("rehber boş")
    else:
        print("rehber\n")

        for i, kisi in enumerate(rehber,1):
            print(f"{i}. isim: {kisi['isim']}, soyisim: {kisi['soyisim']}, telefon: {kisi['telefon']}, e-mail: {kisi['email']} ")

while True:
    secenekler()
    secim=int(input("yapmak istediğiniz işlemi girin(1/2/3/4):"))
    if secim==1:
        kisiEkle()
    elif secim==2:
        kisiSil()
    elif secim==3:
        kisiGoster()
    elif secim==4:
        print("çıkış yapıldı...")
        break
    else:
        print("bir hata  oluştu. yeniden deneyin...")
