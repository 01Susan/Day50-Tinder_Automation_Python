import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv

chrome_path = r"D:\Downloads\chromedriver_win32\chromedriver.exe"
service = Service(chrome_path)
driver = webdriver.Chrome(service=service)
tinder_link = "https://tinder.com/"
driver.get(tinder_link)
driver.maximize_window()
load_dotenv()


# login in tinder account
def login_tinder():
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                                    '//*[@id="u-1779218560"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')))
    login_btn = driver.find_element(by=By.XPATH,
                                    value='//*[@id="u-1779218560"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
    login_btn.click()
    print("clicked")
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
        (By.XPATH, '//*[@id="u787367660"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]')))
    # choosing the facebook option to login

    choose_option = driver.find_element(by=By.XPATH,
                                        value='//*[@id="u787367660"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]')
    choose_option.click()
    print("clicked")
    time.sleep(4)

    # New login page popup(new window for login)
    fb_login_win = driver.window_handles[1]
    driver.switch_to.window(fb_login_win)

    # ---input email and password section ---
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    email_input = driver.find_element(by=By.ID, value="email")
    email_input.send_keys(email)
    WebDriverWait(driver, 2)
    password_input = driver.find_element(by=By.ID, value="pass")
    password_input.send_keys(password)
    login_click = driver.find_element(by=By.ID, value="loginbutton")
    login_click.click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])


# Navigate notification and location
def navigate():
    location_element = driver.find_element(by=By.XPATH,
                                           value='/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
    location_element.click()
    print("location_clicked")
    time.sleep(2)
    notification_element = driver.find_element(by=By.XPATH,
                                               value='/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
    notification_element.click()
    print("notification_clicked")
    time.sleep(2)
    cookie_element = driver.find_element(by=By.XPATH,
                                         value='/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]')
    cookie_element.click()
    print("cookie_element_clicked")


def find_girl():
    # like_element = driver.find_element(by=By.XPATH,
    #                                    value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button")
    dislike_element = driver.find_element(by=By.XPATH,
                                          value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button")
    for _ in range(40):
        time.sleep(5)
        try:
            dislike_element.click()
            print("clicked")
        except ElementClickInterceptedException:
            try:
                add_window = driver.find_element(by=By.XPATH,
                                                 value="/html/body/div[2]/main/div/div[2]/button[2]/div[2]/div[2]")
                add_window.click()
                print("getting add window section")
            except NoSuchElementException:
                pass
            driver.implicitly_wait(3)
            dislike_element.click()
        except NoSuchElementException:
            print("no such element exception")
            driver.implicitly_wait(3)
            dislike_element.click()


login_tinder()
time.sleep(4)
navigate()
time.sleep(10)
find_girl()
time.sleep(200)
