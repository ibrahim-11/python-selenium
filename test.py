from selenium import webdriver 

import time

# creer une instance de webdriver
driver  = webdriver.Chrome()

# utilisation de l'instance
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

time.sleep(5)



driver.quit()