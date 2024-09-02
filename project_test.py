from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
from time import sleep
import pytest
#browser = webdriver.Chrome()

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    yield driver

    driver.quit()

def test_check_title(driver):
    title = driver.title
    assert title == "Swag Labs"

    sleep(10)

def login_standard_user(driver):
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.ID, "login-button")
    button.click()

    sleep(10)

def add_product_01(driver):
    product_01 = driver.find_element("")
    



# Logar no site com o usuário standard


# ○ Adicionar os 6 produtos no carrinho
# ○ Conferir que no carrinho tem a badge com 6 produtos
# ○ Entrar no carrinho
# ○ Remover um dos produtos do carrinho
# ○ Conferir que no carrinho tem a badge com 5 produtos
# ○ Clicar no botão Checkout
# ○ Preencher os dados solicitados e clicar em Continue
# ○ Clicar no botão Finish
# ○ Conferir a mensagem “Thank you for your order!”

sleep(10)