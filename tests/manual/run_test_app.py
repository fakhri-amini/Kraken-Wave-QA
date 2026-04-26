from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# TEST HOME
driver.get("http://127.0.0.1:5000")
print("TEST HOME")
assert "Kraken Wave" in driver.page_source

# TEST CART KOSONG
driver.get("http://127.0.0.1:5000/cart")
assert "Cart kosong" in driver.page_source

# TAMBAH ITEM
driver.get("http://127.0.0.1:5000")

for i in range(3):
    driver.find_elements(By.TAG_NAME, "button")[0].click()
    time.sleep(1)

assert "Cart (3)" in driver.page_source

# CHECKOUT BERHASIL
driver.get("http://127.0.0.1:5000/cart")
driver.find_element(By.XPATH, "//a[@href='/checkout']/button").click()

time.sleep(1)
assert "Checkout berhasil" in driver.page_source

# CEK CART SETELAH CHECKOUT
driver.get("http://127.0.0.1:5000/cart")
assert "Cart kosong" in driver.page_source

print("SEMUA TEST SELESAI")
driver.quit()