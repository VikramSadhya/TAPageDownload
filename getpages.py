#Importing all the necessary libraries
from selenium import webdriver
import time
import os
import datetime
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#This url marks the starting point of the scraping. Change this to the home page of the hotel's page of any city / region/ state on TA
start = "https://www.tripadvisor.com/Hotels-g187849-Milan_Lombardy-Hotels.html"

#Create a folder for the current date and change the working directory to it
file = datetime.date.today()
filename = file.isoformat()
if not os.path.exists(filename):
    os.makedirs(filename)
os.chdir(filename)

#Loads the phantomjs webdriver
driver = webdriver.PhantomJS("C:\phantomjs-2.0.0-windows\\bin\phantomjs.exe")
driver.get(start)
wait = WebDriverWait(driver, 10)
page_limit = 5
counter = 1


#This loop saves the pages by click the next button on the current page
while counter <= page_limit:
    try:
        page = driver.page_source
        with open('page-' + str(counter) + '.html', 'w') as fid:
            fid.write(page.encode('utf-8'))
        print("Page: " + str(counter) + " saved!!")
        counter = counter + 1
        element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Next')))
        element.click()
        time.sleep(random.uniform(3, 10))
    except Exception, error:
        print(error)
        break