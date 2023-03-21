from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

class Test_Sauce:
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        sleep(5)
        #user-name id li elementin görünmesini en fazla 5 sn bekle
        userNameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(2)
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")
        
        
testClass = Test_Sauce()
testClass.test_invalid_login()