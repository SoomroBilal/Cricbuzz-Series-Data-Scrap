# Importing all the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
import pandas as pd


# Creating Lists to save data 
series = []
links = []
dates  = []

# Accessing the website
driver = webdriver.Chrome()
driver.get("https://www.cricbuzz.com")
time.sleep(5)

# Navigating to series link and accessing it
drop = driver.find_element(By.XPATH,"//div[@id='seriesDropDown']//nav[@class='cb-sub-navigation']//a[@class='cb-text-link cb-subnav-item']")
driver.get(drop.get_attribute('href'))
time.sleep(5)

# Using XPATH, finding the required tags
series_list = driver.find_elements(By.XPATH,"//a[@class='text-black text-hvr-underline']")
date_list = driver.find_elements(By.XPATH,"//div[@class='text-gray cb-font-12']")


# Iterating through lists to get necessary data
for series in series_list:
    series.append(series.text)
    links.append(series.get_attribute('href'))

for date in date_list:
    dates.append(date.text)
    
driver.close()


# Creating a data Frame
df = {'Series':series, 'Date':dates, 'Link for full schedule':links}
df = pd.DataFrame(df)
df.head()





