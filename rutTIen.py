from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import threading
from queue import Queue
from datetime import datetime, timedelta


# Specify the path to your Chrome user data directory
base_user_data_dir = os.path.join(os.getcwd(), "chrome_user_data")  # Base directory for user data

# Create the base directory if it doesn't exist
if not os.path.exists(base_user_data_dir):
    os.makedirs(base_user_data_dir)


def get_links():
    links = []
    print("Enter links one by one. Type 'done' when finished:")
    while True:
        link = input("Enter link: ")
        if link.lower() == 'done':
            break
        links.append(link)
    return links

def get_thread_count():
    while True:
        try:
            thread_count = int(input("Enter number of threads to run (1-10): "))
            if 1 <= thread_count <= 10:
                return thread_count
            print("Please enter a number between 1 and 10")
        except ValueError:
            print("Please enter a valid number")

def get_line_credentials():
    username = 'fishbu7k@gmail.com'
    password = 'Hoilamgi1@'
    return username, password

def process_link(link, thread_id, line_username, line_password):
    # Use only 3 profiles in rotation
    profile_id = thread_id % 3  # This will rotate between 0, 1, 2
    
    options = webdriver.ChromeOptions()
    
    # Set window size and position
    window_width = 480
    window_height = 800
    options.add_argument(f"--window-size={window_width},{window_height}")
    
    # Use one of three fixed profiles
    user_data_dir = f"E:/qtd/python/chrome_user_data/profile_{profile_id}"
    options.add_argument(f"--user-data-dir={user_data_dir}")
    
    # Basic required options
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_argument(f"--remote-debugging-port={9222 + profile_id}")
    
    driver = None
    try:
        driver = webdriver.Chrome(options=options)
        
        # Position window based on profile_id (not thread_id)
        x_position = profile_id * window_width
        driver.set_window_position(x_position, 0)
        
        driver.get(link)
        print(f'Thread {thread_id} running link: {link}')
        time.sleep(10)

        # Find and click buttons
        button = driver.find_element(By.CLASS_NAME, 'PrivateSwitchBase-input')
        button.click()
        time.sleep(3)
        
        button2 = driver.find_element(By.ID, ':r0:')
        button2.click()
        time.sleep(3)
        
        button3 = driver.find_element(By.CLASS_NAME, 'jss53')
        button3.click()
        time.sleep(5)
        
        driver.switch_to.window(driver.window_handles[-1])
        button4 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/section[1]/div/div/div[3]/div/div/div[2]/button')
        button4.click()
        time.sleep(5)

        # Switch to Line login window and handle login
        driver.switch_to.window(driver.window_handles[-1])
        
        # # Input username/email
        # username_field = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/form/fieldset/div[1]/input')
        # username_field.send_keys(line_username)
        # time.sleep(2)

        # # Input password
        # password_field = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/form/fieldset/div[2]/input')
        # password_field.send_keys(line_password)
        # time.sleep(2)

        # # Click login button
        # login_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/form/fieldset/div[3]/button')
        # login_button.click()
        # time.sleep(10)

        button5 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div/div[3]/button')
        button5.click()
        time.sleep(15)
    
    except Exception as e:
        print(f"Error in thread {thread_id}: {str(e)}")
    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass

# Modify the main execution part
if __name__ == "__main__":
    # Create only 3 profile directories
    for i in range(3):
        profile_path = f"E:/qtd/python/chrome_user_data/profile_{i}"
        if not os.path.exists(profile_path):
            os.makedirs(profile_path)
    
    max_threads = get_thread_count()
    links = get_links()
    line_username, line_password = get_line_credentials()
    
    # Create and start threads
    threads = []
    active_threads = 0

    for thread_id, link in enumerate(links):
        # Wait if we've reached max threads
        while active_threads >= max_threads:
            threads = [t for t in threads if t.is_alive()]
            active_threads = len(threads)
            time.sleep(2)
        
        time.sleep(5)  # Wait between starting threads
        
        thread = threading.Thread(target=process_link, args=(link, thread_id, line_username, line_password))
        thread.start()
        threads.append(thread)
        active_threads += 1

    # Wait for all threads to complete
    for thread in threads:
        thread.join()