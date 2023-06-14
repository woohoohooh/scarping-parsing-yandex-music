from selenium import webdriver
from seleniumwire import webdriver
import time

options = webdriver.ChromeOptions()

options.add_argument('user_agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/2010001 Firefox/84.0')

driver = webdriver.Chrome(
    executable_path=r'C:\PY\scrap_tutorial-master\chromedriver\chromedriver',
    options=options)

try:
    driver.get(url='https://vk.com/')
    time.sleep(5)

    email_input = driver.find_element_by_id('index_email')
    email_input.clear()
    email_input.send_keys('79513610187')
    time.sleep(5)

    login_button = driver.find_element_by_id('index_login_button').click()

    password_input = driver.find_element_by_id('index_pass')
    password_input.clear()
    password_input.send_keys('jjfj2&&@KJjkUyf21372N(Fndsk2i3ifiOILLL3i32ifneni38&2G@')
    time.sleep(5)

    login_button = driver.find_element_by_id('index_login_button').click()

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
