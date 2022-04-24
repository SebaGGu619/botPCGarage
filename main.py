import requests
from selenium import webdriver
from time import *
from bs4 import BeautifulSoup
import datetime
import random
import time as timpDelay
from plyer import notification

# WARNING
# If ACTIVAT = True the code will buy the video card, it wont stop at warning only.

ACTIVAT = False

fisier = open('urls.txt', 'r')
urls = fisier.readlines()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.82 Safari/537.36 '
}

systemTimeMilli = time() * 1000
systemTimeTarget = systemTimeMilli

exitLoop = False

while not exitLoop:
    systemTimeMilli = time() * 1000
    if systemTimeMilli > systemTimeTarget:
        nextTime = random.randint(0, 1)
        systemTimeTarget = systemTimeMilli + nextTime * 1000
        # print('             Next check in: ' + str(nextTime))

        for i in range(len(urls)):
            timpDeAsteptat = random.randint(0, 20)
            print('----------' + str(datetime.datetime.now()) + '---------- ' + str(timpDeAsteptat))
            timpDelay.sleep(timpDeAsteptat)

            url = urls[i]
            url = url[:-1]

            x = requests.get(url, headers=headers)
            pagina = BeautifulSoup(x.content, 'html.parser')

            if 'Nu este in stoc' in pagina.text:
                print("Checked: " + str(url))
                print("  " + str(x.status_code))
            else:
                print('STOC STOC STOC STOC STOC | ' + str(url) + ' | ' + str(x.status_code))
                notification.notify(
                    title="BUYING BUYING BUYING",
                    message=str(i+1),
                    timeout=15
                )
                exitLoop = True
                break
        if exitLoop:
            break
        # print("         ----------restart----------")
    # print("          Checking in: " + str(round((systemTimeTarget - systemTimeMilli) / 1000)) + " Seconds")
    if systemTimeTarget - systemTimeMilli < 5000:
        timpDelay.sleep(1)
    else:
        timpDelay.sleep(3)
timpDelay.sleep(3)

browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_id("cookie_agree").click()
browser.find_element_by_class_name("btn-md").click()

browser.find_element_by_id("lastname").send_keys("---")  # last name
browser.find_element_by_id("firstname").send_keys("---")  # first name

browser.execute_script("window.scrollTo(0, 1000);")

browser.find_element_by_xpath("//select[@name='delivery_state']/option[text()='---']").click()  # county

browser.find_element_by_name("delivery_city").click()
timpDelay.sleep(5)
browser.find_element_by_xpath("//select[@name='delivery_city']/option[text()='---']").click()  # city
browser.find_element_by_name("delivery_city").click()

browser.find_element_by_name("delivery_address").send_keys("---")  # address
browser.find_element_by_name("delivery_zipcode").send_keys("---")  # zipcode

browser.execute_script("window.scrollTo(0, 1400);")

browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div['
                              '2]/form/div/div/div[4]/div/div[17]/div/label/span').click()

browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div['
                              '2]/form/div/div/div[6]/div/p[3]/input').send_keys("---")  # phone number

browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div['
                              '2]/form/div/div/div[6]/div/p[4]/input').send_keys("---")  # emai

browser.execute_script("window.scrollTo(0, 1400);")

browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div['
                              '2]/form/div/div/div[8]/div/div[2]/label/span').click()

browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div['
                              '2]/form/div/div/div[11]/div/label/span').click()

if ACTIVAT:
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div['
                                  '2]/form/div/div/div[12]/button').click()
