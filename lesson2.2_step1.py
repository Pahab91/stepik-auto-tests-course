from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x1 = browser.find_element_by_css_selector('[id="num1"]')
    x = int(x1.text)
    print(x)
    y1 = browser.find_element_by_css_selector('[id="num2"]')
    y = int(y1.text)
    print(y)
    n = x + y
    print(n)
    n = str(n)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(n)
    button = browser.find_element_by_css_selector('[class="btn btn-default"]')
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
