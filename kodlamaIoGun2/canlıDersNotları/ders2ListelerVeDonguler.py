#tip dönüşümleri(type conversion)
faiz = 1.59
vade = 36
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade) + 12)
faiz = str(faiz)
print(type(faiz))

vade = input("Vade sayısını giriniz: ") #default string
print(vade)
print(type(vade))
print(int(vade) + 12) # sadece bu noktada tip dönüşümü yaptık

vade = int(input("Vade sayısını giriniz: ")) #bu noktadan itibaren tip dönüşür
print(vade)
print(type(vade))
vade = vade + 12

#string interpolation

print("Seçim sonucu yeni vade : " + str(vade))
print("Seçim sonucu yeni vade : {vadeSayisi}".format(vadeSayisi = vade))
print(f"Seçim sonucu yeni vade : {vade}")

#listeler
#döngüler
#fonksiyonlar

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))
print(krediler)

print(krediler[0])

print(len(krediler))

krediler.append("Özel kredi")# listenin sonuna ekleme
print(krediler)

krediler.pop()#default son elemanı siler
print(krediler)
krediler.pop(0)
print(krediler)

krediler.remove("Taşıt Kredisi")#index sırasına göre verilen ilk öğeyi siler
print(krediler)

krediler.extend(["X Kredisi", "Y Kredisi", "Z Kredisi"])#birden fazla öğe ekleme
print(krediler)

#for

for i in range(10): #0-9
    print("x")
    print(i)

print("**************")

for i in range(5,10):
    print(i)

print("**************")

for i in range(0,51,10):
    print(i)

print("**************")


for kredi in krediler:
    print(kredi)

print("**************")

for i in range(len(krediler)):
    print(krediler[i])

print("**************")

#while
i = 0
while i < 10 :
    print("X")
    i += 1

print("**************")

while True:
    print("X")
    break

print("**************")

i = 0
while i < len(krediler):
    print(krediler[i])
    i += 1

#fonksiyonlar
fiyat = 100
indirim = 20

def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat - indirim)

calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)

def sayHello(name):
    print(f"Merhaba {name}")

sayHello("Emrah")
sayHello("Yücel")

def calculateAndReturn(fiyat,indirim):
    return fiyat - indirim

yeniFiyat = calculateAndReturn(200,100)
print(yeniFiyat)

