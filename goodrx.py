#!/usr/bin/env python3
import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

#global variables
driver = webdriver.Chrome()
email = ''
firstName = ''
lastName = ''

print("Hello")

driver.get("https://www.python.org")