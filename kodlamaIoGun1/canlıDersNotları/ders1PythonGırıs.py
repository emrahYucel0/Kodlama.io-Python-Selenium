print("Kodlamaio")
baslik = "Taşıt Kredisi"
print(baslik)

#sting => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)

#int, integer => sayısal ifade
vade = 36
ekVade = 6
vade2 = "36"

#float, decimal, double
aylikOdeme = 200.50

#bool, boolean => True veya False
yukselisteMi = False

#matematiksel operatörler
print(2000 + 3000)
print(vade + 10)
print(vade + ekVade)
yeniVade = vade / 2 
fiyat = 100
indirimliFiyat = fiyat - 20
print(yeniVade)
print(indirimliFiyat)

# mantıksal operatörler
a = 1
b = 1
c = 2
d = "3"
e = 3
print(d == e)
print(a == b)
print(a == c)
print(a > b)
print(a < c)
print(a <= b)
print(a != b)
print(a != b)

#or and
print(a < b or a < c)
print(a < b and a < c)
print(a < b or a < c and c > a)

#karar yapıları 
#if else
sayi1 = 100
sayi2 = 500
if sayi1 > sayi2:
    print("sayi1 sayi2 den büyüktür!")
elif sayi1 < sayi2:
    print("sayi1 sayi2 den küçüktür!")
else:
    print("sayılar eşittir!")