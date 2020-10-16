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
                    elif counselorname == "Eric Bono":
                        counseloremail = "eric.bono@du.edu"
                    else:
                        counseloremail = "samantha.rutsky@du.edu"
                        
                elif apptint == 2:
                    apprawtime, appdate = y.strip().split("on")
                    apptime, appampm = apprawtime.strip().split(" ")
                elif apptint == 3:
                    studentname = y.strip()
    else:
        print ('Counselor? Andrea[a] / Eric[e] / Sam [s] / Other [o]')
        x2 = raw_input()
        
        if  x2 == 'a':
            counselorname = "Andrea Montague"
            counseloremail = "andrea.montague@du.edu"
        elif x2 == 'e':
            counselorname = "Eric Bono"
            counseloremail = "eric.bono@du.edu"
        elif x2 == 's':
            counselorname = "Samantha Zandman"
            counseloremail = "samantha.rutsky@du.edu"
        else:
            print('Name of counselor or Host:')
            counselorname = raw_input().strip()
            print('DU Email of Counselor or (Co)Host:')
            counseloremail = raw_input().strip()
            
        print('Time?')
        apptime = raw_input().strip()
        print('[A]M/[P]M?')
        appampminput = raw_input().strip()
        if appampminput == 'a':
            appampm = 'AM'
        else:
            appampm = 'PM'
        print('Student/Guest Name?')
        studentname = raw_input().strip()
        print('Date?')
        appdate = raw_input().strip()
        
    driver.find_element_by_id("topic").send_keys(studentname+" / "+counselorname)
    
    print('Input date and time (y) when done: '+appdate+' '+apptime+' '+appampm)
    x3 = raw_input()
    if x3 == 'y':
        print('Proceeding . . . ')
    else:
        print('Moving on, keeping todays date')
        
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    
    driver.find_element_by_id("mtg_alternative_host").send_keys(counseloremail)
    driver.find_element_by_css_selector("button.btn-lg").click()
    
    html.send_keys(Keys.HOME)
    
    time.sleep(6)

    try:
        driver.find_element_by_id("copyInvitation").click()
    except:
        time.sleep(5)
        try:
            driver.find_element_by_id("copyInvitation").click()
        except:
            time.sleep(10)
            driver.find_element_by_id("copyInvitation").click()
            
    try:
        time.sleep(3)
        driver.find_element_by_css_selector("#copyInviteDialog > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)").click()
    except:
        time.sleep(15)
        driver.find_element_by_css_selector("#copyInviteDialog > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)").click()
                                          
    print("Appt generated. Another? (y/n)")
    x5 = raw_input()
    if x5 == 'y':
        driver.get("https://udenver.zoom.us/meeting/schedule")
        continue
    else:
        a = 0


driver.quit()

