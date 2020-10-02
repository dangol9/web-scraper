# web-scraper
Python web scraper for the Visualizing Social Networks Project

**Tested with 1000 users** <br>

This is a script that scrapes users, links to their profiles and the groups that they are in. The amount of scraped users per runtime is not limited, but is affected by webdriver stability and network connectivity - minor changes in these things may alter the scraping behavior and crash the script, so make sure that your interent is stable and that your computer doesn't go into sleep mode while the script is running, also it is recommended to let the computer idle while the script is running - i.e leave the script running overnight. <br>

Script is the file named **scraping.py** <br>

Script asks the user for input: <br>
  **count - how many users we want to show on the list** <br>
  **offset - how many users ahead from the first users should the list be** <br>
  
Ideally, if we want to scrape 2000 users - then the input would be: **offset=0 and count = 2000**, <br>
**BUT** since count=0 is not supported - there is an another file named **scrape_first_user.py** which scrapes the first user on the list and after that we can continue with **scraping.py** with the values **offset = 1 and count = 2000** <br>

**To scrape 2000 users after the first 2000 users - the input should be: offset=2000 and count=4000** <br>

Script logic - **scrape all user data from the desired group** > **use that data to navigate to each scraped user** > **check the "Following" page of each scraped user** > **scrape around 40 groups from each user** > **repeat** > **at the end all the data is appended into an excel table.** <br>

Dependencies: <br>
  **selenium <br>
  webdriver_manager <br>
  pandas** <br>
  
  
**IMPORTANT - if you want to run the script multiple times - then to avoid data loss move the created results.xlsx file somewhere else - after every successful run then script overwrites that file**<br>

How to run: 

  1. Download Python.
  2. Download the scraping.py and the secrets.py files.
  3. Put the scraping.py and secrets.py files into a directory.
  4. Use cmd to install all the dependencies that are required. (pip install *dependency*)
  5. Make sure that VK two-step authentication is disabled on your account.
  6. Change the secrets.py file data - username should be your VK email address and password should be your VK password. **(Example: username="email@mail.ru")**
  7. Run the script by typing *python scraping.py*.
  8. Enter offset and count values.
  9. Sit back and look at how the script works. **(Expected runtime: 10 minutes per 100 users)**
  
