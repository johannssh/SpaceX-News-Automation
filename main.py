from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pandas as pd
from datetime import datetime
import os
import sys

path = os.path.dirname(sys.executable)
current_date = datetime.now()
date = current_date.strftime("%m%d%Y")

options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)
driver.get('https://www.nytimes.com/spotlight/spacex')

containers = driver.find_elements(by="xpath", value='//div[@class="css-10wtrbd"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./h3/a').text
    link = container.find_element(by="xpath", value='./h3/a').get_attribute("href")
    titles.append(title)
    links.append(link)

dict = {
    'title' : titles,
    'link' : links
}

headline = pd.DataFrame(dict)
file_name = f'SpaceXNews-{date}.csv'
resulting_path = os.path.join(path,file_name)

headline.to_csv(resulting_path)

driver.quit()