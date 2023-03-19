***Konu1 = HTML hakkında bilgi veriniz***

---

# HTML NEDİR ?

HTML (HyperText Markup Language), web sayfalarının yapısını tanımlayan bir işaretleme dilidir. Web sayfaları, HTML etiketleri yardımıyla yapılandırılır ve bu etiketler sayfa içeriğinin anlamını belirler. Web Arayüz Programlama’nın ilk ayağı olarak adlandırılabilecek HTML için Web’in iskeleti diyebiliriz. Bütün web sayfalarında kullanılan bir standarttır.
HTML bir programlama dili değildir. Adında da belirtildiği şekilde işaretleme (markup) dilidir. Sunulmak istenen veri etiketler yardımıyla işaretlenir.
HTML için çeşitli etiketler vardır. Etiketler yardımıyla HTML içeriği anlamlandırılır. Örneğin başlık yapılmak istenen metin, başlık etiketiyle işaretlenir.
Sadece HTML ile web sayfaları hazırlamak mümkündür. Bu web sayfaları Statik Web Sayfaları olarak adlandırılır.

```html

<!DOCTYPE html>
<html lang="tr">
    <head>
        <title>İlk Sayfa</title>
</head>
<body>
    <div>
        <p>Merhaba Dünya!</p>
    </div>
</body>
</html>

```


"!DOCTYPE html" komutu bu dosyanın HTML5 formatında olduğunu ve içeriklerin bu formata uygun hazırlandığını tarayıcıya bildiren komuttur ve etiket olmadığı için kapatılmasına gerek yoktur. Sonraki satırda gelen "html" etiketleri arasına HTML kodu yazılarak sayfa oluşturulur. Bu etiketin içerisindeki lang="tr" ise tarayıcıya bu sayfanın Türkçe dilinde olduğunu söylemektedir. HTML dosyaları iki ana kısımdan oluşur. Bunlar dosyanın içeriği, yazarı gibi genel bilgilerin olduğu "head" ve ekranda gösterilen tüm ögelerin bulunduğu "body" kısımlarıdır.

# HTML ETİKETLERİ

## Başlık Etiketleri

HTML sayfalarda bulunan metinlerin başlıklarını belirtmek için “Başlık Etiketleri” olarak adlandırılan özel tanımlamalar vardır. "h1", "h2", "h3", "h4", "h5", "h6" sırasıyla en büyük başlıktan en küçük başlığa doğru gitmektedir.

## Paragraf Etiketi

Paragrafları etiketlemek için "p" etiketi kullanılır.Tarayıcılar paragraf etiketlerinin öncesine ve sonrasına boşluk koyarak paragrafları ayırırlar.

## Biçimlendirme Etiketleri

1. "b" : Metin içerinde kalın göstermek istediğimiz kısım bu blok içine yazılır.
2. "strong" : SEO algoritmasına metin içindeki anahtar kelimeleri verir.
3. "i" : Sağa italik yazmak için kullanılır.
4. "em" : Metin seslendirme algoritmalarında içindeki kelime bloğunun farklı ses tonuyla okunmasını sağlar.
5. "del" : Etiketi ile işaretlenen kelimenin üzeri çizilir.
6. "mark" : Metin arka planını sarı vurgular.
7. "u" : Kelimenin altı çizilir
8. "small" : Yazının diğer bölümlerine göre daha ufak yazdırır.
9. "abbr title=" : Kısaltılan kelimenin uzun hali title içine yazılır.
10. "q" : Kısa alıntılar diye adlandırılan cümlelerde kullanılabilir
11. "blockquote" : Uzun alıntılarda kullanılır.

## Resim Etiketi

Web sayfalarında resim göstermek için kullanılan <img> etiketi kapanış etiketi gerektirmeyen, resim yolunu içerisindeki alt özellikler yoluyla alan bir etikettir.

```html

<h1>Resim Örneği</h1>
<img src="img_girl.jpg" alt="Girl in a jacket" width="500" height="600">

```

