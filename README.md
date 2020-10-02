# web-scraper
Python web scraper for the Visualizing Social Networks Project

**Tested with 1000 users**

This is a script that scrapes users, links to their profiles and the groups that they are in. The amount of scraped users per runtime is not limited, but is affected by webdriver stability and network connectivity - minor changes in these things may alter the scraping behavior and crash the script.

Script is the file named **scripting.py**

Script asks the user for input:
  **count - how many users we want to show on the list**
  **offset - how many users ahead from the first users should the list be**
  
Ideally, if we want to scrape 2000 users - then the input would be: **offset=0 and count = 2000**, <br>
**BUT** since count=0 is not supported - there is an another file named **scrape_first_user.py** which scrapes the first user on the list and after that we can continue with **offset = 1 and count = 2000**

**To scrape 2000 users after the first 2000 users - the input should be: offset=2000 and count=4000**

Script logic - **scrape all user data from the desired group** > **use that data to navigate to each scraped user** > **check the "Following" page of each scraped user** > **scrape around 40 groups from each user** > **repeat** > **at the end all the data is appended into an excel table.**

Dependencies: <br>
  **selenium <br>
  webdriver_manager <br>
  pandas** <br>
  
How to run:

  1. Download Python.
  2. Download the scraping.py and the secrets.py files.
  3. Put the scraping.py file into a directory.
  4. Use cmd to install all the dependencies that are required. (pip install *dependency*)
  5. Make sure that VK two-step authentication is disabled on your account
  6. Change the secrets.py file data - username should be your VK email address and password should be your VK password. **(Example: username="email@mail.ru")**
  7. Run the script by typing *python scraping.py*
  8. Sit back and look at how the script works **(Expected runtime: 10 minutes per 100 users)**
  
