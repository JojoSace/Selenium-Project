from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "https://practicetestautomation.com/practice-test-login/"
driver.get(url)
driver.maximize_window()

username = "student"
user_incorrect = "incorrectUser"
password = "Password123"
pass_incorrect = "incorrectPassword"
Expect_Login = "Logged In Successfully"
Expect_User_Invalid = "Your username is invalid!"
Expect_Pass_Invalid = "Your password is invalid!"

#Positive Login test
user_input = driver.find_element(By.XPATH,"//input[@id='username']")
user_input.send_keys(username)
pass_input = driver.find_element(By.XPATH,"//input[@id='password']")
pass_input.send_keys(password)
driver.find_element(By.XPATH,"//button[@id='submit']").click()

Login_success = driver.find_element(By.XPATH,"//h1[normalize-space()='Logged In Successfully']").text
if Expect_Login == Login_success:
    print("The expected text [",Expect_Login,"] is a match!.")
else:
    print("The expected text [", Expect_Login, "] is not a match!, instead [", Login_success,"] is shown.")

#Logout
driver.find_element(By.XPATH,"//a[normalize-space()='Log out']").click()

#Test Case#1 - Negative username test
user_input = driver.find_element(By.XPATH,"//input[@id='username']")
user_input.send_keys(user_incorrect)
pass_input = driver.find_element(By.XPATH,"//input[@id='password']")
pass_input.send_keys(password)
driver.find_element(By.XPATH,"//button[@id='submit']").click()

time.sleep(1)
invalid_user = driver.find_element(By.ID,"error").text
if Expect_Login == Login_success:
    print("The expected text [",Expect_User_Invalid,"] is a match!")
else:
    print("The expected text [", Expect_User_Invalid, "] is not a match!, instead [", invalid_user,"] is shown.")
driver.refresh()

#Test Case#2 - Negative password test
user_input = driver.find_element(By.XPATH,"//input[@id='username']")
user_input.send_keys(username)
pass_input = driver.find_element(By.XPATH,"//input[@id='password']")
pass_input.send_keys(pass_incorrect)
driver.find_element(By.XPATH,"//button[@id='submit']").click()

time.sleep(1)
invalid_pass = driver.find_element(By.ID,"error").text
if Expect_Login == Login_success:
    print("The expected text [",Expect_Pass_Invalid,"] is a match!")
else:
    print("The expected text [", Expect_Pass_Invalid, "] is not a match!, instead [", invalid_pass,"] is shown.")
driver.refresh()

driver.quit()