import gymReservationDetails as grd
import time, os, re, webbrowser
import urllib.request 
from selenium import webdriver
# # # from webdriver_manager.chrome import ChromeDriverManager
# import selenium.webdriver.chrome.webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options

url = 'https://reservation.frontdesksuite.ca/rcfs/richcraftkanata'

driver = webdriver.Chrome()
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get(url)
print("test")