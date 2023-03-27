from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Test_Sauce:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://saucedemo.com/")
        
    def test_invalid_login(self):
        #user-name id li elementin görünmesini en fazla 5 sn bekle
        WebDriverWait(self.driver, 5).until(ec.visibility_of_all_elements_located((By.ID, "user-name")))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        WebDriverWait(self.driver, 5).until(ec.visibility_of_all_elements_located((By.ID, "password")))
        passwordInput = self.driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(2)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")

    def test_valid_login(self):
        self.driver.get("https://saucedemo.com/")
        WebDriverWait(self.driver, 5).until(ec.visibility_of_all_elements_located((By.ID, "user-name")))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        WebDriverWait(self.driver, 5).until(ec.visibility_of_all_elements_located((By.ID, "password")))
        passwordInput = self.driver.find_element(By.ID,"password")
        
        #Action Chains
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput, "standard_user")
        actions.send_keys_to_element(passwordInput, "secret_sauce")
        actions.perform()
        
        
        # userNameInput.send_keys("standard_user")
        # passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(10)

        
        
        
testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()