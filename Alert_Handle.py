from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome()
url="https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)
time.sleep(3)

Alert_btn=driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(3) > button")
Alert_btn.click()
time.sleep(3)
alert=driver.switch_to.alert #switches to alert prompt
alert_text=alert.text
time.sleep(3)
print(alert_text)

#writes message to alert prompt
alert.send_keys("this is message")
time.sleep(3)

#accepts the alert
alert.accept()

#dismiss the alert
#alert.dismiss()
time.sleep(5)