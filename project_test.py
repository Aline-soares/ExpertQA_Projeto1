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
    checkout.click()

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Aline")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Pereira")

    postcode = driver.find_element(By.XPATH, "//input[@id='postal-code']")
    postcode.send_keys("4012345")

    press_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
    press_continue.click()

    finish = driver.find_element(By.XPATH, "//button[@id='finish']")
    finish.click()

    check_message = driver.find_element(By.CLASS_NAME, "complete-header")
    assert check_message.text == "Thank you for your order!"

sleep(10)

def test_checkout_no_postcode(driver: WebDriver):
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.ID, "login-button")
    button.click()

    product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
    product.click()

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1"

    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart.click()

    checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
    checkout.click()

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Aline")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Pereira")

    press_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
    press_continue.click()

    check_messageerror = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert check_messageerror.text == "Error: Postal Code is required"


sleep(10)

def test_products_quantity(driver: WebDriver):
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.ID, "login-button")
    button.click()

    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    products_quantity = len(products)
    print(f"The page shows {products_quantity} products")
    assert products_quantity == 6

sleep(10)    



# def test_order_of_products(driver: WebDriver):

#     username = driver.find_element(By.ID, "user-name")
#     username.send_keys("standard_user")

#     password = driver.find_element(By.ID, "password")
#     password.send_keys("secret_sauce")

#     button = driver.find_element(By.ID, "login-button")
#     button.click()

#     filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
#     filter_dropdown.click()
#     filter_dropdown = driver.find_element(By.XPATH, "//option[@value='lohi']")
#     filter_dropdown.click()

# sleep(20)









# Sugestão 2: Verificar a Ordenação dos Produtos
# Logar no site com o usuário standard.
# Navegar para a página de produtos.
# Alterar o critério de ordenação dos produtos (por exemplo, de "Preço - baixo para alto" para "Preço - alto para baixo").
# Verificar se os produtos estão sendo exibidos conforme o critério de ordenação selecionado.
# Adicionar um produto ao carrinho.
# Entrar no carrinho e verificar se o produto foi adicionado corretamente.
# Finalizar a compra e confirmar a mensagem de agradecimento.

# Sugestão 3: Testar o Fluxo de Compra Sem Preencher Informações de Checkout
# Logar no site com o usuário standard.
# Adicionar alguns produtos ao carrinho (pode ser um ou dois).
# Entrar no carrinho e clicar em Checkout.
# Deixar os campos obrigatórios de informação em branco (Nome, Sobrenome e CEP).
# Tentar avançar no fluxo e verificar se o site exibe as mensagens de erro apropriadas.
# Preencher as informações corretamente e concluir o pedido.
# Verificar a mensagem de agradecimento após finalizar a compra.