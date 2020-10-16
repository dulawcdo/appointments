from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://udenver.zoom.us/meeting/schedule")

time.sleep(5)

driver.find_element_by_id("username").send_keys("zeeshan.reshamwala@du.edu")
driver.find_element_by_id("password").send_keys("Zmn76642Denver")
driver.find_element_by_css_selector("button.form-element").click()


a = 1

while a == 1:
    
    print("Input method? [a]Appt request / [m]Manual")
    x = raw_input()
    
    # USING APPOINTMENT DETAILS pulled from email via emacs function send-appt-to-shell()
    
    
    if x == 'a':
        with open('rawappt.txt') as f:
            lines = f.readlines()
            apptint = 0
            for line in lines:
                x,y = line.split(':', 1)
                print(y.strip())
                apptint += 1
                if apptint == 1:
                    counselorname = y.strip()
                    if counselorname == "Andrea Montague":
                        counseloremail = "andrea.montague@du.edu"
                    else:
                        counseloremail = "eric.bono@du.edu"
                elif apptint == 2:
                    apprawtime, appdate = y.strip().split("on")
                    apptime, appampm = apprawtime.strip().split(" ")
                elif apptint == 3:
                    studentname = y.strip()
    else:
        print ('Counselor? Andrea[a] / Eric[e]')
        x2 = raw_input()
        
        if  x2 == 'a':
            counselorname = "Andrea Montague"
            counseloremail = "andrea.montague@du.edu"
        else:
            counselorname = "Eric Bono"
            counseloremail = "eric.bono@du.edu"
        print('Time?')
        apptime = raw_input().strip()
        print('AM/PM?')
        appampm = raw_input().strip()
        print('Student Name?')
        studentname = raw_input().strip()
        print('Date?')
        appdate = raw_input().strip()
        
    
    print("Appt generated. Another? (y/n)")
    x5 = raw_input()
    if x5 == 'y':
        driver.get("https://udenver.zoom.us/meeting/schedule")
        continue
    else:
        a = 0


driver.quit()

