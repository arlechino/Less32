from faker import Faker
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestsOne:
    def test_one(self):
        browser = webdriver.Chrome(options=Options())
        browser.maximize_window()
        browser.get('https://www.google.com/')

        fake = Faker()

        button_canceld_cookies = browser.find_element(By.XPATH, '//*[@id="W0wltc"]')
        button_enter = browser.find_element(By.CSS_SELECTOR, '.gb_ia.gb_ja.gb_fe.gb_fd')



        WebDriverWait(browser, 5).until(EC.element_to_be_clickable(button_canceld_cookies))
        button_canceld_cookies.click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable(button_enter))
        button_enter.click()
        assert WebDriverWait(browser, 5).until(EC.url_changes('https://accounts.google.com/v3/signin/identifier?dsh=S784845%3A1676713953885824&continue=https%3A%2F%2Fwww.googl' \
        'e.com%2F&ec=GAZAmgQ&hl=ru&passive=true&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHcJv0ASeqS5IaAcEGhGMCq9ifH9' \
        '2_tbW36T-uQfhDxKf7K1bHI0S-2kDuWzuol7FASiM6Dumg'))


        button_create_account = browser.find_element(By.XPATH,
                                                     '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/button/span')
        button_for_personal_use = browser.find_element(By.CSS_SELECTOR,
                                                       '#yDmH0d > c-wiz > div > div.eKnrVb > div > div.Z6Ep7d > div > div.XOrBDc > div > div > div:nth-child(2) > div > ul > li:nth-child(2) > span.VfPpkd-StrnGf-rymPhb-b9t22c')
        button_create_account.click()
        time.sleep(5)
        button_for_personal_use.click()
        input_name = browser.find_element(By.CSS_SELECTOR, '#firstName')
        input_second_name = browser.find_element(By.CSS_SELECTOR, '#lastName')
        # time.sleep(5)

        assert WebDriverWait(browser, 5).until(EC.url_changes
                                               ('https://accounts.google.com/signup/v2/webcreateaccount?biz=false&'
                                                'cc=PT&continue=https%3A%2F%2Fwww.google.com%2F&dsh=S784845%3A16767139'
                                                '53885824&flowEntry=SignUp&flowName=GlifWebSignIn&hl=ru&ifkv=AWnogHdKGEY'
                                                'OhaGiNMiK7vCSJN-vYcloXF3yzG_htaS8Rx9m_6ECB8hH4kFZzHcujRq_8nQfXDg7'))
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable(input_name))
        input_name.send_keys( fake.name() )
        input_second_name.send_keys(fake.name())

        time.sleep(5)
        browser.quit()