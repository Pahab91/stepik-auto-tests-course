from selenium import webdriver
import time
import math


def calc(kek):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element_by_css_selector('[class="trollface btn btn-primary"]')
    button1.click()
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
    time.sleep(1)
    x1 = browser.find_element_by_css_selector('[id="input_value"]')
    x = x1.text
    print(x)
    y = calc(x)
    input1 = browser.find_element_by_css_selector('[id="answer"]')
    input1.send_keys(y)

    button = browser.find_element_by_css_selector('[class="btn btn-primary"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
