students = ["Emrah Yücel", "Murat Yücel", "Ayşegül Yücel", "Sibel Yücel", "Yiğit Yücel"]
# 1 -) listeye öğrenci ekleme fonksiyonu
def addStudent():
    name = input("Eklemek istediğiniz öğrencinin adı: ")
    surname = input("Eklemek istediğiniz öğrencinin soyadı: ")
    student = name + " " + surname
    students.append(student)
    print(f"{student} eklendi.")
    

# 2 -) listeden öğrenci kaldırma fonksiyonu
def removeStudent():
    name = input("Silmek istediğiniz öğrencinin adı: ")
    surname = input("Silmek istediğiniz öğrencinin soyadı: ")
    student = name + " " + surname
    if student in students:
        students.remove(student)
        print(f"{student} silindi")
    else:
        print(f"{student} bulunamadı.")

# 3 -) listeye birden fazla öğrenci  ekleme
def addStudents():
    numberOfStudents = int(input("Kaç öğrenci ekleyeceksiniz? "))
    newStudents = []
    for i in range(numberOfStudents):
        name = input(f"{i+1}. öğrencinin adını girin: ")
        surname = input(f"{i+1}. öğrencinin soyadını girin: ")
        newStudents.append(f"{name} {surname}")
    students.extend(newStudents)
    print(f"{numberOfStudents} öğrenci listeye eklendi.")

# 4-) listedeki öğrencileri tek tek yazdırma
def listOfStudents():
    for student in students:
        print(student)

# 5-) index no = öğrenci no olacak şekilde görüntüleme
def studentNumber():
    name = input("Öğrencinin adı: ")
    surname = input("Öğrencinin soyadı: ")
    student = name + " " + surname
    if student in students:
        number = students.index(student)
        print(f"{student} öğrencisinin numarası: {number}")
    else:
        print("Listede böyle bir öğrenci yok.")

# 6-) listeden döngü kullanarak birden fazla öğrenci silme
def removeStudents():
    while True:
        name = input("SİLMEK İSTEDİĞİNİZ ÖĞRENCİ ADI (!!!Menüye dönmek için 'q' tuşuna basın!!!): ")
        surname = input("siLMEK İSTEDİĞİNİZ ÖĞRENCİ SOYADI: ")
        student = name + " " + surname
        if name == 'q':
            break
        count = students.count(student)
        if count == 0:
            print("Listede böyle bir öğrenci yok.")
        else:
            for i in range(count):
                students.remove(student)
            print(f"{count} öğrenci silindi.")
            

#öğrenci kayıt sistemi için menü oluşturma
def mainMenu():
    print("***************")
    print("Öğrenci Kayıt - Görüntüleme Sistemi\n")
    print("1. Öğrenci ekle")
    print("2. Öğrenci sil")
    print("3. Çoklu örenci ekle")
    print("4. Öğrenci listesi")
    print("5. Öğrenci numarası")
    print("6. Çoklu öğenci sil")
    print("7. Çıkış yap")

while True:
    mainMenu()
    choice = input("\nHoşgeldiniz\n******\nİşlem Numaranızı Giriniz: ")
    if choice == "1":
        addStudent()
    elif choice == "2":
        removeStudent()
    elif choice == "3":
        addStudents()
    elif choice == "4":
        listOfStudents()
    elif choice == "5":
        studentNumber()
    elif choice == "6":
        removeStudents()
    elif choice == "7":
        print("Çıkış Yapılıyor...")
        break
    else:
        print("Geçersiz seçim. Tekrar deneyin.")



   
