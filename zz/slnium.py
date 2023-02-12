#starting selenium
#done in sublime on windows
#Run on Windows using Ctrl + B
import sys
sys.path.append("c:\python310\lib\site-packages")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
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
search_button.send_keys("debugging duck")
# search.send_keys(Keys.RETURN) works similar to submit
# submit == ENTER
search_button.submit()

result = driver.find_element("id", "main")
print(result.text)
# Check documentation for explicit wait in python

time.sleep(10)

driver.quit()
