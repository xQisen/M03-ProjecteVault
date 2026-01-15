from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

# Configuració Chrome (headless opcional)
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# Ruta absoluta al fitxer login.html
file_path = "file://" + os.path.abspath("login.html")
driver.get(file_path)

passwords = ['1234', 'qwerty', 'admin', 'password123', 'letmein']

for pwd in passwords:
    # Localitzar camps
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "loginBtn")

    # Netejar camps
    username_input.clear()
    password_input.clear()

    # Injectar credencials
    username_input.send_keys("admin")
    password_input.send_keys(pwd)

    # Clicar login
    login_button.click()

    time.sleep(0.5)

    # Comprovar resultat
    message = driver.find_element(By.ID, "message").text

    if message == "ACCESS_GRANTED":
        print("VULNERABILITAT TROBADA")
        driver.save_screenshot("hacked.png")
        break

driver.quit()
sys.exit(1)
