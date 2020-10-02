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


website = ("https://m.vk.com/search?c[section]=people&c[group]=9884911")

driver.get(website)
sleep(1)


profiles = []


sleep(1)

link = driver.find_element_by_class_name('simple_fit_item')

profiles.append(link.get_attribute('href'))

sleep(1)


sleep(1)

#python scraping.py

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

        sleep(2)

        #    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        sleep(1)

        group_names = driver.find_elements_by_xpath('//div[@class="si_body"]')

        sleep(1)

        if not group_names:

            print("Groups not available")
            group_names_table.insert(i, ["Groups not available"])
            print(i)
            i += 1

        else:

            listing = []

            for group_name in group_names:
                listing.append(group_name.text.split("\n")[0])
                print(group_name.text.split("\n")[0])

                print(i)

            group_names_table.insert(i, listing)

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

df.to_excel('result_first.xlsx', index = False)

driver.quit()
