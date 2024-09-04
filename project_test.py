from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

# def test_check_title(driver):
#     title = driver.title
#     assert title == "Swag Labs"

#     sleep(10)

def test_priority(driver: WebDriver):
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.ID, "login-button")
    button.click()

    product_01 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    product_01.click()

    product_02 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    product_02.click()

    product_03 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
    product_03.click()
    
    product_04 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
    product_04.click()

    product_05 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
    product_05.click()

    product_06 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
    product_06.click()

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "6"

    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart.click()

    remove_product_01 = driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-bolt-t-shirt']")
    remove_product_01.click()

    cart_badge2 = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge2.text == "5"

    checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
    #checkout = driver.find_element(By.ID, "checkout")
    checkout.click()

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Aline")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Pereira")

    last_name = driver.find_element(By.XPATH, "//input[@id='postal-code']")
    last_name.send_keys("4012345")

    press_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
    press_continue.click()

    finish = driver.find_element(By.XPATH, "//button[@id='finish']")
    finish.click()

    check_message = driver.find_element(By.CLASS_NAME, "complete-header")
    assert check_message.text == "Thank you for your order!"



sleep(25)


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