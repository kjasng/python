from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import os


# Specify the path to your Chrome user data directory
user_data_dir = os.path.join(os.getcwd(), "chrome_user_data")  # Create a directory for user data

options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={user_data_dir}")  # Use the specified user data directory

# Initialize your WebDriver with the options
driver = webdriver.Chrome(options=options)

# driver.get("https://access.line.me/oauth2/v2.1/login?returnUri=%2Foauth2%2Fv2.1%2Fauthorize%2Fconsent%3Fbot_prompt%3Dnormal%26client_id%3D1654049937%26code_challenge%3D4GlxiHTRgBSQ1rZmr2Bj-nmw-SKu2CRhuxWeNuhFX_Y%26code_challenge_method%3DS256%26nonce%3D6f3e84c5-ee8e-4cf1-98aa-ff06374a994f%26redirect_uri%3Dhttps%253A%252F%252Fwww.gift-wallet.app%252Foauth%252Fauthorization%26response_type%3Dcode%26scope%3Dopenid%2520profile%26state%3Da5ffeeca-a149-426d-a6d2-574a7c6799e4&loginChannelId=1654049937&loginState=WoQ82jsW8Iu82cDJpkhLuO")


# time.sleep(1000)

# Function to get links from user input
def get_links():
    links = []
    print("Enter links one by one. Type 'done' when finished:")
    while True:
        link = input("Enter link: ")
        if link.lower() == 'done':
            break
        links.append(link)
    return links

# Get the list of links from user input
links = get_links()

# Loop through each link
for link in links:
    driver.get(link)  # Navigate to the current link
    print('Đang chạy link: ', link)
    # Give the page some time to load
    time.sleep(10)

    # Find the button you want to click (replace with the actual selector)
    button = driver.find_element(By.CLASS_NAME, 'PrivateSwitchBase-input')  # Use the appropriate selector
    num_clicks = 1

    # Auto-click loop
    for _ in range(num_clicks):

        button.click()  # Click the button
        time.sleep(3)   # Wait for 1 second between clicks
        button2 = driver.find_element(By.ID, ':r0:')
        button2.click()
        time.sleep(3)   # Wait for 1 second between clicks
        button3 = driver.find_element(By.CLASS_NAME, 'jss53')
        button3.click()
        time.sleep(7)   # Wait for 1 second between clicks
        driver.switch_to.window(driver.window_handles[-1])  # Switch to the last opened tab
        button4 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/section[1]/div/div/div/div[3]/div/div/button')
        button4.click()

        time.sleep(10)


        button5 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div/div[3]/button')
        button5.click()


        time.sleep(10)


driver.quit()