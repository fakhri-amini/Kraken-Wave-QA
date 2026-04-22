import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000")
    yield driver
    driver.quit()

def test_home(driver):
    assert "Kraken Wave" in driver.page_source

def test_add_to_cart(driver):
    driver.find_element(By.XPATH, "//a[contains(@href,'/add')]//button").click()
    time.sleep(1)
    assert "Cart (1)" in driver.page_source

def test_checkout_empty(driver):
    driver.get("http://127.0.0.1:5000/checkout")
    assert "Cart kosong" in driver.page_source

def test_checkout(driver):
    driver.get("http://127.0.0.1:5000")

    driver.find_element(By.XPATH, "//a[contains(@href,'/add')]//button").click()
    time.sleep(1)

    driver.get("http://127.0.0.1:5000/cart")
    driver.find_element(By.XPATH, "//a[@href='/checkout']/button").click()
    time.sleep(1)

    assert "Checkout berhasil" in driver.page_source

def test_remove_item(driver):
    driver.find_elements(By.TAG_NAME, "button")[0].click()
    time.sleep(1)

    driver.get("http://127.0.0.1:5000/cart")

    driver.find_element(By.XPATH, "//a[contains(@href, '/remove')]/button").click()
    time.sleep(1)

    assert "Cart kosong" in driver.page_source