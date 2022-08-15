from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

# THE GAME CONTINUE FOR 5 MINUTES

driver = webdriver.Chrome('c:/Development/chromedriver.exe')

driver.get("http://orteil.dashnet.org/experiments/cookie/")
time_out = time.time() + 5

cookie_button = driver.find_element(By.XPATH, '//*[@id="cookie"]')

products = driver.find_elements(By.CSS_SELECTOR, ".grayed b")

products_dict = {}
for p in products:
    products_dict[p.text.split('-')[len(p.text.split('-')) - 1]] = p.text.split('-')[0]
products_dict.pop('')
new_products_dict = {}
for price, p in products_dict.items():
    c = price.replace(",", "")
    c = c.replace(" ", "")
    new_products_dict[int(c)] = p

end = time.time() + 60*50

while True:

    cookie_button.click()

    if time_out <= time.time():

        cookies_count = driver.find_element(By.CSS_SELECTOR, "#money").text
        cookies_count = int(cookies_count.replace(",", ""))

        affordable = {}
        for price, product in new_products_dict.items():
            if price < cookies_count:
                affordable[price] = product

        product_max_price = max(affordable)
        print(product_max_price)
        to_purchase_id = "buy" + affordable[product_max_price]
        xpath = f'//*[@id="{to_purchase_id}"]'
        xpath = xpath.replace(" ", "")
        driver.find_element(By.XPATH, xpath).click()

        time_out = time.time() + 5

        if time.time() > end:
            cookies_per_sec = driver.find_element(By.XPATH, '//*[@id="cps"]').text
            cookies_per_sec = cookies_per_sec.replace("/", " per ")
            print(cookies_per_sec)
            break


