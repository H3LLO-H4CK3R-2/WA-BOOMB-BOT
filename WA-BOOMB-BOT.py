from selenium import webdriver
import time
# ENTER YOUR DRIVER PATH HERE
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
# LINK
driver.get("https://web.whatsapp.com/")
# SCAN THE QRCODE THEN
# COME TO TERMINAL TO INPUT name,msg,count,tim

# printing name and color
print('\033[31m')
print("WA-BOOMB-BOT Login")
print(" ")
# input things
name = input("ENTER BOOMBER NAME : ") # ENTER THE NAME WHO WANT TO BOOMB
msg = input("ENTER YOUR MESSAGE HERE : ")# ENTER THE MESSAGE YOU WANT TO SEND
count = eval(input("HOW MANY MESSAGE DO YOU WANT : "))# ENTER THE COUN YOU WANT TO SEND
tim = eval(input("ENTER YOUR TIME : ")) # USE A TIME MATCHING WITH COUNT ORWISE THE CODE WILL BREAK
# finding input name
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
# sending messages
msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
# for loop for sending messages
for i in range(count):
    msgBox.send_keys(msg)
    sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
    sendButton.click()
# logout
time.sleep(tim) # inputing tim ( time for sleep )
dot = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div/span')
dot.click()
logout = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[7]/div')
logout.click()
# exit
time.sleep(3)
driver.quit()
