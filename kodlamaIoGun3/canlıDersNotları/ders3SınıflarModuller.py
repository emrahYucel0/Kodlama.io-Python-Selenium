#class

class Human:
    def talk(self,sentence):
        print(f"Human : {sentence}")
    def walk(self):
        print("Human is walking")

human1 = Human()
human1.talk("Merhaba")
human1.walk()

print("*****************")

class Human2:
    name = "Emrah" # fonksiyon içinde self ile ulaşırız default value
    def talk(self,sentence):
        name = "Yücel"
        print(f"{self.name}: {sentence}")
        print(f"{name} : {sentence}")
    def walk(self):
        print("Human is walking")

#instence-örnek
human2 = Human2()
human2.name = "Murat" # fonksiyon dışındaki name i değiştirir
human2.talk("Merhaba")
human2.walk()

print("***********************")

class Human3:
    #built in
    #constructor
    #initialize
    def __init__(self,name) -> None:
        self.name = name
        print("Yapıcı blok çalıştın Human instence üretildi") 

    def __str__(self) -> str:
        return f"STR Fonksiyonundan dönen değer: {self.name}"
    
    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
        print(f"{self.name} : {sentence}")
    def walk(self):
        print(f"{self.name} is walking")

#instence-örnek
human3 = Human3("Yiğit") 
human3.talk("Merhaba")
human3.walk()
print(human3)# str fonksiyonunu eklemeseydik ram adresini çıktı olarak alacaktık.


