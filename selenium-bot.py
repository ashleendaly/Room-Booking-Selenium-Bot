from selenium import webdriver

uofg = webdriver.Chrome()
uofg.get('https://www.gla.ac.uk/apps/uofglife/#/login')


# --------- Login ------------
guid = uofg.find_element_by_xpath('//*[@id="guid"]')
guid.send_keys('2552805d')

password = uofg.find_element_by_xpath('//*[@id="password"]')
password.send_keys('Ai#Y?v*OL5S3')

login = uofg.find_element_by_xpath('//*[@id="app"]/div[3]/main/button')
login.click()

# --------- Wait For Next Page To Load ------------
uofg.implicitly_wait(5)

# --------- Go To Booking Page ------------
findSpace = uofg.find_element_by_xpath('//*[@id="contain"]/div[9]/ul/li[3]/span')
findSpace.click()

bookable = uofg.find_element_by_xpath('//*[@id="contain"]/div[1]/ul/li[2]')
bookable.click()

# --------- Fill In Booking Form ------------
timeStart = uofg.find_element_by_xpath('//*[@id="startTime"]/option[6]')
timeStart.click()

timeEnd = uofg.find_element_by_xpath('//*[@id="endTime"]/option[12]')
timeEnd.click()

