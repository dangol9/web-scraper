from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from secrets import username, password
from selenium.common import exceptions
import pandas as pd

df = pd.DataFrame()

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

#driver.get("https://m.vk.com/search?c[section]=people&c[group]=9884911")
driver.get("https://m.vk.com/search?c[section]=people&c[group]=178161127&offset=200")

sleep(1)

links = []
profiles = []

while True:

    for i in range(1, 3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        sleep(1)

    try:

        links = driver.find_elements_by_class_name('simple_fit_item')

        if not links:

            break

        else:
                for link in links:
                    profiles.append(link.get_attribute('href'))

                more_users_btn = driver.find_element_by_xpath('//a[@class="show_more"]')
                more_users_btn.click()
                
                sleep(1)

    except (exceptions.StaleElementReferenceException, exceptions.NoSuchElementException) as e:
        pass
        break

#last_height = driver.execute_script("return document.documentElement.scrollHeight")

#while True:

#    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#    sleep(1)

#    new_height = driver.execute_script("return document.documentElement.scrollHeight")

#    if new_height == last_height:
#        break
#    last_height = new_height

sleep(1)

#python scraping.py

sleep(1)

sleep(1)

df['Profile'] = profiles

profile_names_table = []

group_names_table = []

i = 0

for profile in profiles:

    driver.get(profile)

    sleep(2)

    print(profile)

    profile_names = driver.find_elements_by_xpath('//h2[@class="op_header"]')
    profile_names.pop(0)

# add error catch
    try:

        for profile_name in profile_names:

            print(profile_name.text)

            profile_names_table.append(profile_name.text)

        more_info_btn = driver.find_element_by_xpath('//*[@class="OwnerInfo__linkBold"]')
        more_info_btn.click()

        sleep(2)

        groups_btn = driver.find_element_by_xpath("//div[contains(text(), 'Following')]")
        groups_btn.click()

        sleep(1)

        #    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        sleep(1)

        sleep(1)

        group_names = driver.find_elements_by_xpath('//div[@class="si_body"]')

        sleep(1)

        if not group_names:

            print("Groups not available")
            group_names_table.insert(i, ["Groups not available"])
            #group_names_table.append("Groups not available")
            i += 1

        else:

            listing = []

            for group_name in group_names:
                listing.append(group_name.text.split("\n")[0])
                print(group_name.text.split("\n")[0])

                #group_names_table.insert(i, [listing])

                print(i)

                #print(listing)

            group_names_table.insert(i, listing)

            #print(group_names_table)

            i += 1

        print("\n")

        sleep(1)

    #error catch ends here
    except:

        print("Groups not available")
        group_names_table.insert(i, ["Groups not available"])

        print(i)

        i += 1

        print("\n")


df['Name'] = profile_names_table
df['Groups'] = group_names_table

df.to_excel('result.xlsx', index = False)

driver.quit()
