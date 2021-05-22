from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.haveibeenemotet.com/")

search = driver.find_element_by_name("email-input")



thislist = ["academiadepolitie.ro","sri.ro","pmb.ro"]



search.send_keys(thislist[0])
search.send_keys(Keys.RETURN)
time.sleep(3)

driver.get("https://www.haveibeenemotet.com")
search = driver.find_element_by_name("email-input")


search.send_keys(thislist[1])
search.send_keys(Keys.RETURN)
time.sleep(3)

driver.get("https://www.haveibeenemotet.com")
search = driver.find_element_by_name("email-input")


search.send_keys(thislist[2])
search.send_keys(Keys.RETURN)
time.sleep(2)
