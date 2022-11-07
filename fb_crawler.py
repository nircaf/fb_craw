# selenium-related
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# other necessary ones
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import time
import re

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
browser = webdriver.Chrome(executable_path = r'chromedriver.exe', options=option)#, options=option)

def fb_run():
    EMAIL = "ncafri@gmail.com"
    PASSWORD = "nir159Caf"


    browser.get("http://facebook.com")
    browser.maximize_window()
    wait = WebDriverWait(browser, 30)
    email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
    email_field.send_keys(EMAIL)
    pass_field = wait.until(EC.visibility_of_element_located((By.NAME, 'pass')))
    pass_field.send_keys(PASSWORD)
    pass_field.send_keys(Keys.RETURN)

    time.sleep(5)

    browser.get('https://www.facebook.com/groups/249366278926503/') # once logged in, free to open up any target page

    time.sleep(5)

    from selenium.webdriver.common.action_chains import ActionChains

    Bool_try = True

    while Bool_try:
        try:
            link = browser.find_element(By.XPATH,"//span[contains(text(),'View') and contains(text(),'more comments')]").click() # find the link
            browser.implicitly_wait(10)
            link = browser.find_element(By.XPATH,"//span[contains(text(),'About')]") # find the link
            webdriver.ActionChains(browser).move_to_element(link).perform()

        except:
            Bool_try = False

    link = browser.find_element(By.XPATH,"//*").text

    all_numbers = re.findall(r'\d{10}', link)

    for number in all_numbers:
        number = number[2:]
        number = '9725' + number
        with open("filename.txt", "r+") as file:
            for line in file:
                if number in line:
                    break
            else: # not found, we are at the eof
                file.write(number + '\n') # append missing data

def read_txt_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def send_whatsapp(all_numbers):
    message = 'היי, מה נשמע? אשמח לקבל הצעת מחיר להובלה של מכונת כביסה ותנור מירושלים קומה 1 בלי מעלית לתל אביב קומה 4 עם מעלית. ביום שישי או שבת הקרובים. תודה רבה. '
    for index, number in enumerate( all_numbers):
        # Goes to site
        site = f"https://wa.me/{number}?text={message}"
        browser.get(site)

        browser.find_element(By.XPATH,"//span[contains(text(),'Continue to Chat')]").click()
        time.sleep(5)
        # Clicks on the button
        import pyautogui
        def click_pyautogui(x, y):
            pyautogui.moveTo(x, y)
            pyautogui.click()

        click_pyautogui(1876 , 980)
        time.sleep(5)

if __name__ == '__main__':
    fb_run()
    txt_read = read_txt_file('filename.txt')
    # send_whatsapp(txt_read)
