# selenium-related
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from webdriver_manager.chrome import ChromeDriverManager

# other necessary ones
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import time
import re
from oauth2client.service_account import ServiceAccountCredentials
import gspread

def sheets_connection():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/spreadsheets']

    #Generate a json file by using service account auth in google developer console
    '''
    Link: https://console.developers.google.com/
    1) Enable API Access for a Project if you haven’t done it yet.
    2) Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.
    3) Fill out the form
    4) Click “Create” and “Done”.
    5) Press “Manage service accounts” above Service Accounts.
    6) Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY > Create new key”.
    7) Select JSON key type and press “Create”.
    8) Go to the google sheet and share the sheet with the email from service accounts.
    '''

    creds = ServiceAccountCredentials.from_json_keyfile_name(r'figures/lunar-tube-373814-cffbcc3ccf54.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1XIfCgUnM0WOkenUCVeRGZHSeeTPQPSS_pMvDd-Wh3Ng")
    worksheet = sheet.worksheet('Automation')
    data = worksheet.get_all_values()
    # to df
    data = pd.DataFrame(data[1:], columns=data[0])
    return data, worksheet

def scape_to_data(data,link,phone,name,location):
    # if link in data column links
    if data['Links'].isin([link]).any() or data['Phone'].isin([phone]).any() or data['Name'].isin([name]).any() or data['Location'].isin([location]).any():
        print(f'{link}, {phone}, {name}, {location} ALREADY in data!')
        return data
    else:
        data = pd.concat([data, pd.DataFrame([{'Links': link, 'Phone': phone, 'Name': name, 'Location': location}])], ignore_index=True)
        print(f'{link}, {phone}, {name}, {location} added!')
    return data

def openComment(browser):
    moreComment = browser.find_elements(By.XPATH, "//span[contains(@class,'d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v lrazzd5p m9osqain') and starts-with(text(), 'View') and contains(text(), 'more comment')]")
    if len(moreComment) > 0:
        count = 0
        for i in moreComment:
            action=ActionChains(browser)
            try:
                action.move_to_element(i).click().perform()
                count += 1
            except:
                try:
                    browser.execute_script("arguments[0].click();", i)
                    count += 1
                except:
                    continue
        if len(moreComment) - count > 0:
            print('moreComment issue:', len(moreComment) - count)
        time.sleep(1)
    else:
        pass


def openReply(browser):
    replies = browser.find_elements(By.XPATH, "//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t pfnyh3mw d2edcug0 hpfvmrgz n8tt0mok hyh9befq r8blr3vg jwdofwj8 g0qnabr5']")
    if len(replies) > 0:
        count = 0
        for i in replies:
            action=ActionChains(browser)
            try:
                action.move_to_element(i).click().perform()
                count += 1
            except:
                try:
                    browser.execute_script("arguments[0].click();", i)
                    count += 1
                except:
                    continue
        if len(replies) - count > 0:
            print('replies issue:', len(replies) - count)
        time.sleep(1)
    else:
        pass


def openReply2(browser):
    replies = browser.find_elements(By.XPATH, "//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v lrazzd5p m9osqain' and contains(text(),'more repl')]")
    if len(replies) > 0:
        count = 0
        for i in replies:
            action=ActionChains(browser)
            try:
                action.move_to_element(i).click().perform()
                count += 1
            except:
                try:
                    browser.execute_script("arguments[0].click();", i)
                    count += 1
                except:
                    continue
        if len(replies) - count > 0:
            print('replies2 issue:', len(replies) - count)
        time.sleep(1)
    else:
        pass


def openSeeMore(browser):
    readMore = browser.find_elements(By.XPATH, "//div[contains(@class,'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p') and contains(text(), 'See More')]")
    if len(readMore) > 0:
        count = 0
        for i in readMore:
            action=ActionChains(browser)
            try:
                action.move_to_element(i).click().perform()
                count += 1
            except:
                try:
                    browser.execute_script("arguments[0].click();", i)
                    count += 1
                except:
                    continue
        if len(readMore) - count > 0:
            print('readMore issue:', len(readMore) - count)
        time.sleep(1)
    else:
        pass

def getBack(browser):
    if not browser.current_url.endswith('reviews'):
        print('redirected!!!')
        browser.back()
        print('got back!!!')

def archiveAtEnd(browser, reviewList):
    browser.execute_script("window.scrollTo(0, -document.body.scrollHeight);") # scroll back to the top
    time.sleep(10)

    for idx, l in enumerate(reviewList):
        if idx % 10 == 0:
            if idx < 15:
                browser.execute_script("arguments[0].scrollIntoView();", reviewList[0])
            else:
                browser.execute_script("arguments[0].scrollIntoView();", reviewList[idx-15])

            time.sleep(1)
            try:
                browser.execute_script("arguments[0].scrollIntoView();", reviewList[idx+15])
            except:
                browser.execute_script("arguments[0].scrollIntoView();", reviewList[-1])

            time.sleep(1)
            browser.execute_script("arguments[0].scrollIntoView();", reviewList[idx])

            for r in range(2):
                time.sleep(3)
                try:
                    browser.execute_script("arguments[0].scrollIntoView();", reviewList[idx+5])
                    time.sleep(3)
                except:
                    browser.execute_script("arguments[0].scrollIntoView();", reviewList[-1])
                browser.execute_script("arguments[0].scrollIntoView();", reviewList[idx+r*3])
                time.sleep(3)
                with open(f'./PATH/{str(idx)}_{r}.html',"w", encoding="utf-8") as file:
                    source_data = browser.page_source
                    bs_data = bs(source_data, 'html.parser')
                    file.write(str(bs_data.prettify()))
                    print(f'written: {idx}_{r}')



# set options as you wish
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument('--disable-notifications')
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})
prefs = {"protocol_handler": {"excluded_schemes": {"<INSERT PROTOCOL NAME>": "false"}}}
option.add_experimental_option("prefs", prefs)
from selenium.webdriver.chrome.service import Service

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)

