#!/usr/bin/env python3
import os
import time
import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

#global variables
site = "https://www.singlecare.com"
driver = webdriver.Chrome(ChromeDriverManager().install())

def get_data(query):
    search_bar = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/section/div[3]/button/span')
    search_bar.send_keys('Test Input')
    search_bar.send_keys(Keys.ENTER)

def get_query():
    my_file = open("src/drug_query.txt", "r")
    drug_query = my_file.readlines()
    drug_query = list(map(lambda x:x.strip(),drug_query))
    print(drug_query)
    return drug_query

def main():
    print("Scraping GoodRx Site for the following: ")
    query = get_query()
    print("Navigating to Site")
    driver.get(site)
    get_data(query)

if __name__ == "__main__":
    main()