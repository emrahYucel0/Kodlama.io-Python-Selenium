from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pytest
from pathlib import Path
from datetime import date

class Test_Demo:
    #her testten önce çağrılır
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://saucedemo.com/")
        
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

        
    
    #her testten sonra çağrılır
    def teardown_method(self):
        self.driver.quit()

    def test_demoFunc(self):
        # 3A Act Arange Assert
        text = "Hello"
        assert text == "Hello"

    def test_demo2(self):
        assert True

    # Pytest Decorators

    # @pytest.mark.skip()
    @pytest.mark.parametrize("username,password",[("1","1"),("2","2")])
    def test_invalid_login(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        sleep(2)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"

    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))