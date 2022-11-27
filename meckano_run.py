from selenium import webdriver
import yaml
import time
from selenium.webdriver.support.ui import WebDriverWait
import random
from selenium.webdriver.common.by import By
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

def main():
    with open(r'C:/Nir/meckano_auto/config.yaml') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)

    option = webdriver.ChromeOptions()
    # I use the following options as my machine is a window subsystem linux.
    # I recommend to use the headless option at least, out of the 3
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-sh-usage')
    option.add_argument('--disable-notifications')
    # Replace YOUR-PATH-TO-CHROMEDRIVER with your chromedriver location
    driver = webdriver.Chrome(executable_path = r'C:/Nir/meckano_auto/chromedriver.exe', options=option)

    driver.get('https://app.meckano.co.il/login.php#login') # Getting page HTML through request
    wait=WebDriverWait(driver,30)
    driver.maximize_window()
    driver.find_element(By.ID, "email").send_keys(cfg['email'])
    driver.find_element(By.ID, "password").send_keys(cfg['password'])
    driver.find_element(By.ID, "submitButtons").click()

    time.sleep(6)
    driver.find_element(By.CLASS_NAME, "wrapperCheckout").click()
    time.sleep(4)
    print('meckano activated')

if __name__ == "__main__":
    print('meckano started')
    randint = random.randint(60, 60*60)
    print('meckano will run after ' + str(randint/60) + ' seconds')
    time.sleep(randint) #inclucive
    main()
