from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
browser = webdriver.Chrome("chromedriver")
browser.get(url)

time.sleep(2)

def scrap():
    headers = ["Name", "Distance", "Mass", "Radius"]
    starData = []

    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        tables = soup.find_all("table")
        table_rows = tables[7].find_all("tr")

        for tr_tags in table_rows:
            td_tags = tr_tags.find_all('td')
            tempList = []

            for index, td_tag in enumerate(td_tags):
                
                if index == 0:
                    
                    #print(tempList)
                    tempList.append(td_tag.find_all("a")[0].contents[0])
                    
                elif index == 5 or index == 7 or index == 8:
                    try:
                        tempList.append(td_tag.contents[0])

                    except:
                        tempList.append("")

            starData.append(tempList)
        
        with open('scrape.csv', 'w') as f:
            csvWriter = csv.writer(f)
            csvWriter.writerow(headers)
            csvWriter.writerows(starData)
scrap()