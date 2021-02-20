from selenium import webdriver
import time
import math


def calc(kek):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x1 = browser.find_element_by_css_selector('[id="treasure"]')
    x = x1.get_attribute("valuex")
    print(x)
    y = calc(x)
    input1 = browser.find_element_by_css_selector('[id="answer"]')
    input1.send_keys(y)
    checkbox = browser.find_element_by_css_selector('[id="robotCheckbox"]')
    checkbox.click()
    radio = browser.find_element_by_css_selector('[id="robotsRule"]')
    radio.click()
    time.sleep(1)
    button = browser.find_element_by_css_selector('[class="btn btn-default"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()