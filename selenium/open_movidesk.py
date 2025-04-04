import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user_name_movidesk = 'usuario'
user_key_movidesk = 'senha'
movidesk_url = 'https://prefixo.movidesk.com/Account/Login'

browser = Chrome()
browser.get(movidesk_url)

campo_name_user = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, "UserName"))
)
campo_name_user.send_keys(user_name_movidesk)

campo_key_user = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, "Password"))
)
campo_key_user.send_keys(user_key_movidesk)

entrar = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "btnSubmit"))
)
entrar.click()

time.sleep(5)
#browser.quit()