"src" özelliği ile resmin yolu ve adresi belirtilmiştir. Resim dosya ile aynı klasörde ise sadece resim adı yeterlidir. "alt" özelliği ile resim hakkında kısa bir açıklama yapılmıştır. "width" ve "height" özellikleri ile resmin boyutlandırması yapılmıştır.

## Linkler

Dosyalar arasında geçiş yapmak için "a" etiketini kullanabiliriz. Bu etiketin içerisindeki "href" özelliği ile gidilecek sayfanın konumu belirtilir. Bu etiketin aldığı başka bir özellik olan "target" ile sayfanın açılacağı konumu belirleyenebilir. Sayfayı aynı sekmede açmak için target="_self", farklı sekmede açmak için target="_blank" kullanabilir.

## Listeler

Eklenen elemanları sıralı ve sırasız gösterebileceğiniz iki tür etiket vardır. "ol" etiketi içerisindeki "li" elemanlarını rakamla sıralayarak gösterir."ul" ile "li" elemanlarını sıralarken rakam yerine başında nokta ile işaretleyerek gösterir. Bu iki liste türünün haricinde açıklama amaçlı kullanılan "dl" etiketi de vardır. Alt eleman olarak "dt" ve "dd" elemanlarını alır.

## Görüntü Seviyeleri

Temelde 2 tane görüntü seviyesi vardır. Etiket tüm satırı kaplıyorsa block ve sadece içeriği kadar alan kaplıyorsa inline olarak adlandırılır. "div" etiketi genel olarak sayfayı bölümlemek için kullanılır. Bu etiketin genişliği tüm sayfayı kaplayan %100 boyutundadır. İçerisine aldığı nesnenin genişliğinden bağımsız olarak tüm satırı kapladığı için block elemadır. "span" ise sadece içerdiği eleman kadar alan kaplar. Block elemanlardan sonra gelen her eleman bir alt satırdan başlar.

---


***Konu2 = HTML locators hakkında bilgi veriniz***


---

HTML sayfalarında, sayfadaki öğeleri belirlemek ve onlarla etkileşimde bulunmak için "HTML locators" adı verilen çeşitli yöntemler kullanılır. Bu yöntemler aşağıdaki gibidir:

1. ID: HTML öğelerine eşsiz bir tanımlayıcı veren "id" özelliği, öğeleri belirlemenin en kolay yolu olarak kabul edilir.
2. Name: HTML öğelerine isim vermek için "name" özelliği kullanılır. Bu özellik, özellikle form öğeleri için yararlıdır.
3. Class: "class" özelliği, HTML öğelerine bir veya daha fazla sınıf adı atamanızı sağlar.
4. Tag Name: HTML öğelerine "tag name" ile referans verilebilir.
5. Link Text: Bu yöntem, bir bağlantıyı metin içeriğiyle belirler.
6. Partial Link Text: Bu yöntem, bağlantı metninin bir kısmını kullanarak bağlantıyı belirler. 
7. CSS Selector: CSS seçicileri, HTML öğelerinin belirli özelliklerine göre seçilmesini sağlar.
8. XPath: XPath, XML tabanlı belgelerdeki öğeleri belirlemek için kullanılan bir dil ve HTML sayfalarında da kullanılabilir.

---


***Konu3 = Selenium'da aksiyonlar hakkında bilgi veriniz.***


---

Selenium'da kullanılan bazı yaygın aksiyonlar şunlardır:

1. get(url): Belirtilen URL'ye gitmek için kullanılır.
2. find_element(): Belirtilen özelliklere göre bir elementi (bir metin kutusu, bir buton, bir bağlantı vb.) bulmak için kullanılır.
3. send_keys(keys) : Bir elemente metin girmek için kullanılır.
4. click() : Bir elementi tıklamak için kullanılır.
5. clear() : Bir metin kutusundaki mevcut metni silmek için kullanılır.
6. submit() : Bir formu göndermek için kullanılır.
7. back() : Önceki sayfaya dönmek için kullanılır.
8. forward() : İleri sayfaya gitmek için kullanılır.
9. refresh() : Sayfayı yenilemek için kullanılır.
10. execute_script(script) : Belirtilen JavaScript kodunu çalıştırmak için kullanılır.

---


