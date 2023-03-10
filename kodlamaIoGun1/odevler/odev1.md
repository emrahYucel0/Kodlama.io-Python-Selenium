**Konu1 = Python veri tiplerini araştırıp kendi cümleleriniz ile yazınınız.**

# VERİ TİPLERİ

Python'daki standart veri türleri şunlardır:

## Numbers(Sayılar)
Sayısal değerleri saklamaktadır. Bu türlere bir değer atandığında sayı nesneleri oluşturulur.
Python dört farklı sayısal türü desteklemektedir. Bunlar:
- integer(tam sayılar)
- long(uzun tam sayılar)
- float(ondalıklı sayılar)
- complex(karmaşık sayılar)

```python

x = 100
y = 3.14
z = 2 + 3j

```

## String(Metin Dizisi)
Tek veya çift tırnak içerisinde metinsel ifadeleri saklamak için kullanılır.

```python

message = "Merhaba Kodlama.io"
idNumber = "11111111111"

```

## List(Liste)
Sıralı ve değiştirilebilir bir veri tipidir. Eşsiz olmayan öğelere sahip olabilir ve farklı 
veri tiplerini bir arada tutabilir.
Virgülle ayrılmış öğeler parantez [] içinde yazılıp tanımlanır.

```python

myList = [7, 10.0, "Python Öğrenmek Eğlenceli"]

```
## Tuple(Demet)
Liste ile benzer bir şekilde sıralı ve farklı veri tiplerini bir arada tutabilen veri tipleridir.
Listeden farkı oluşturulduktan sonra değiştirilemez olmalarıdır.
Virgülle ayrılmış öğeler parantez () içinde yazılıp tanımlanır.

```python

myTuple = (3, "Drogon", "Rhaegal", "Viserion")

```

## Set(Küme)
Eşsiz öğeleri depolamak için kullanılan bir veri tipidir. Öğeler değistirilebilir ve sırasızdır.
Virgülle ayrılmış öğeler parantez {} içinde yazılıp tanımlanır.

```python

mySet = {"İstanbul", "Ankara", "İzmir"}

```

## Dictionary(Sözlük)
Anahtar : değer çiftlerinin sırasız bir koleksiyonudur. Liste ve Tuple gibi farklı veri tiplerinin
bir araya gelerek oluşturduğu veri tipidir.
Her öğe anahtar : değer biçiminde bir çift olacak şekilde süslü parantezler {} içinde
tanımlanır.

```python

myDict = {"Fibonacci" : 1.618, "Pi" : 3.14, "Euler" : 0.5772}

```

## Booleans(Mantıksal Değerler)
True ve False doğruluk değerlerini temsil eder. Genellikle koşullu ifadelerde ve döngülerde kullanılırlar.

```python

myFalse = True

```

---

**KONU2 = Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.**

*Profil düzenle ve kart bilgileri sekmeleri altında bulunan*;

```python

fullName = "XXX XXX" #string tipinde değişken

cardNumber = 1234 #numbers tipinde değişken

postCode = 9876 #number tipinde değişken

city = "XXX" #string tipi değişken

dict = {"Kategori" : "Programlama", "Eğitmen":"Tümü"} #dictionary tipi değişken

programingList = ["Java", "Angular", "JavaScript", "Python", "React"] #list tipi değişken

isLogged = True #boolean tipi değişken

```
---

**KONU3 = Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz**

*Kullanıcı girişi yapılan bölüm*;

```python

username = "kodlama_io"
password = "123456"

if username == "kodlama_io" and password == "123456":
    print("Giriş başarılı.")
else:
    print("Kullanıcı adı veya şifre yanlış.")

```
*Kariyer Sekmesindeki doldurulması zorunlu bölümler*;

```python

username = input("Adınız Soyadınız: ")

if username: # eğer username doğru (None, '', [], 0 gibi değil) ise
    print("Hello, " + username + "!")
else: # eğer username yanlış (None, '', [], 0 gibi) ise
    print("Bu, yanıtlaması zorunlu bir sorudur")

```






