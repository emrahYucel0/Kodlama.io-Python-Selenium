from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Test_Kodlamaio:
    def test_invalid_login(self):#doğru giriş yaılmama durumu testi
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://www.kodlama.io/")
        loginBtn = driver.find_element(By.XPATH,"/html/body/header/div/div/div/div/ul/li[3]/a")
        loginBtn.click()
testClass = Test_Kodlamaio()
testClass.test_invalid_login()
