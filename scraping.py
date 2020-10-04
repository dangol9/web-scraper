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

offset = input("Enter offset:")
num_of_pages = input("Enter number of pages you want to see:")

if int(offset) == 0:
    offset_pages=0
else:
    offset_pages = int(offset) / 50

counter = int(offset_pages) + 1

all_pages = int(num_of_pages) + int(offset_pages)

website = ("https://m.vk.com/anxietyboys?act=members&offset=" + offset)

driver.get(website)

sleep(1)

links = []
profiles = []


while True:

    for i in range(1, 6):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        sleep(1)

    try:

        links = driver.find_elements_by_class_name('inline_item')

        if not links:

            break

        else:
                for link in links:
                    profiles.append(link.get_attribute('href'))

                counter += 1

                print("Current page is: ", counter)
                print("Allpages", all_pages)

                if counter == (all_pages + 1):
                    print(profiles)
                    break

                more_users_btn = driver.find_element_by_xpath("//a[contains(text(), '{}')]".format(counter))
                more_users_btn.click()

                sleep(1)

    except (exceptions.StaleElementReferenceException, exceptions.NoSuchElementException) as e:
        pass
        break

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
    sleep(1)
    try:
        profile_names = driver.find_elements_by_xpath('//h2[@class="op_header"]')
        profile_names.pop(0)
        if not profile_names:
            print("Profile deleted")
            profile_names.append("Profile deleted")
    except:
        print("Profile deleted")
        profile_names.append("Profile deleted")


# add error catch
    try:

        for profile_name in profile_names:
            try:
                print(profile_name.text)
                sleep(1)
                profile_names_table.append(profile_name.text)
            except:
                profile_names_table.append(profile_name)
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



            group_names_table.insert(i, listing)
            print(i)
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

df.to_excel('result_3.xlsx', index = False)

driver.quit()