# browser = webdriver.Chrome(executable_path = r'chromedriver.exe', options=option)#, options=option)

def numbers_from_web(url):
    browser.get(url)
    wait = WebDriverWait(browser, 30)
    # get all text in the page
    text = browser.find_element(By.XPATH,"//*").text
    # look for numbers in the text and save them in a list
    all_numbers = re.findall(r'\d{10,12}', text)
    # extend to numbers in pattern XXX-XXXXXXX
    all_numbers.extend(re.findall(r'\d{3}-\d{7}', text))
    # remove duplicates
    res = [*set(all_numbers)]
    txt_file = f"{url.split('.')[1]}.txt"
    # clean with open("filename.txt", "r+") as file:
    with open(txt_file, "w") as file:
        file.write('')
    # write numbers to txt file
    for number in res:
        if number[:3]=='972' and len(number)==12:
            write_num_to_txt(number, txt_file)
            continue
        elif number[0]=='0' and len(number)==10:
            number = number[2:]
            number = '9725' + number
            write_num_to_txt(number, txt_file)
        # if number is XXX-XXXXXXX
        elif number[3]=='-' and len(number)==11:
            number = number.replace('-','')
            number = number[1:]
            number = '972' + number
            write_num_to_txt(number, txt_file)



import yaml
def fb_run(url):
    # read yaml cred.yaml
    with open('cred.yaml') as f:
        cred = yaml.load(f, Loader=yaml.FullLoader)
    browser.get("https://www.facebook.com")
    browser.maximize_window()
    wait = WebDriverWait(browser, 30)
    email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
    email_field.send_keys(cred['EMAIL'])
    pass_field = wait.until(EC.visibility_of_element_located((By.NAME, 'pass')))
    pass_field.send_keys(cred['PASSWORD'])
    pass_field.send_keys(Keys.RETURN)

    time.sleep(5)

    browser.get(url)

    time.sleep(5)

    from selenium.webdriver.common.action_chains import ActionChains

    Bool_try = True
    numbers = []
    for i in range(10):
        print(f' i = {i}')
        for run in range(4):
            print(f'run: {run+i}')
            try:
                xpath_ele = "//span[contains(text(),'View') and contains(text(),'more comment')]"
                # get all elements with the xpath
                elements = browser.find_elements(By.XPATH, xpath_ele)
                # click the last element
                elements[-1].click()
                # link = browser.find_element(By.XPATH,xpath_ele).click() # find the link
            except:
                pass
            browser.implicitly_wait(3)
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            link = browser.find_element(By.XPATH,"//*").text
            all_numbers = re.findall(r'\d{10,12}', link)
            numbers.extend(all_numbers)
            try:
                # close post
                element = browser.find_element(By.XPATH, '//*[contains(@d, "M18.707")]')
                element.click()
            except:
                pass
            browser.implicitly_wait(5)
            link = browser.find_element(By.XPATH,"//*").text
            if link:
                all_numbers = re.findall(r'\d{10,12}', link)
                numbers.extend(all_numbers)

    res = [*set(numbers)]
    print("List after removing duplicate elements: ", res)
    # clean with open("filename.txt", "r+") as file:
    with open("filename.txt", "w") as file:
        pass
    for number in numbers:
        num_to_txt(number)


