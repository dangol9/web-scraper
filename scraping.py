from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from secrets import username, password

driver = webdriver.Chrome(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--disable notifications')

driver.get("https://m.vk.com")

sleep(1)

email_in = driver.find_element_by_xpath('//*[@name="email"]')
email_in.send_keys(username)

password_in = driver.find_element_by_xpath('//*[@name="pass"]')
password_in.send_keys(password)

login_btn = driver.find_element_by_xpath('//*[@class="button wide_button"]')
login_btn.click()

sleep(2)

driver.get("https://m.vk.com/search?c[section]=people&c[group]=9884911")

sleep(1)

for i in range(1, 6):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)

#python -i scraping.py

links = driver.find_elements_by_class_name('simple_fit_item')

profiles = []

sleep(1)

for link in links:
    profiles.append(link.get_attribute('href'))

sleep(1)

for profile in profiles:
    driver.get(profile)

    sleep(2)

    print(profile)
    profile_names = driver.find_elements_by_xpath('//h2[@class="op_header"]')
    profile_names.pop(0)

    for profile_name in profile_names:
        print(profile_name.text)

    more_info_btn = driver.find_element_by_xpath('//*[@class="OwnerInfo__linkBold"]')
    more_info_btn.click()

    sleep(2)

    groups_btn = driver.find_element_by_xpath("//div[contains(text(), 'Following')]")
    groups_btn.click()

    sleep(1)

    group_names = driver.find_elements_by_xpath('//div[@class="si_body"]')

    for group_name in group_names:
        print(group_name.text)

    sleep(1)

driver.quit()
