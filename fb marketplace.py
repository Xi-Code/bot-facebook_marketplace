import requests
import re
import pandas as pd
import time
from termcolor import colored
from datetime import datetime
import random

from copy import copy
from tabnanny import check
import time
import csv
from unittest import skip
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import pytz
import selenium
import configparser
import argparse
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from termcolor import colored
from selenium.webdriver.common.by import \
    By  # https://stackoverflow.com/questions/69875125/find-element-by-commands-are-deprecated-in-selenium
import random
import numpy as np
from selenium.webdriver.common.proxy import *
from selenium import webdriver
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

print("Current selenium version is:", selenium.__version__)
# Select webdriver profile to use in selenium or not.
import sys
import os
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def driver_Profile(Profile_name):
    if Profile_name == "Yes":
        ### Selenium Web Driver Chrome Profile in Python
        # set proxy and other prefs.
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", allproxs[0]['IP Address'])
        profile.set_preference("network.proxy.http_port", int(allproxs[0]['Port']))
        # update to profile. you can do it repeated. FF driver will take it.
        profile.set_preference("network.proxy.ssl", allproxs[0]['IP Address']);
        profile.set_preference("network.proxy.ssl_port", int(allproxs[0]['Port']))
        # profile.update_preferences()
        # You would also like to block flash
        # profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)
        profile.set_preference("media.peerconnection.enabled", False)

        # save to FF profile
        profile.update_preferences()
        driver = webdriver.Firefox(profile, executable_path='./geckodriver')
        # webrtcshield = r'/home/qtdata/PycharmProjects/BotSAM/webrtc_leak_shield-1.0.7.xpi'
        # driver.install_addon(webrtcshield)
        # urbanvpn = r'/home/qtdata/PycharmProjects/BotSAM/urban_vpn-3.9.0.xpi'
        # driver.install_addon(urbanvpn)
        # driver.profile.add_extension(webrtcshield)
        # driver.profile.add_extension(urbanvpn)
        # driver.profile.set_preference("security.fileuri.strict_origin_policy", False)
        ### Check the version of Selenium currently installed, from Python
        print("Current selenium version is:", selenium.__version__)
        print("Current web browser is", driver.name)
        ### Current time using time module
        ## current_time = time.strftime("%H:%M:%S", time.localtime())
        ## print("Current time is:",current_time)
        ### datetime object containing current date and time
        now = datetime.now()
        ### dd/mm/YY H:M:S
        dt_string = now.strftime("%B %d, %Y    %H:%M:%S")
        print("Current date & time is:", dt_string)
        print(colored("You are using webdriver profile!", "red"))
    else:
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
        # chrome_options.add_argument("--headless")
        driver = uc.Chrome(options=chrome_options, executable_path=r'/home/qtdata/PycharmProjects/BotSAM/chromedriver')
        ### Check the version of Selenium currently installed, from Python
        print("Current selenium version is:", selenium.__version__)
        print("Current web browser is", driver.name)
        ### Current time using time module
        ## current_time = time.strftime("%H:%M:%S", time.localtime())
        ## print("Current time is:",current_time)
        ### datetime object containing current date and time
        now = datetime.now()
        ### dd/mm/YY H:M:S
        dt_string = now.strftime("%B %d, %Y    %H:%M:%S")
        print("Current date & time is:", dt_string)
        print(colored("You are NOT using webdriver profile!", "red"))
    return driver

def Scroll_Pages_infinite_loading ():
    ### Scroll to a page with infinite loading, like social network ones, facebook etc.
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    print("Begin scroll to a page with infinite loading.")
    # print("Begin Document Height", last_height)
    y = 0
    while True:
        # Scroll down to bottom
        for timer in range(0, 100):
            driver.execute_script("window.scrollTo(0, " + str(y) + ")")
            y += random.choice(np.arange(50, 60, 1)) # increase height random
            # print(random.choice(np.arange(50, 60, 1)), "&", y)
            time.sleep(0.1)
        # Wait to load page
        time.sleep(round(random.choice(np.arange(2, 5, 0.1)), 1))  # time sleep random
        # print("time sleep", round(random.choice(np.arange(2, 5, 0.1)), 1))
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print("Stop scroll page with infinite loading.")
            break
        else:
            # print("new height", new_height, "last height", last_height)
            last_height = new_height

