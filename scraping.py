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

page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

links = driver.find_elements_by_class_name('simple_fit_item')

profiles = []

sleep(1)

for link in links:
    profiles.append(link.get_attribute('href'))
    #print(link.get_attribute('text')))

sleep(1)

for profile in profiles:
    driver.get(profile)
    sleep(2)
    print(profile)
    profile_names = driver.find_elements_by_xpath('//h2[@class="op_header"]')
    profile_names.pop(0)

    for name in profile_names:
        print(name.text)

    more_info_btn = driver.find_element_by_xpath('//*[@class="OwnerInfo__linkBold"]')
    more_info_btn.click()

    sleep(2)

    groups_btn = driver.find_element_by_xpath("//div[contains(text(), 'Following')]")
    groups_btn.click()

    sleep(1)

    group_names = driver.find_elements_by_xpath('//div[@class="si_body"]')

    for name in group_names:
        print(name.text.split()[0])
    #last_height = driver.execute_script("return document.body.scrollHeight")
    #while True:
    # Scroll down to bottom
    #    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    #    sleep(2)
    # Calculate new scroll height and compare with last scroll height
    #    new_height = driver.execute_script("return document.body.scrollHeight")
    #    if new_height == last_height:
    #        break
    #    last_height = new_height
    #    sleep(1)


    sleep(1)
