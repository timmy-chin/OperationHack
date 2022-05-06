from selenium import webdriver
import time
import pyautogui
from Username_ListMaker import OfficialList

browser = webdriver.Chrome('/Users/timmychin/Downloads/chromedriver')

browser.get('https://www.instagram.com/')

time.sleep(3)
login_email = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
login_email.send_keys(input('Enter Username for Instagram'))

Password = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
Password.send_keys(input('Enter Password for Instagram:'))

button = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
button.click()

time.sleep(15)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.instagram.com/direct/new/')

time.sleep(7)

message = "Hello, you may have already noticed, my account timmy_chin_ got hacked. So, if you receive a message about a screenshot from that account, please ignore it :)"

count = 0
for name in OfficialList:           #Send Group Message to 32 People
    searchbox = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/input')
    searchbox.send_keys(name)
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    count += 1

    if count >= 32:
        next = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/div/button')
        next.click()
        time.sleep(13)
        pyautogui.typewrite(message)
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(3)
        browser.get('https://www.instagram.com/direct/new/')
        time.sleep(5)
        count = 0