def phone_to_num(number2):
    # with re get only numbers
    number = re.sub("[^0-9]", "", number2)
    if number == '':
        return
    if number[:3]=='972' and len(number)==12:
        pass
    elif number[0]=='0' and len(number)==10:
        number = number[2:]
        number = '9725' + number
    elif number[3]=='-' and len(number)==11:
        number = number.replace('-','')
        number = number[1:]
        number = '972' + number
    return number

def num_to_txt(number2):
    # with re get only numbers
    number = re.sub("[^0-9]", "", number2)
    if number == '':
        return
    if number[:3]=='972' and len(number)==12:
        write_num_to_txt(number)
    elif number[0]=='0' and len(number)==10:
        number = number[2:]
        number = '9725' + number
        write_num_to_txt(number)
    elif number[3]=='-' and len(number)==11:
        number = number.replace('-','')
        number = number[1:]
        number = '972' + number
        write_num_to_txt(number)

def read_txt_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def write_num_to_txt(number, file_path='filename.txt'):
    with open(file_path, "r+") as file:
        for line in file:
            if number in line:
                break
        else: # not found, we are at the eof
            file.write(number + '\n') # append missing data

def click_pyautogui(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()


def send_whatsapp(all_numbers):
    all_numbers = all_numbers.split('\n')[:-1]
    message = """היי, מה קורה? אנחנו מחפשים גן אירועים לחתונה של 100-150 מוזמנים במאי 2025. נשמח לקבל הצעת מחיר לאירוע ביום חול, בחמישי ערב ובשישי ערב. תודה רבה"""
    for index, number in enumerate(all_numbers):
        # run twice
        for i in range(2):
        # Goes to site
            site = f"https://wa.me/{number}?text={message}"
            browser.get(site)
            if index == 0 and i == 0:
                click_pyautogui(732 , 165)
                time.sleep(2)
                click_pyautogui(1025 , 225)
            try:
                browser.find_element(By.XPATH,"//span[contains(text(),'Continue to Chat')]").click()
            except:
                pass
        time.sleep(5)
        # Clicks on the button to send message
        click_pyautogui(1880 , 1000)
        time.sleep(1)
        # remove number from filename.txt
        with open("filename.txt", "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if number not in line:
                    file.write(line)
            file.truncate()

def update_google_sheets(data, worksheet):
    # data['Id'] = data.index
    data['Id'] = data.index + 1
    # write data to google sheets
    import numpy as np
    # Replace non-compliant float values
    data2 = data.replace([np.inf, -np.inf], np.nan)
    data2 = data2.fillna(0)  # or any other value that makes sense in your context
    # Now try to update the worksheet
    worksheet.update([data2.columns.values.tolist()] + data2.values.tolist())

def wedding_venues_10comm():
    mother_link = "https://10comm.com/places.php?cat=2&area=center"
    browser.get(mother_link)
    # browser.maximize_window()
    wait = WebDriverWait(browser, 10)
    numbers = []
    # get all links in list
    links = browser.find_elements(By.TAG_NAME, 'a')
    # links to list
    links2 = []
    # Convert links to a list
    for link in links:
        links2.append(link.get_attribute('href'))
    # remove duplicates
    links2 = list(set(links2))
    data,worksheet = sheets_connection()
    # go to each link in list
    for link in links2:
        # browser get link in new tab
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[1])
        browser.get(link)
        phone = ''
        try:
            try:
                # get phone by string regex 05x-xxxxxxx
                phone = re.findall(r'05\d-[0-9]{7}', browser.page_source)[0]
            except:
                pass
                # #click on 640 150
                # click_pyautogui(640, 150)
            # phone = phone_to_num(phone)
            if phone == '':
                continue
            print(f'Phone found : {phone}')
            # get first h1 element
            wait.until(EC.visibility_of_element_located((By.ID, 'topBar_left_businessShourtName')))
            h1_element = browser.find_element(By.ID, 'topBar_left_businessShourtName')
            name = h1_element.text
            # find link that contains "waze" in href
            location = browser.find_element(By.CLASS_NAME,"topBar_left_address_moreDetails_row")
            location = location.text
            # remove כתובת if exists
            location = re.sub(r'כתובת', '', location)
            data = scape_to_data(data,link,phone,name,location)
            time.sleep(2)
        except:
            time.sleep(2)
            pass
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
    update_google_sheets(data,worksheet)

def wedding_venues_urbanbridesmag():
    mother_link = "https://urbanbridesmag.co.il/%D7%9E%D7%A7%D7%95%D7%9D-%D7%9C%D7%90%D7%99%D7%A8%D7%95%D7%A2.html"
    browser.get(mother_link)
    # browser.maximize_window()
    wait = WebDriverWait(browser, 10)
    numbers = []
    # get all links in list
    links = browser.find_elements(By.TAG_NAME, 'a')
    # links to list
    links2 = []
    # Convert links to a list
    for link in links:
        links2.append(link.get_attribute('href'))
    # remove duplicates
    links2 = list(set(links2))
    data,worksheet = sheets_connection()
    # go to each link in list
    for link in links2:
        # browser get link in new tab
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[1])
        browser.get(link)
        phone = ''
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "phone")))
            # get phone by class
            phone = browser.find_element(By.CLASS_NAME, "phone").text
            phone = phone_to_num(phone)
            numbers.append(phone)
            print(f'Phone found : {phone}')
            # get first h1 element
            h1_element = browser.find_element(By.TAG_NAME, 'h1')
            name = h1_element.text
            # find link that contains "waze" in href
            location = browser.find_element(By.XPATH, "//a[contains(@href, 'waze')]")
            location = location.text
            # remove כתובת if exists
            location = re.sub(r'כתובת', '', location)
            data = scape_to_data(data,link,phone,name,location)
        except:
            pass
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
    update_google_sheets(data,worksheet)

