import time
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '.first[required]')
    input1.send_keys('text')
    input2 = browser.find_element(By.CSS_SELECTOR, '.second[required]')
    input2.send_keys('text')
    input3 = browser.find_element(By.CSS_SELECTOR, '.third[required]')
    input3.send_keys('text')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
    welcom_text = welcome_text_elt.text

    assert 'Congratulations! You have successfully registered!' == welcom_text
finally:
    time.sleep(10)
    browser.quit()