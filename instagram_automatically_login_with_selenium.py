from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
## load chromedriver.exe
chromedriver = './chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.instagram.com/?hl=en')

## your id and password
insta_id = '************'
insta_pw = '************'
## login services
def long_in(insta_id, insta_pw):
    try:
        link_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='_fcn8k']"))
        )
        link_login.click()

    except Exception, e:
        print e

    username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))

    username.send_keys(insta_id)
    password.send_keys(insta_pw)
    btn_login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='_ah57t _84y62 _i46jh _rmr7s']")))
    btn_login.click()
    return True
### Click "Like" at on first
def like_click():
    try:
        like = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,"//span[@class = '_soakw coreSpriteHeartOpen']"))
            )
        like.click()
    except Exception, e:
        print e
    return True

### Click "like" on the screen 
def like_many_click():
    try:
        likebuttons= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class ='_qj7yb']")))

        for likebutton in likebuttons.WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'span'))):
            likebutton.click()

    except Exception, e:
        print e

long_in(insta_id, insta_pw)

like_click()

like_many_click()


#driver.quit()"""
