from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
import pytest
from pathlib import Path
from datetime import date

class Test_Demo:
    #her testten önce çağrılır
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://saucedemo.com/")
        
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    #her testten sonra çağrılır
    def teardown_method(self):
        self.driver.quit()

    def login_method(self, username, password):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        loginButton = self.driver.find_element(By.ID,"login-button")

        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        sleep(2)
        loginButton.click()

    def test_emptyUsernamePassword(self):
        self.login_method("", "")

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(self.folderPath+"/test-emptyusernamePassword.png")
        assert errorMessage.text == "Epic sadface: Username is required"
    
    def test_emptyPassword(self):
        self.login_method("user", "")

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(self.folderPath+"/test-emptyPassword.png")
        assert errorMessage.text == "Epic sadface: Password is required"

    def test_lockedUser(self):
        self.login_method("locked_out_user", "secret_sauce")

        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(self.folderPath+"/test-lockedUser.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    def test_closedIcon(self):
        self.login_method("", "")

        closeButton = self.driver.find_element(By.CLASS_NAME, "error-button")
        closeButton.click()
        
        closeIcon = self.driver.find_elements(By.CLASS_NAME,"error_icon")
        self.driver.save_screenshot(self.folderPath+"/test-closedIcon.png")
        assert len(closeIcon) == 0

    def test_inventoryPage(self):
        self.login_method("standard_user", "secret_sauce")

        errorMessage = self.driver.current_url
        self.driver.save_screenshot(self.folderPath+"/test-invonteryPage.png")
        assert errorMessage == "https://www.saucedemo.com/inventory.html"
        
    def test_inventoryItem(self):
        self.login_method("standard_user", "secret_sauce")
        listOfInventories = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        self.driver.save_screenshot(self.folderPath+"/test-invonteryItem.png")
        assert len(listOfInventories) == 6

    #Bu test fonksiyonu, sayfadan çıkış seneryosunu simüle eder
    def test_exitPage(self):
        self.login_method("standard_user", "secret_sauce")
        burgerMenuButton = self.driver.find_element(By.ID, "react-burger-menu-btn")
        burgerMenuButton.click()
        sleep(2)
        logoutButon = self.driver.find_element(By.ID, "logout_sidebar_link")
        logoutButon.click()
        
        errorMessage = self.driver.current_url
        self.driver.save_screenshot(self.folderPath+"/test-exitPage.png")
        assert errorMessage == "https://www.saucedemo.com/"

    #Bu test fonksiyonu, alışveriş sepetinden ürünlerin bulunduğu sayfaya geçişi simüle eder
    def test_backInventoryPage(self):
        self.login_method("standard_user", "secret_sauce")
        shoppingCart = self.driver.find_element(By.ID, "shopping_cart_container")
        shoppingCart.click()
        continueButton = self.driver.find_element(By.ID, "continue-shopping")
        continueButton.click()
        sleep(5)
        
        errorMessage = self.driver.current_url
        self.driver.save_screenshot(self.folderPath+"/test-backInventoryPage.png")
        assert errorMessage == "https://www.saucedemo.com/inventory.html"

    #Bu test fonksiyonu, bir web sayfasında bir ürün satın almayı simüle eder
    @pytest.mark.parametrize("firstname,lastname,postalcode",[("Emrah","Yücel","60"),("Murat","Yücel","58"),("Ayşegül","Yücel","34")])
    def test_buyProduct(self,firstname,lastname,postalcode):
        self.login_method("standard_user", "secret_sauce")
        addChartButton = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        addChartButton.click()
        
        shoppingCart = self.driver.find_element(By.ID, "shopping_cart_container")
        shoppingCart.click()
    
        checkout_button = self.driver.find_element(By.CLASS_NAME,"checkout_button")
        checkout_button.click()
        

        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        postalCodeInput = self.driver.find_element(By.ID, "postal-code")
        firstNameInput.send_keys(firstname)
        lastNameInput.send_keys(lastname)
        postalCodeInput.send_keys(postalcode)
        
        continueButton = self.driver.find_element(By.ID,"continue")
        continueButton.click()
        
        finishButton = self.driver.find_element(By.ID,"finish")
        finishButton.click()

        message = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div")
        self.driver.save_screenshot(self.folderPath+"/test-buyProduct.png")
        assert message.text == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"

    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

