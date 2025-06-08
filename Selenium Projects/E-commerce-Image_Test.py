from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

chrome_options=Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
url = "https://www.saucedemo.com/"
driver.get(url)
driver.maximize_window()
time.sleep(1)

username_list = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]
pass_all = "secret_sauce"
item_list = ["backpack", "shirt", "onesie", "bike-light", "pullover", "red-tatt"]

#Test Login using multiple usernames
for username in username_list:
    user_input = driver.find_element(By.CSS_SELECTOR, "#user-name")
    user_input.send_keys(username)
    #time.sleep(1)
    pass_input = driver.find_element(By.CSS_SELECTOR, "#password")
    pass_input.send_keys(pass_all)
    #time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    #time.sleep(2)
    if driver.current_url == "https://www.saucedemo.com/inventory.html":
        print("-----", username, "CAN LOGIN-----")
#Verify if displayed image is correct
        for item in item_list:
            backpack_img = driver.find_element(By.CSS_SELECTOR, "img[alt='Sauce Labs Backpack']").get_attribute("src")
            shirt_img = driver.find_element(By.CSS_SELECTOR, "img[alt='Sauce Labs Bolt T-Shirt']").get_attribute("src")
            onesie_img = driver.find_element(By.CSS_SELECTOR, "img[alt='Sauce Labs Onesie']").get_attribute("src")
            bike_light_img = driver.find_element(By.CSS_SELECTOR, "img[alt='Sauce Labs Bike Light']").get_attribute("src")
            pullover_img = driver.find_element(By.CSS_SELECTOR, "img[alt='Sauce Labs Fleece Jacket']").get_attribute("src")
            red_tatt_img = driver.find_element(By.CSS_SELECTOR,"img[alt='Test.allTheThings() T-Shirt (Red)']").get_attribute("src")
            if item in backpack_img:
                print(item, "image is CORRECT")
            elif item in shirt_img:
                print(item, "image is CORRECT")
            elif item in onesie_img:
                print(item, "image is CORRECT")
            elif item in bike_light_img:
                print(item, "image is CORRECT")
            elif item in pullover_img:
                print(item, "image is CORRECT")
            elif item in red_tatt_img:
                print(item, "image is CORRECT")
            else:
                print("[ [ [ [ [", item, "image is INCORRECT ] ] ] ] ]")
        driver.get(url)
    else:
        print("[ [ [ [ [", username, "CANNOT LOGIN ] ] ] ] ]")
        print("[ [ [ [ [ images CANNOT be tested ] ] ] ] ]")
        driver.get(url)