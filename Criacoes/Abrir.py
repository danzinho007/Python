from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# Inicialize o navegador
options = webdriver.ChromeOptions()
options.add_argument("--profile-manager")

# Inicialize o serviço do ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Abra o Chrome e selecione o 1° usuário
driver.get("chrome://settings/")
WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.ID, "profile-picker"))
profiles = driver.find_elements(By.CSS_SELECTOR, "#profile-picker .profile")
profiles = driver.find_elements(By.CSS_SELECTOR, "#profile-picker .profile")
for profile in profiles:
    if profile.text == "Dan":
        profile.click()
        break

# Abra as 5 páginas
urls = ["https://www.google.com", "https://www.youtube.com", "https://www.github.com", "https://www.stackoverflow.com", "https://www.python.org"]
for url in urls:
    driver.get(url)

# Feche o navegador quando terminar
driver.quit()
