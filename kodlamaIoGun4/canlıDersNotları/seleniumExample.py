from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com")
input = driver.find_element(By.NAME,"q") #find_element geriye ilk bulduğu elementi döner
input.send_keys("kodlamaio")
searchButton = driver.find_element(By.NAME, "btnK")
sleep(2)
searchButton.click()
sleep(2)

#full xpath
# firstResult = driver.find_element(By.XPATH," /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a")
#xpath
secondResult = driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/a")
# firstResult.click()
secondResult.click()

listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")#find_elements geriye liste döner
print(f"Kodlamaio sitesinde şu anda {len(listOfCourses)} adet kurs var.")



# sleep(20)
while True:
    continue
# html locators