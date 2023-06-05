import time

from selenium import webdriver
from global_var import *
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
from global_var import *
import os
from datetime import datetime

known_faces_names =  []
folder_dir = path_for_photo_storing
for images in os.listdir(folder_dir):
	if (images.endswith(".jpg")):
         temp_image = os.path.splitext(images)[0]
         known_faces_names.append(temp_image)

current_date_time = datetime.now().strftime("%Y-%m-%d-%I-%M")
var_naming = "Attendance Form for " + current_date_time

def LaunchApp():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))   #changes made
    driver.maximize_window()

def add_option(name):
    driver.find_element(By.XPATH, '//*[@id="SchemaEditor"]/div/div[2]/div/div[2]/div[3]/div/div/div/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div[3]/div[1]/div/span/div/div/div[1]/input').click()
    driver.find_element(By.XPATH, '//*[@id="SchemaEditor"]/div/div[2]/div/div[2]/div[3]/div/div/div/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div[3]/div[1]/div/span/div/div/div[1]/input').send_keys(Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="SchemaEditor"]/div/div[2]/div/div[2]/div[3]/div/div/div/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div[3]/div[1]/div/span/div/div/div[1]/input').send_keys(name)

def another_option1(name):
    x_path = '//*[@id="SchemaEditor"]/div/div[2]/div/div[2]/div[3]/div/div/div/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div/div[2]/input'
    driver.find_element(By.XPATH,x_path).send_keys(name)
    time.sleep(1)

def main_gforms_auto():
    try:
        print("Creating a form ")
        print("Please Wait ...")
        driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S-83668617%3A1682573537518317&continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fu%2F0%2F%3Ftgif%3Dd&followup=https%3A%2F%2Fdocs.google.com%2Fforms%2Fu%2F0%2F%3Ftgif%3Dd&ifkv=AQMjQ7S44iL6wRH9HZZ8xnXOHdVz0wGBmdwBhzrXXrd9IP9-VCFlLQhXzrHPXPq7RXRIHO8n57JxnA&ltmpl=forms&osid=1&passive=1209600&service=wise&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        driver.implicitly_wait(10)

        driver.find_element(By.XPATH,'//*[@id="identifierId"]').click()
        driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(google_user_name)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()
        time.sleep(2.5)
        driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').click()
        driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(google_acc_pass)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id=":1i"]/div[1]').click()
        driver.find_element(By.XPATH, '//*[@id="T2Ybvb0"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="T2Ybvb0"]').clear()
        driver.find_element(By.XPATH, '//*[@id="T2Ybvb0"]').send_keys("Attendance Form")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="tJHJj"]/div[1]/div[1]/div[2]/div[1]/div/div[1]/input').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="tJHJj"]/div[1]/div[1]/div[2]/div[1]/div/div[1]/input').send_keys(var_naming)
        original_window = driver.current_window_handle
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="T2Ybvb2"]').click()
        driver.find_element(By.XPATH, '//*[@id="T2Ybvb2"]').clear()
        driver.find_element(By.XPATH, '//*[@id="T2Ybvb2"]').send_keys("Name")
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[text()='Short answer']").click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, '//*[@id="SchemaEditor"]/div/div[2]/div/div[2]/div[3]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[4]/span').click()
        time.sleep(2)
        add_option(known_faces_names[0])
        time.sleep(2)
        for i in range(1,len(known_faces_names)) :
            another_option1(known_faces_names[i])
            time.sleep(0.7)
        driver.find_element(By.XPATH,'//*[@id="i2"]/div[3]/div').click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//span[@class='NPEfkd RveJvd snByac']").click()
        time.sleep(2)
        '''  uncomment it after 24 hrs as the email exceeded limit
        #driver.find_element(By.XPATH,'//*[@id="email"]/div/div/div[1]/div[3]/div/div[1]/div/div[1]/input').click()
        time.sleep(0.5)
        #driver.find_element(By.XPATH,'//*[@id="email"]/div/div/div[1]/div[3]/div/div[1]/div/div[1]/input').send_keys(admin_email)  #uncomment after 24 hours
        time.sleep(4)
        #driver.find_element(By.XPATH,'//*[@id="email"]/div/div/div[2]/div[2]/div[2]/span/span').click()
        time.sleep(2)
        #driver.find_element(By.XPATH,"//span[@class='NPEfkd RveJvd snByac']").click()
        time.sleep(2)
        '''
        driver.find_element(By.XPATH,'//*[@id="VVcGtd"]/div[1]/div[3]/span/div').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="link"]/div/div/div[2]/div/div/div[1]/div').click()
        time.sleep(2)
        var = driver.find_element(By.XPATH,'//*[@id="link"]/div/div/div[2]/div/div/div[1]/div/div[1]/input').get_attribute("data-initial-value")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="link"]/div/div/div[4]/div[1]/span/span').click() # cancel button
        driver.find_element(By.XPATH, '//*[@id="tJHJj"]/div[1]/div[2]/div/div[8]').click()   # more option
        time.sleep(3)
        driver.find_element(By.XPATH, '/html/body/div[12]/div/div/span[3]').click()  # for cliking prefill option    #check this
        time.sleep(2)

        #chaning tabs
        all_windows = driver.window_handles

        # Loop through the window handles until we find the new window
        for window in all_windows:
            if window != original_window:
                driver.switch_to.window(window)
                break

        # Now we can interact with the new window
        new_window_title = driver.title

        driver.find_element(By.XPATH, '//*[@id="i6"]').click()  # cliking a option        
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div/div/div[3]/div/div/div').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]').click()
        copied_text = pyperclip.paste()   # Output: the copied value
        processinglink = copied_text
        processinglink = processinglink.split("=")[0] + processinglink.split("=")[1] + "="
        processedlink = processinglink.replace("viewform?usppp_url&entry", "formResponse?entry")
        Url_for_google_form = processedlink
        time.sleep(5)
        print("Done")
        driver.minimize_window()
        return Url_for_google_form
    except:
        return "error"

LaunchApp()
Url_for_google_form = main_gforms_auto()