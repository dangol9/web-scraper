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
sleep(2)

email_in = driver.find_element_by_xpath('//*[@name="email"]')
email_in.send_keys(username)

password_in = driver.find_element_by_xpath('//*[@name="pass"]')
password_in.send_keys(password)

login_btn = driver.find_element_by_xpath('//*[@class="button wide_button"]')
login_btn.click()
sleep(2)

driver.get("https://m.vk.com/search?c[section]=people&c[group]=9884911")


for i in range(1, 6):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(0.5)
#python -i scraping.py
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

names = soup.find_all('span', class_='si_owner')

links = driver.find_elements_by_class_name('simple_fit_item')
profiles = []
for link in links:
    profiles.append(link.get_attribute('href'))
    #print(link)

for profile in profiles:
    driver.get(profile)
    sleep(2)
    print(profile)
    more_info = driver.find_element_by_xpath('//*[@class="OwnerInfo__linkBold"]')
    more_info.click()
    sleep(1)
    groups = driver.find_element_by_xpath("//div[contains(text(), 'Following')]")
    groups.click()
    sleep(2)
