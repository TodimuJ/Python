import gymReservationDetails as grd
import time, re, webbrowser
import urllib.request 
import selenium.webdriver.chrome.webdriver
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

url = 'https://reservation.frontdesksuite.ca/rcfs/richcraftkanata'

driver = webdriver.Chrome()
driver.get(url)