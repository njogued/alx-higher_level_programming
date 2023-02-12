#starting selenium
#done in sublime on Windows 10
#Run on sublime using Ctrl + B
#uses chrome browser
import sys
sys.path.append("c:\python310\lib\site-packages")
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Deprecated Warning: still works though
# driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com")

print(driver.title)
# driver title is the page title
# page_source can be used to access the entire page (INSPECTED)

search_button = driver.find_element("name", "q")
# Note: find_element_by_name was removed in updates selenium
# hierarchy is id -> name -> class
# id is the most unique and class is least unique
search_button.clear()
#clear the google search bar
search_button.send_keys("debugging duck")
# search.send_keys(Keys.RETURN) works similar to submit
# submit == ENTER
search_button.submit()
try:
	link1 = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.TAG_NAME, "h3"))
		)
	# only finds the first TAG with heading 3
	# wait until the element specified is located
	link1.click()
	#print(driver.find_element("id", "main").text)
	#wiki = driver.find_element(By.TAG_NAME, "h3")
	#wiki.click()
	driver.back()
	driver.back()
	driver.forward()
	link2 = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.TAG_NAME, "h3"))
		)
	link2.click()
	# will find the link found again
	print(driver.title)
	time.sleep(10)

finally:
	driver.quit()
# print(result.text)
# Check documentation for explicit wait in python

# time.sleep(10)
