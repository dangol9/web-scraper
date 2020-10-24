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

groups_about_table = []

groups_followers_table = []

df2 = pd.DataFrame()

c = 0

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

driver.get("https://vk.com/groups?act=catalog&c%5Blike_hints%5D=1&c%5Bper_page%5D=40&c%5Bsection%5D=communities&c%5Bskip_catalog%5D=1&c%5Bsort%5D=6")

df = pd.read_excel('TopGroup.xlsx')
groups = df['Group'].tolist()

sleep(1)
groups = groups[:20]
print(groups)
for group in groups:
    c += 1

    group_in = driver.find_element_by_xpath("//input[@placeholder='Search communities']")
    group_in.send_keys(group)

    sleep(2)

    search_btn = driver.find_element_by_xpath("//button[contains(@class, 'ui_search_button_search _ui_search_button_search')]")

    search_btn.click()

    sleep(2)

    try:
        about = driver.find_element_by_xpath("//div[contains(@class, 'labeled')][2]")
        print("About: " + about.text)
        groups_about_table.append(about.text)
    except:
        print("No about info")
        groups_about_table.append("No about info")

    try:
        name = driver.find_element_by_xpath("//div[contains(@class, 'labeled title')]")
        link = driver.find_element_by_xpath("//div[contains(@class, 'labeled title')]/a").get_attribute('href')
        print("Name: "+ name.text)
        groups_name_table.append(name.text)
        #driver.get(link)
    except:
        print("Bad search")
        groups_name_table.append("Bad search")

    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #sleep(2)

    try:
        #followers = driver.find_element_by_xpath("//div[@id='public_followers']/a[@class='module_header']/div[contains(@class, 'header_top clear_fix')]")
        followers = driver.find_element_by_xpath("//div[contains(@class, 'labeled')][3]")
        print("Followers: " + followers.text.split(" ")[0])
        #print("Followers: " + follower.text.split("\n")[1])
        groups_followers_table.append(followers.text.split(" ")[0])
    except:
        print("Followers not available")
        groups_followers_table.append("Followers not available")

    print(c)

    driver.get("https://vk.com/groups?act=catalog&c%5Blike_hints%5D=1&c%5Bper_page%5D=40&c%5Bsection%5D=communities&c%5Bskip_catalog%5D=1&c%5Bsort%5D=6")

    sleep(2)

df2['Name']= groups_name_table
df2['About'] = groups_about_table
df2['Followers'] = groups_followers_table

df2.to_excel('result_groups.xlsx', index = False)

driver.quit()
