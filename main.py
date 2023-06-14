import time
import pickle
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions

driver = webdriver.Chrome(
    executable_path=r'C:\PY\1-scarping-parsing traders\parsing_yandex_music\chromedriver.exe')
try:
    driver.get('https://yandex.ru')
    time.sleep(15)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


# https://leagueoftraders.io/_next/data/jDEYM0MljLKuCcuKeKzU8/en/portfolio/62dff470f7fd9a2d9f268cf5.json

