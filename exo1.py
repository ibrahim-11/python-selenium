from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.cdiscount.com/")


cookies_btn_accept = WebDriverWait(driver, 10).until(
  EC.visibility_of_element_located((By.XPATH,"//*[@id=\"footer_tc_privacy_button_2\"]"))
)
cookies_btn_accept.click()

input_search = WebDriverWait(driver, 10).until(
  EC.visibility_of_element_located((By.XPATH,"//*[@id=\"search\"]"))
)
input_search.send_keys("ps4")


btn_search = WebDriverWait(driver, 10).until(
  EC.visibility_of_element_located((By.XPATH,"//*[@id=\"header\"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/button[2]"))
)

btn_search.click()


product_click = WebDriverWait(driver, 10).until(
  EC.visibility_of_element_located((By.XPATH,"//*[@id=\"lpBloc\"]/li[2]/div/div/form/div[1]/ul/li/img"))
)

product_click.click()

btn_ajout_panier = WebDriverWait(driver, 10).until(
  EC.visibility_of_element_located((By.XPATH,"//*[@id=\"fpAddBsk\"]"))
)

btn_ajout_panier.click()

btn_consulte_pannier = WebDriverWait(driver, 10).until(
  EC.visibility_of_element_located((By.XPATH,"//*[@id=\"header\"]/div[1]/div[2]/div[3]/div/div[3]/a"))
)
# btn_consulte_pannier = WebDriverWait(driver, 10).until(
#   EC.visibility_of_element_located((By.ID,"itemCart"))
# )

try : 
    btn_consulte_pannier.click()
except Exception as ex:
  assert print("pannier introuvable")


driver.get_screenshot_as_file("pannier.png")
# time.sleep(5)
sleep(5)