def test_phone_num_online(number):
    browser.get('https://2chat.co/tools/whatsapp-checker')
    # find id :R6jajal6dak6:
    element = browser.find_element(By.ID, ':R6jajal6dak6:')
    from selenium.webdriver.common.keys import Keys
    # Get the length of the input field's content
    length = len(element.get_attribute('value'))
    # Send backspace keys equal to the length of the input field's content
    for _ in range(length):
        element.send_keys(Keys.BACKSPACE)
    # send number
    element.send_keys(number)
    button = browser.find_element(By.ID, ':R2lajal6dak6:').click()
    time.sleep(8)
    if 'This number is on NOT WhatsApp' in browser.page_source:
        return False
    return True


def send_whatsapp_sheets():
    data,worksheet = sheets_connection()
    message = """היי, מה קורה? אנחנו מחפשים גן אירועים לחתונה של 100-150 מוזמנים במאי 2025. נשמח לקבל הצעת מחיר לאירוע ביום חול, בחמישי ערב ובשישי ערב. תודה רבה"""
    bool_first = True
    # run over data rows
    for index, row in data.iterrows():
        if '10comm' not in row['Links']:
            continue
        if row['Phone'][:2] != '05':
            continue
        # get phone number from row
        number = phone_to_num(row['Phone'])
        # check if number has whatsapp
        # run twice
        for i in range(1):
            # Goes to site
            site = f"https://wa.me/{number}?text={message} {row['Links']}"
            browser.get(site)
            if bool_first:
                click_pyautogui(732 , 165)
                time.sleep(2)
                click_pyautogui(1025 , 225)
                bool_first = False
            try:
                browser.find_element(By.XPATH,"//span[contains(text(),'Continue to Chat')]").click()
            except:
                pass
        time.sleep(5)
        for i in range(2):
            click_pyautogui(1330 ,530)
        # click on 1052 555 twice
        for i in range(2):
            click_pyautogui(1052, 555)
            time.sleep(1)
        # Clicks on the button to send message
        click_pyautogui(1880 , 1000)
        time.sleep(1)
    pass

import re

if __name__ == '__main__':
    # wedding_venues_10comm()
    # wedding_venues_urbanbridesmag()
    # fb_run('https://www.facebook.com/groups/420825184963260/?hoisted_section_header_type=recently_seen&multi_permalinks=2081779185534510')
    # url = 'https://www.pro.co.il/pest-control/tel-aviv'
    # numbers_from_web(url)
    # txt_read = read_txt_file('pro.txt')
    send_whatsapp_sheets()
