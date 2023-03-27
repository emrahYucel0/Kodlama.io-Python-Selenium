# PyTest Dekoratörleri

PyTest, test kodlarını yazmak ve yönetmek için popüler bir Python test çerçevesidir. PyTest, kodu test etmek ve hata ayıklamak için birçok özellik sunar. 

---

### @pytest.mark.dependency

 Bu dekoratör, testler arasındaki bağımlılıkları belirlemek için kullanılır. Bu şekilde, bir testin öncesinde veya sonrasında belirli bir testin çalıştırılması sağlanabilir.

 ```python

 import pytest

@pytest.mark.dependency()
def test_login():
    # Login işlemleri

@pytest.mark.dependency(depends=["test_login"])
def test_logout():
    # Logout işlemleri

```

Bu testte, "test_logout" fonksiyonu "test_login" fonksiyonundan önce çalıştırılacaktır. "test_logout" fonksiyonu, "test_login" fonksiyonunun çıktısına ihtiyaç duyduğu için, "depends" argümanı kullanılarak bağımlılık belirtilir

---

### @pytest.mark.timeout

Bu dekoratör, belirli bir testin belirli bir süre içinde tamamlanması gerektiğini belirler. Eğer test belirlenen süre içinde tamamlanmazsa, test otomatik olarak başarısız olur.

```python

import pytest
import time

@pytest.mark.timeout(2)
def test_slow_function():
    time.sleep(3) # Bu fonksiyon 3 saniye uyur

```

Bu testin 2 saniyeden kısa bir sürede tamamlanması gerekir. Ancak, test 3 saniyeden daha uzun sürerse, Pytest, bir hata verir ve test başarısız olur.

---

### @pytest.mark.slow

Bu dekoratör, belirli bir testin uzun süre çalışacağı veya yavaş çalışacağı durumlarda kullanılır. Bu şekilde, test süresinin uzunluğuna dikkat çekilerek, test senaryosunun optimize edilmesi sağlanabilir.

```python

import pytest
import time

@pytest.mark.slow
def test_slow_function():
    time.sleep(3) # Bu fonksiyon 3 saniye uyur

```

Bu test normalden daha yavaş çalıştığı için, Pytest bu test için bir uyarı mesajı verir.

---

### @pytest.fixture

Bu dekoratör, bir test fonksiyonuna veya bir test sınıfına veri veya nesneler sağlar. Fixture, test senaryolarının gerçek dünya senaryolarını simüle etmek için kullanılabilir. Örneğin, bir veritabanı bağlantısı oluşturmak, bir dosya yolu almak veya bir test nesnesi oluşturmak için kullanılabilir. Fixture'lar, testlerin daha modüler ve okunaklı hale gelmesini sağlar.

```python

import pytest

@pytest.fixture
def user():
    return {'name': 'Emrah', 'age': 30}

def test_user_name(user):
    assert user['name'] == 'Emrah'
    
def test_user_age(user):
    assert user['age'] == 30

```

Yukarıdaki örnekte "@pytest.fixture dekoratörü", "user" adında bir fixture oluşturmak için kullanılır. "user" fixture'ı, test fonksiyonlarına bir Python sözlüğü sağlar. test_user_name fonksiyonu, fixture'ın name anahtarının "Emrah" olduğunu doğrular. Benzer şekilde, test_user_age fonksiyonu, fixture'ın age anahtarının 30 olduğunu doğrular.

---

### @pytest.mark.parametrize

Bu dekoratör, aynı test senaryosunu farklı parametrelerle çalıştırmak için kullanılır. Bu, testlerinizi daha modüler hale getirir ve farklı durumları test etmek için kod tekrarını önler. Parametreler, değişken sayıda argümanlarla birlikte kullanılabilir. PyTest, her parametre kombinasyonu için ayrı bir test çalıştırır.

```python

import pytest

def add(x, y):
    return x + y

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (4, 5, 9),
    (10, 20, 30)
])
def test_add(x, y, expected):
    assert add(x, y) == expected

```

Yukarıdaki örnekte "@pytest.mark.parametrize" dekoratörü, "test_add" fonksiyonunu farklı girdi parametreleriyle test etmek için kullanılır. "test_add" fonksiyonu, x, y ve expected argümanlarını alır ve bu argümanların farklı kombinasyonları için ayrı ayrı çalışır. PyTest, her kombinasyon için ayrı bir test olarak çalıştırır. Yukarıdaki örnekte, test_add fonksiyonu, üç farklı parametre kombinasyonu için test edilir.

---

### @pytest.mark.skip

Bu dekoratör, belirli bir testin atlanmasına veya çalıştırılmamasına olanak tanır. Bu genellikle, belirli bir test senaryosunun henüz hazır olmadığı veya hatalı olduğu durumlarda kullanılır.

```python

import pytest

@pytest.mark.skip(reason="temporary test")
def test_something():
    assert False

```

Yukarıdaki örnekte "@pytest.mark.skip" dekoratörü, "test_something" fonksiyonunun geçici olarak atlanması gerektiğini belirtir. Bu test, geçici olarak atlanır ve PyTest sonuçlarında gösterilmez.

---

### @pytest.mark.xfail

Bu dekoratör, belirli bir testin bilerek başarısız olacağı veya hata vereceği durumlarda kullanılır. Bu şekilde, testin beklenen bir hatayla sonuçlanacağı veya henüz geliştirilmemiş bir özelliğin test edildiği durumlarda kullanılabilir.

```python

import pytest

def divide(a, b):
    return a / b

@pytest.mark.xfail(raises=ZeroDivisionError)
def test_divide_by_zero():
    divide(1, 0)

```

Yukarıdaki örnekte "@pytest.mark.xfail" dekoratörü, "test_divide_by_zero" fonksiyonunun bir sıfıra bölme hatası oluşturacağını ve bu hatanın bilinçli olarak kabul edildiğini belirtir. PyTest, bu testin başarısız olacağını bildirir, ancak bu sonucun beklenildiğini de belirtir.