def create_marketplace():
    driver.get("https://m.facebook.com/login")
    # Manual login
    time.sleep(30)
    df = pd.read_csv("input.csv")
    # initialise data
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("mycreds.txt")
    drive = GoogleDrive(gauth)
    for i in range(0, len(df)):
        name = df['Name'][i]
        price = df['Price'][i]
        content = df['Content'][i]
        photo = df['Photo'][i]
        type_of_listing = df['Type'][i]
        location = df['Location'][i]
        driver.get("https://m.facebook.com/marketplace/create")
        time.sleep(5)
        # Download files in folder
        folder_id = photo.split("/")[-1]
        file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
        # Click on add photo button
        for f in file_list:
            file = drive.CreateFile({'id': f['id']})
            file.GetContentFile(f['title']) 
            time.sleep(5)
            cd = os.getcwd()
            driver.find_element_by_xpath("//input[@type='file'][@name='photos-input']").send_keys(f"{cd}\\{f['title']}")
            print(f"{cd}\\{f['title']}")
        #Fill up other details
        # What are you selling
        driver.find_element_by_xpath("//input[contains(@name, 'title')]").send_keys(name)
        time.sleep(2)

        # Price
        driver.find_element_by_xpath("//input[contains(@name, 'price')]").send_keys(price)
        time.sleep(random.randint(2,4))

        #Category
        driver.find_element_by_xpath("//div[contains(@class, '_a58 _a5v _9_7 _2rgt _1j-g _2rgt')]").click()
        time.sleep(4)
        Scroll_Pages_infinite_loading()  
        # method 1
        categories = driver.find_elements_by_xpath("//div[contains(@class, '_59k _2rgt _1j-f _2rgt')]")
        for category in categories:
            if type_of_listing == category.text:
                action = ActionChains(driver)
                action.move_to_element(category).click().perform()
                time.sleep(5)
                break
        #method 2                                        
        # driver.find_element_by_xpath(f"//div[@text='{type_of_listing}' and @class='_59k _2rgt _1j-f _2rgt']").click()

        #Location
        btns = driver.find_elements_by_xpath("//div[contains(@class, '_a58 _a5v _9_7 _2rgt _1j-g _2rgt')]")
        for btn in btns:
            if btn.text == 'Location':
                btn.click()
        time.sleep(4)
        driver.find_element_by_xpath("//input[contains(@class, '_52ji _56bg _6il8 _2rgt _1j-g _2rgt')]").send_keys(location)
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='0']").click()

        #Description
        driver.find_element_by_xpath("//textarea[contains(@name, 'description')]").send_keys(content)
        time.sleep(random.randint(2, 5))

        #Post
        Scroll_Pages_infinite_loading() 
        btns = driver.find_elements_by_xpath("//div[contains(@class, '_a58 _a5t _9_7 _2rgt _1j-g _2rgt')]")
        time.sleep(random.randint(6, 15))
        btns[1].click()
        time.sleep(3)

if __name__ == '__main__':
    ### Select using drive profile or not ("Yes" or "No")
    ### Get time of a Python program's execution
    start_time = datetime.now()

    driver = driver_Profile('No')

    create_marketplace()
    time.sleep(2)
    # input is company name

    ###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ### Get time of a Python program's execution
    ## start_time = datetime.now()
    ## do your work here
    end_time = datetime.now()
    print(colored('Duration time: {} seconds '.format(end_time - start_time), "blue"), "\n start_time:", start_time,
          "\n", "end_time  :", end_time)