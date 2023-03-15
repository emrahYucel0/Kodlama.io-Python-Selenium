class Matematik:
    def topla(self,sayi1,sayi2):
        return sayi1 + sayi2
    def cıkar(self,sayi1,sayi2):
        return sayi1 - sayi2
    
matematik = Matematik()
sonuc1 = matematik.topla(10,5)
sonuc2 = matematik.cıkar(10,5)
print(f"Toplama sonucu: {sonuc1}, Çıkarma sonucu: {sonuc2}")

class Matematik2:
    def __init__(self,sayi1,sayi2): #constructor
        self.s1 = sayi1 # genel kullanım self.sayi1 = sayi1
        self.s2 = sayi2
        print("Matematik Başladı(referans oluştu)")
    def topla(self):
        return self.s1 + self.s2 # self kendi demek yani self = Matematik2 de oluşturduğumuz s1, sayi1 değil
    def cıkar(self):
        return self.s1 - self.s2
    def bol(self):
        return self.s1 / self.s2
    def carp(self):
        return self.s1 * self.s2
    
matematik2 = Matematik2(100,10) 
print(f"Toplam: {matematik2.topla()}, Fark: {matematik2.cıkar()}, Bölüm: {matematik2.bol()}, Çarpım: {matematik2.carp()}") 

class Istatistik(Matematik2):
    def __init__(self,sayi1,sayi2):
        super().__init__(sayi1,sayi2)#super() metodu = Üst-sınıfa ait nesne yaratma: Bir alt-sınıf, super() metodunu kullanarak, 
    def kalan(self):                 #üst sınıfının bir nesnesini yaratabilir ve onun değişkenlerine değer atayabilir.
        return self.s1 % self.s2 
    
istatistik = Istatistik(9,3)
print(f"Kalan : {istatistik.kalan()}")