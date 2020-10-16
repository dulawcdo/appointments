#!/bin/python

from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import subprocess

driver = webdriver.Firefox()
driver.get("https://udenver.zoom.us/meeting/schedule")

time.sleep(5)

driver.find_element_by_id("username").send_keys("zeeshan.reshamwala@du.edu")
driver.find_element_by_id("password").send_keys("Zmn76642Denver")
driver.find_element_by_css_selector("button.form-element").click()

# Now enter a date

# driver.execute_script("some javascript code here");

time.sleep(25)

driver.execute_script("document.getElementById('start_date').removeAttribute('readonly',0);")

print('Enter date')
date = raw_input().strip()

p = subprocess.Popen(["date", "+%m/%d/%Y", "-d", date], stdout=subprocess.PIPE)
out, err = p.communicate()

print(out)

startdate = driver.find_element_by_id('start_date')
startdate.click()
startdate.clear()
startdate.send_keys(out)



print('Enter time')
aptime = raw_input().strip()

p = subprocess.Popen(["date", "+%-I:%M", "-d", aptime], stdout=subprocess.PIPE)
out, err = p.communicate()

print(out.strip())

driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div[5]/form/div[2]/div[1]/div[1]/div/div[1]/div').click()
# driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div[5]/form/div[2]/div[1]/div[1]/div/div[1]/div').send_keys(out)
driver.find_element_by_class_name('zm-select-input__inner').send_keys(out.strip())
driver.find_element_by_class_name('zm-select-input__inner').send_keys(Keys.ENTER)

time.sleep(1)
p = subprocess.Popen(["date", "+%H*60", "-d", aptime], stdout=subprocess.PIPE)
resulting, err = p.communicate()
print(int(resulting))

driver.find_element_by_xpath('//*[@id="start_time_2"]').click()
if resulting > 720:
    driver.find_element_by_id('select-item-start_time_2-1').click()
else:
    driver.find_element_by_id('select-item-start_time_2-0').click()


#driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div[5]/form/div[2]/div[1]/div[1]/div/div[1]/div/div/button/i').click()

# if out 
# driver.find_element_by_
# 
# 
# 
# aptimeselect = Select(driver.find_element_by_css_selector('#start_time-popup-list'))
# aptimeselect.select_by_visible_text(out)

