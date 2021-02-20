from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('[name="firstname"]')
    input1.send_keys("Frodo")
    input2 = browser.find_element_by_css_selector('[name="lastname"]')
    input2.send_keys("Baggins")
    input3 = browser.find_element_by_css_selector('[name="email"]')
    input3.send_keys("Shire@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    input4 = browser.find_element_by_css_selector('[id="file"]')
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    input4.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('[class="btn btn-primary"]')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()