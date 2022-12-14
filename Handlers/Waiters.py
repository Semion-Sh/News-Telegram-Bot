import asyncio, aioschedule
from selenium.webdriver.common.by import By
from .Errors import *
from Config import *


async def waiters():
    driver.get('https://hh.ru/search/vacancy?text=Официант&from=suggest_post&area=1002')
    driver.find_element(By.CLASS_NAME, 'serp-item').click()
    # print(driver.find_element(By.CLASS_NAME, 'vacancy-address-with-map').text)
    # driver.implicitly_wait(5)
    # body = driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div[1]')
    last_waiter_view = {
        # 'title': driver.find_element(By.CLASS_NAME, 'highlighted').text,
        # 'salary': driver.find_element(By.CLASS_NAME, 'g-user-content').text,
        # 'header': driver.find_element(By.CLASS_NAME, 'bloko-tag').text,
        'adress': driver.find_element(By.CLASS_NAME, 'adress').text
    }
    await bot.send_message(chat_id=waiters_chennel_id['admin'],
                           text=last_waiter_view['adress'],
                           parse_mode='html')
    print(last_waiter_view)


async def start_waiters_ru():
    aioschedule.every().minute.do(waiters)

