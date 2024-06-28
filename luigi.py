from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://black-book-editions.fr/")

# Validation des cookies
driver.find_element(By.XPATH, "//*[@id=\"form-accept-cookies\"]/button[2]").click()

#Test de la bar de recherche
try:
  bar_de_recherche = driver.find_element(By.ID, "str_to_search")
  bar_de_recherche.clear()
  bar_de_recherche.send_keys("d&d")
  bar_de_recherche.send_keys(Keys.ENTER)

  prix_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"produit_11727\"]/div[2]"))
  )
  prix = prix_element.text
  print(prix)
except Exception as ex:
  assert print("produit introuvable")

time.sleep(25)