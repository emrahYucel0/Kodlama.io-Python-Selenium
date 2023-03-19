import matematik as m
from ders3SınıflarModuller import Human3

from selenium import webdriver

# from matematik import topla as toplamaIslemi
#print(toplamaIslemı(10,20))

#built-in modules
import random

print(m.topla(10,20))

human = Human3("Emrah")
human.talk("Selam")

print(random.randint(0,100))

chromeDriver = webdriver.Chrome()