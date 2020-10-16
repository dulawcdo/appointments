from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import subprocess
import pyperclip

def screenclear():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')


driver = webdriver.Firefox()
driver.get("https://udenver.zoom.us/meeting/schedule")

time.sleep(5)

try:
    driver.find_element_by_id("username").send_keys("zeeshan.reshamwala@du.edu")
except:
    time.sleep(4)
    driver.find_element_by_id("username").send_keys("zeeshan.reshamwala@du.edu")

driver.find_element_by_id("password").send_keys("Zmn76642Denver")
driver.find_element_by_css_selector("button.form-element").click()

def counselor_link_details():

    # Format Time
    
    p = subprocess.Popen(["date", "+%-I:%M", "-d", apptime], stdout=subprocess.PIPE)
    out, err = p.communicate()
    timeentry = out.strip()


    # Format Date

    p = subprocess.Popen(["date", "+%B %-d", "-d", appdate], stdout=subprocess.PIPE)
    out, err = p.communicate()
    dateentry = out.strip()

    print('Counselor has personal recurring link.')
    open('/home/zeeshanr/Documents/python/appointments/recurdata.txt', 'w').close()
    f = open("/home/zeeshanr/Documents/python/appointments/recurdata.txt", "a+")
    f.write("Topic: "+studentname+" / "+counselorname+"\n")
    f.write("Time: "+dateentry+", "+timeentry+" "+appampm+" Mountain Time (US and Canada)"+"\n")
    f.write("\n")
    f.write("Join from PC, Mac, Linux, iOS or Android: "+counselorlink+"\n")
    
    with open('/home/zeeshanr/Documents/python/appointments/recurdata.txt', 'r') as f:
        print(f.read())
    
    fo = open('/home/zeeshanr/Documents/python/appointments/recurdata.txt', 'r').read()
    pyperclip.copy(fo)
    print('Successfully copied to clipboard')
    f.close()

    
a = 1

while a == 1:
    
    print("Input method? [a]Appt request / [m]Manual")
    x = raw_input()
    
    # USING APPOINTMENT DETAILS pulled from email via emacs function send-appt-to-shell()
    
    
    if x == 'a':
        with open('/home/zeeshanr/Documents/python/appointments/rawappt.txt') as f:
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
        
    if counselorname == 'Eric Bono':
        counselorlink='https://udenver.zoom.us/j/84897750395'
        counselor_link_details()
        
    else:
        
        driver.find_element_by_id("topic").send_keys(studentname+" / "+counselorname)

        # Enter date

    
        driver.execute_script("document.getElementById('start_date').removeAttribute('readonly',0);")


        p = subprocess.Popen(["date", "+%m/%d/%Y", "-d", appdate], stdout=subprocess.PIPE)
        out, err = p.communicate()
        print(out)

        startdate = driver.find_element_by_id('start_date')
        startdate.click()
        startdate.clear()
        startdate.send_keys(out)

        # Enter Time

        p = subprocess.Popen(["date", "+%-I:%M", "-d", apptime], stdout=subprocess.PIPE)
        out, err = p.communicate()
        timeentry = out.strip()
        timehour, timeminute = timeentry.split(":")
        print(timeentry)
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div[5]/form/div[2]/div[1]/div[1]/div/div[1]/div').click()
        if timehour == '2':
            driver.find_element_by_class_name('zm-select-input__inner').send_keys(timeentry)
            driver.find_element_by_class_name('zm-select-input__inner').send_keys(Keys.DOWN)
            driver.find_element_by_class_name('zm-select-input__inner').send_keys(Keys.ENTER)
        else:
            driver.find_element_by_class_name('zm-select-input__inner').send_keys(timeentry)
            driver.find_element_by_class_name('zm-select-input__inner').send_keys(Keys.ENTER)

        # Automated AMPM
    
        time.sleep(1)
        p = subprocess.Popen(["date", "+%-H*60", "-d", apptime], stdout=subprocess.PIPE)
        resulting, err = p.communicate()
        resulting=resulting.strip()
        resulting=eval(resulting)
        print(int(resulting))

        driver.find_element_by_xpath('//*[@id="start_time_2"]').click()
        if resulting < 540:
            driver.find_element_by_id('select-item-start_time_2-1').click()
            # driver.find_element_by_xpath('//*[@id="select-item-start_time_2-1"]')
        elif resulting > 660:
            driver.find_element_by_id('select-item-start_time_2-1').click()
        else:
            driver.find_element_by_id('select-item-start_time_2-0').click()




            #        if resulting > 720:
            #        driver.find_element_by_id('select-item-start_time_2-1').click()
            #    else:
            #        driver.find_element_by_id('select-item-start_time_2-0').click()

        print('Check date and time; (y) when done: '+appdate+' '+apptime+' '+appampm)
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
        screenclear()
        continue
    else:
        a = 0


driver.quit()
exit()
