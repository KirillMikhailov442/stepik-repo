"""Stepik module 2: checkboxes, radiobuttons and a math expression."""
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("https://suninjuly.github.io/math.html")
    x = int(browser.find_element(By.ID, "input_value").text)
    answer = str(math.log(abs(12 * math.sin(x))))
    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    print(browser.switch_to.alert.text)
