import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elem_x = browser.find_element(By.ID, "input_value")
    x = elem_x.text
    y = calc(x)

    elem_input = browser.find_element(By.ID, "answer")
    elem_input.send_keys(y)

    elem_checkbox = browser.find_element(By.ID, "robotCheckbox")
    elem_checkbox.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    time.sleep(2)

    button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()