from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/inputs.html")


input = driver.find_element(By.NAME, "no_type")
input.clear()
input.send_keys("Anouarfefdiufhisufseiufhsiufhsiefh")

input_bis = WebDriverWait(driver, 10).until(
  EC.visibility_of_element_located((By.XPATH, "/html/body/form/input[5]"))
)
input_bis.clear()
input_bis.send_keys("Anouarfefdiufhisufseiufhsiufhsiefh")

driver.get_screenshot_as_file("input.png")

driver.quit()