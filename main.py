from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

wait_time=3
chrome_opt=webdriver.ChromeOptions()
chrome_opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_opt)
driver.get("https://tinder.com/app/explore")
driver.maximize_window()

#login_btn
time.sleep(wait_time)
driver.find_element(By.XPATH,value='//*[@id="u1469300313"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div').click()

#more
time.sleep(wait_time)
driver.find_element(By.XPATH,value='//*[@id="u1690640749"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/button').click()
#//*[@id="u1690640749"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/button

#cick Fb login
time.sleep(wait_time)
driver.find_element(By.XPATH,value='//*[@id="u1690640749"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div').click()

# change current window from tinder to FB
fb_win=driver.window_handles[1]
driver.switch_to.window(fb_win)
EMAIL=os.environ.get("EMAIL")
PASSWORD=os.environ.get("PASSWORD")
time.sleep(wait_time)
driver.find_element(By.ID,value="email").send_keys(EMAIL)
time.sleep(wait_time)
driver.find_element(By.XPATH,value='//*[@id="pass"]').send_keys(PASSWORD,Keys.ENTER)
#driver.find_element(By.XPATH,value='//*[@id="u_0_0_ZN"]').click()
input("CONFORM HERE ONCE CAPTCHA DONE MANUAlLY : ")
print("CAPTCHA COMPLETED MANUALLY")
print("Code running.......")


tinder=driver.window_handles[0]
driver.switch_to.window(tinder)



driver.find_element(By.XPATH,value='//*[@id="u1690640749"]/div/div/div/div/div[3]/button[1]/div[2]/div[2]').click()
driver.find_element(By.CLASS_NAME,value="lxn9zzn").click()

time.sleep(wait_time*3)
swipe=True
while swipe:
    webdriver.ActionChains(driver).send_keys(Keys.RIGHT).perform()
    time.sleep(1)




