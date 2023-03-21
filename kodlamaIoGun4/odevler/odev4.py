from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#Aşağıda verilen test caselerin hepsini "https://www.saucedemo.com/" sitesinde gerçekleştirmeniz istenmektedir.

class LoginTest():
    #sayfanın ilk açılışı ve boyutunu init fonksiyonun içinde tuttum
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://saucedemo.com/")

    #Tüm fonksiyonlarda ortak kullanıcı adı,şifre ve giriş butonu elementlerini için ayrı bir fonksiyon oluşturdum.
    def login(self, username, password):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        loginButton = self.driver.find_element(By.ID,"login-button")

        sleep(1)
        usernameInput.clear() #fonksiyonları peş peşe çağırdığımızda çakışmanın önüne geçmek için kullandım
        sleep(0.5)
        usernameInput.send_keys(username)
        sleep(0.5)
        passwordInput.clear()
        sleep(0.5)
        passwordInput.send_keys(password)
        sleep(1)

        loginButton.click()   
        sleep(1)

    # # Test Case1 = Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
    def emptyUsernamePassword(self):
        self.login("", "")

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Password and Username Empty Test Result: {testResult}")

    # Test Case2 = Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.

    def emptyPassword(self):
        self.login("user", "")

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Password Empty Test Result: {testResult}")

    # Test Case3 = Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde 
    #"Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir

    def lockedUser(self):
        self.login("locked_out_user", "secret_sauce")

        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Locked Out User Test Result: {testResult}")

    # Test Case4 = Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. 
    # Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)

    def closedIcon(self):
        self.login("", "")

        closeButton = self.driver.find_element(By.CLASS_NAME, "error-button")
        closeButton.click()
        
        closeIcon = self.driver.find_elements(By.CLASS_NAME,"error_icon")
        testResult = len(closeIcon) == 0
        print(f"Icon Disspear Test Result: {testResult}")

    # Test Case5 = Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.

    def inventoryPage(self):
        self.login("standard_user", "secret_sauce")

        errorMessage = self.driver.current_url
        testResult = errorMessage == "https://www.saucedemo.com/inventory.html"
        print(f"Login Inventory Page Test Result: {testResult}")

    # Test Case6 = Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

    def inventoryItem(self):
        listOfInventories = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        testResult = len(listOfInventories) == 6
        print(f"Numbers Of Products Test Result: {testResult}")

    # Test Case Extra = Inventory sayfasından çıkış yapıp kullanıcı girişi sayfasına geçme durumu

    def exitPage(self):
        burgerMenuButton = self.driver.find_element(By.ID, "react-burger-menu-btn")
        burgerMenuButton.click()
        sleep(2)
        logoutButon = self.driver.find_element(By.ID, "logout_sidebar_link")
        logoutButon.click()
        
        errorMessage = self.driver.current_url
        testResult = errorMessage == "https://www.saucedemo.com/"
        print(f"Logout Test Result: {testResult}")


loginTest = LoginTest()
loginTest.emptyUsernamePassword()
loginTest.emptyPassword()
loginTest.lockedUser()
loginTest.closedIcon()
loginTest.inventoryPage()
loginTest.inventoryItem()
loginTest.exitPage()
