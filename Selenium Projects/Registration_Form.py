from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
url = "https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php"
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)
time.sleep(2)

#Enter Full Name
prefix = Select(driver.find_element(By.ID,"prefix"))
prefix.select_by_visible_text("Mr.")
first_name = driver.find_element(By.ID,"firstname")
first_name.send_keys("John")
last_name = driver.find_element(By.ID,"lastname")
last_name.send_keys("Doe")
time.sleep(1)

#Select Account Type
pension = driver.find_element(By.ID,"pension")
pension.click()
time.sleep(1)

#Enter Father's Name & Mother's Name
father_name = driver.find_element(By.NAME,"fathername")
father_name.send_keys("Jonathan Doe")
mother_name = driver.find_element(By.NAME,"mothername")
mother_name.send_keys("Jane Doe")
time.sleep(1)

#Select ID Type
student_id = driver.find_element(By.XPATH,"//input[@id='studentid']")
action.scroll_to_element(student_id).perform()
student_id.click()
time.sleep(1)

#Enter ID Number
id_num = driver.find_element(By.ID,"identity_number")
id_num.send_keys("987654321")
time.sleep(1)

#Enter Gender
other = driver.find_element(By.ID,"other")
action.scroll_to_element(other).perform()
other.click()
time.sleep(1)

#Enter Date of Birth
month = Select(driver.find_element(By.ID,"dob_month"))
month.select_by_visible_text("August")
day = Select(driver.find_element(By.ID,"dob_date"))
day.select_by_visible_text("18")
year = Select(driver.find_element(By.ID,"dob_year"))
year.select_by_visible_text("1927")
time.sleep(1)

#Enter Marital Status
married = driver.find_element(By.ID,"married")
action.scroll_to_element(married).perform()
married.click()
time.sleep(1)

#Enter Mobile
country_code = Select(driver.find_element(By.ID,"country_code"))
country_code.select_by_visible_text("Philippines (+63)")
mobile_num = driver.find_element(By.ID,"mobile")
mobile_num.send_keys("912345678")
time.sleep(1)

#Enter Nationality
nationality = Select(driver.find_element(By.NAME,"nationality"))
nationality.select_by_visible_text("Filipino")
time.sleep(1)

#Enter Address
address = driver.find_element(By.NAME,"address")
address.send_keys("EDSA cor. West Avenue")
state = driver.find_element(By.ID,"state")
state.send_keys("NCR")
time.sleep(1)

#Enter Country
country = Select(driver.find_element(By.NAME,"country"))
country.select_by_visible_text("Philippines")
time.sleep(1)

#Submit
driver.find_element(By.XPATH,"//input[@value='Submit']").click()
time.sleep(1)

driver.quit()