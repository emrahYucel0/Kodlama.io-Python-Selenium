from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

from pathlib import Path
from datetime import date

from constant import globalButtonConstants
from constant import globalLoginConstants
from constant import globalMessageConstants
from constant import globalUrlConstants

class Test_Demo:
    #her testten önce çağrılır
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(globalUrlConstants.URL_MAIN)
        
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    #her testten sonra çağrılır
    def teardown_method(self):
        self.driver.quit()
    
    # kullanıcı girişleri için ortak fonksiyon
    def login_method(self, username, password):
        self.waitForElementVisible((By.ID,globalLoginConstants.USERNAME_ID))
        userNameInput = self.driver.find_element(By.ID, globalLoginConstants.USERNAME_ID)
        self.waitForElementVisible((By.ID,globalLoginConstants.PASSWORD_ID))
        passwordInput = self.driver.find_element(By.ID, globalLoginConstants.PASSWORD_ID)
        loginButton = self.driver.find_element(By.ID,globalButtonConstants.BTN_LOGIN_ID)

        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        sleep(2)
        loginButton.click()
        
    #ödeme sayfasına giriş için ortak fonksiyon
    def login_payment_method(self,firstname,lastname,postalcode):
        firstNameInput = self.driver.find_element(By.ID,globalLoginConstants.FIRSTNAME_ID)
        lastNameInput = self.driver.find_element(By.ID,globalLoginConstants.LASTNAME_ID)
        postalCodeInput = self.driver.find_element(By.ID,globalLoginConstants.POSTALCODE_ID)
        continueButton = self.driver.find_element(By.ID, globalButtonConstants.BTN_CONTINUE_ID)

        firstNameInput.send_keys(firstname)
        lastNameInput.send_keys(lastname)
        postalCodeInput.send_keys(postalcode)
        
        continueButton.click()
        

    #Test 1 : Sepetten geri ürün sayfasına geçiş testi
    def test_backInventoryPage(self):
        self.login_method("standard_user", "secret_sauce")

        shoppingCart = self.driver.find_element(By.ID, globalButtonConstants.BTN_CART_ID)
        shoppingCart.click()
        continueShoppingButton = self.driver.find_element(By.ID, globalButtonConstants.BTN_CONTINUE_SHOPPING_ID)
        continueShoppingButton.click()
        sleep(5)
        
        errorMessage = self.driver.current_url
        self.driver.save_screenshot(self.folderPath+"/test-backInventoryPage.png")
        assert errorMessage == globalUrlConstants.URL_MAIN_INVENTORY

    #Test 2 : Ürün satın alma testi
    def test_buyProduct(self):
        self.login_method("standard_user", "secret_sauce")

        addChartButton = self.driver.find_element(By.ID, globalButtonConstants.ADD_BACKPACK_ID)
        addChartButton.click()
        
        shoppingCart = self.driver.find_element(By.ID, globalButtonConstants.BTN_CART_ID)
        shoppingCart.click()
    
        checkout_button = self.driver.find_element(By.ID, globalButtonConstants.BTN_CHECKOUT_ID)
        checkout_button.click()

        self.login_payment_method("Emrah","Yücel","34000")

        finishButton = self.driver.find_element(By.ID, globalButtonConstants.BTN_FINISH_ID)
        finishButton.click()

        message = self.driver.find_element(By.XPATH,globalMessageConstants.ORDER_DONE_XPATH)
        self.driver.save_screenshot(self.folderPath+"/test-buyProduct.png")
        assert message.text == globalMessageConstants.ORDER_DONE

    # Test 3 : İsim boş bırakıldığında gelen hata mesajını doğrulama testi
    def test_emptyFirstName(self):
        self.login_method("standard_user", "secret_sauce")

        shoppingCart = self.driver.find_element(By.ID, globalButtonConstants.BTN_CART_ID)
        shoppingCart.click()
    
        checkout_button = self.driver.find_element(By.ID, globalButtonConstants.BTN_CHECKOUT_ID)
        checkout_button.click()

        self.login_payment_method("","Yücel","34000")

        errorMessage = self.driver.find_element(By.CSS_SELECTOR,globalMessageConstants.ERROR_BOX_CSS)
        self.driver.save_screenshot(self.folderPath+"/test-emptyFirstName.png")
        assert errorMessage.text == globalMessageConstants.ERROR_FIRSTNAME

    # Test 4 : Soyisim boş bırakıldığında gelen hata mesajını doğrulama testi
    def test_emptyLastName(self):
        self.login_method("standard_user", "secret_sauce")

        shoppingCart = self.driver.find_element(By.ID, globalButtonConstants.BTN_CART_ID)
        shoppingCart.click()
    
        checkout_button = self.driver.find_element(By.ID, globalButtonConstants.BTN_CHECKOUT_ID)
        checkout_button.click()

        self.login_payment_method("Emrah","","34000")

        errorMessage = self.driver.find_element(By.CSS_SELECTOR,globalMessageConstants.ERROR_BOX_CSS)
        self.driver.save_screenshot(self.folderPath+"/test-emptyLastName.png")
        assert errorMessage.text == globalMessageConstants.ERROR_LASTNAME
    
    # Test 5 : Posta kodu boş bırakıldığında gelen hata mesajını doğrulama testi
    def test_emptyPostalCode(self):
        self.login_method("standard_user", "secret_sauce")

        shoppingCart = self.driver.find_element(By.ID, globalButtonConstants.BTN_CART_ID)
        shoppingCart.click()
    
        checkout_button = self.driver.find_element(By.ID, globalButtonConstants.BTN_CHECKOUT_ID)
        checkout_button.click()

        self.login_payment_method("Emrah","Yücel","")

        errorMessage = self.driver.find_element(By.CSS_SELECTOR,globalMessageConstants.ERROR_BOX_CSS)
        self.driver.save_screenshot(self.folderPath+"/test-emptyPostalCode.png")
        assert errorMessage.text == globalMessageConstants.ERROR_POSTALCODE

    # Test 6 : Twitter hesabına yönlendirme testi
    def test_twitterPage(self):
        self.login_method("standard_user", "secret_sauce")

        twitter_icon = self.driver.find_element(By.LINK_TEXT, globalButtonConstants.LINK_TWITTER)
        twitter_icon.click()
        
        self.driver.switch_to.window(self.driver.window_handles[1])

        errorMessage = self.driver.current_url
        self.driver.save_screenshot(self.folderPath+"/test-twitterPage.png")
        assert errorMessage == globalUrlConstants.URL_TWITTER

    # Test 7 : Facebook hesabına yönlendirme testi
    def test_facebookPage(self):
        self.login_method("standard_user", "secret_sauce")

        twitter_icon = self.driver.find_element(By.LINK_TEXT, globalButtonConstants.LINK_FACEBOOK)
        twitter_icon.click()
        
        self.driver.switch_to.window(self.driver.window_handles[1])

        errorMessage = self.driver.current_url
        self.driver.save_screenshot(self.folderPath+"/test-facebookPage.png")
        assert errorMessage == globalUrlConstants.URL_FACEBOOK

    # Test 8 : Tüm ürünlerin vergi dahil toplam fiyatlarını doğrulama testi
    def test_totalPrice(self):
        self.login_method("standard_user", "secret_sauce")

        addBackpack = self.driver.find_element(By.ID, globalButtonConstants.ADD_BACKPACK_ID)
        addBackpack.click()
        addLight = self.driver.find_element(By.ID, globalButtonConstants.ADD_LIGHT_ID)
        addLight.click()
        addJacket = self.driver.find_element(By.ID, globalButtonConstants.ADD_JACKET_ID)
        addJacket.click()
        addTshirt = self.driver.find_element(By.ID, globalButtonConstants.ADD_TSHIRT_ID)
        addTshirt.click()
        addTshirtRed = self.driver.find_element(By.ID, globalButtonConstants.ADD_TSHIRT_RED_ID)
        addTshirtRed.click()
        addOnesie = self.driver.find_element(By.ID, globalButtonConstants.ADD_ONESIE_ID)
        addOnesie.click()

        shoppingCart = self.driver.find_element(By.ID, globalButtonConstants.BTN_CART_ID)
        shoppingCart.click()
    
        checkout_button = self.driver.find_element(By.ID, globalButtonConstants.BTN_CHECKOUT_ID)
        checkout_button.click()

        self.login_payment_method("Emrah","Yücel","34000")

        message = self.driver.find_element(By.CSS_SELECTOR,globalMessageConstants.TOTAL_PRICE_CSS)
        self.driver.save_screenshot(self.folderPath+"/test-totalPrice.png")
        assert message.text == globalMessageConstants.TOTAL_PRICE_TEXT

    #Test 9 : Sayfadan çıkış testi
    def test_exitPage(self):
        self.login_method("standard_user", "secret_sauce")

        burgerMenuButton = self.driver.find_element(By.ID, globalButtonConstants.BTN_BURGERMENU_ID)
        burgerMenuButton.click()
        sleep(2)
        logoutButon = self.driver.find_element(By.ID, globalButtonConstants.BTN_LOGOUT_ID)
        logoutButon.click()
        
        errorMessage = self.driver.current_url
        self.driver.save_screenshot(self.folderPath+"/test-exitPage.png")
        assert errorMessage == globalUrlConstants.URL_MAIN

    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))



    