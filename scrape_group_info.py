from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from secrets import username, password
from selenium.common import exceptions
import pandas as pd
import names as n

df = pd.DataFrame()

groups_name_table = []

group_followers_table = []


driver = webdriver.Chrome(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument('--disable notifications')

driver.get("https://vk.com")

sleep(1)

email_in = driver.find_element_by_xpath('//*[@name="email"]')
email_in.send_keys(username)

password_in = driver.find_element_by_xpath('//*[@name="pass"]')
password_in.send_keys(password)

login_btn = driver.find_element_by_xpath('//*[@class="button wide_button"]')
login_btn.click()

sleep(2)

driver.get("https://vk.com/groups?act=catalog&c%5Blike_hints%5D=1&c%5Bper_page%5D=40&c%5Bsection%5D=communities&c%5Bskip_catalog%5D=1&c%5Bsort%5D=6")

df = pd.read_excel('TopGroup.xlsx')
groups = df['Group'].tolist()

sleep(1)

for group in groups:
    group_in = driver.find_element_by_xpath("//input[@placeholder='Search communities']")
    group_in.send_keys(group)

    sleep(2)

    try:
        link = driver.find_element_by_xpath("//div[contains(@class, 'labeled title')]/a").get_attribute('href')
        driver.get(link)
    except:
        print("Wierd search")
    sleep(1)

    print("Name: "+ str(group))

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    sleep(1)

    try:
        followers = driver.find_element_by_xpath("//div[@id='public_followers']/a[@class='module_header']/div[contains(@class, 'header_top clear_fix')]")
        print("Followers: " + followers.text.split("\n")[1])
    except:
        print("Followers not available")

    try:

        status = driver.find_element_by_xpath("//div[contains(@class, 'page_current_info')]/span[contains(@class, 'current_text')]")
        print("Status: " + status.text)
    except:
        print("Status not available")

    driver.get("https://vk.com/groups?act=catalog&c%5Blike_hints%5D=1&c%5Bper_page%5D=40&c%5Bsection%5D=communities&c%5Bskip_catalog%5D=1&c%5Bsort%5D=6")
    sleep(1)
