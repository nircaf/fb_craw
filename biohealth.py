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

# other necessary ones
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import time
import re
# Import the os package
import os

# Import the openai package
import openai

# From the IPython.display package, import display and Markdown
from IPython.display import display, Markdown

# load env
from dotenv import load_dotenv
load_dotenv()
# Set openai.api_key to the OPENAI environment variable
openai.api_key = os.environ["OPENAI"]

def ask_gpt(promt):
    response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[ {"role": "system", 'content': 'answer y or n. one letter answers. email address?'},
                  {"role": "user", "content": promt},
              ]
              )
    res = response["choices"][0]["message"]["content"]
    return res

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
browser = webdriver.Chrome(executable_path = r'chromedriver.exe', options=option)#, options=option)

import tqdm
def fb_run(url= ''):
    browser.get(url)
    # get url.split('.')[1] to get the domain name
    domain_name = url.split('.')[1]
    # browser.maximize_window()
    wait = WebDriverWait(browser, 30)

    href_values = get_links_from_page(browser)

    # get only values with '/company/'
    href_values = [x for x in href_values if '/company/' in x]
    # href_values from 535
    # run tqdm with
    # go to the href values
    for href in tqdm.tqdm(href_values):
        wait = WebDriverWait(browser, 10)
        browser.get(href)
        try:
            href_values2 = get_links_from_page(browser)
            # remove links of [twitter, facebook, linkedin, youtube,volle domain_name]
            href_values2 = [x for x in href_values2 if not any(y in x for y in ['twitter', 'facebook', 'linkedin', 'youtube', domain_name,'volle'])]
            # go to the href values
            for href2 in href_values2:
                wait = WebDriverWait(browser, 10)
                browser.get(href2)
                try:
                    # find email address in link
                    email = re.findall(r'[\w\.-]+@[\w\.-]+', browser.page_source)
                    # remove duplicates from email
                    email = list(dict.fromkeys(email))
                    if len(email) > 0:
                        # add all emails in email to list_emails
                        for e in email:
                            if is_email(e):
                                # write email to file
                                with open(f"{domain_name}.txt", "a") as file:
                                    file.write(e + '\n')
                except:
                    continue
        except:
            continue
    # read file to list_emails
    with open(f"{domain_name}.txt", "r") as file:
        list_emails = file.read().split('\n')
    # remove duplicates from list_emails
    list_emails = list(dict.fromkeys(list_emails))
    # write list_emails to file
    with open(f"{domain_name}.txt", "w") as file:
        for email in list_emails:
            file.write(email + '\n')


import re

def is_email(string):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    http_endings = [
    ".com", ".net", ".org", ".edu", ".gov", ".mil", ".int", ".io", ".co", ".ai", ".app",
    ".biz", ".info", ".me", ".us", ".tv", ".ca", ".uk", ".au", ".in", ".de", ".jp", ".fr",
    ".ru", ".ch", ".it", ".nl", ".se", ".no", ".es", ".pl", ".br", ".mx", ".za", ".nz",
    ".sg", ".kr", ".tr", ".be", ".at", ".dk", ".fi", ".hu", ".cz", ".gr", ".pt", ".ar",
    ".cl", ".co.jp", ".ie", ".cn", ".tw", ".th", ".my", ".vn", ".id", ".il", ".ro", ".bg",
    ".hr", ".sk", ".lt", ".si", ".lv", ".ee", ".rs", ".ba", ".mk", ".is", ".cy", ".lu",
    ".by", ".ua", ".kz", ".md", ".ge", ".am", ".az", ".kg", ".uz", ".tj", ".tm", ".af",
    ".np", ".lk", ".bd", ".pk", ".ir", ".sa", ".ae", ".kw", ".qa", ".om", ".bh", ".ye",
    ".jo", ".lb", ".sy", ".ps", ".kw", ".iq", ".ir", ".tr", ".gr", ".cy", ".dk", ".at"
    # Add more endings here if needed
]
    if re.match(pattern, string) and string.endswith(tuple(http_endings)):
        return True
    else:
        return False

def get_links_from_page(browser):
    # Find all elements with href attribute
    elements = browser.find_elements(By.XPATH,"//a[@href]")
    # Retrieve the href values
    href_values = [element.get_attribute("href") for element in elements]
    return href_values


def read_txt_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def write_num_to_txt(number):
    with open("filename.txt", "r+") as file:
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
    # message = " היי , מה נשמע? ראיתי את המספר שלך בקבוצת דוגווקרים בתל אביב. \
    #     אנחנו גרים על בתל אביב בן אביגדור ומחפשים מישהו שיגיע 2-3 ימים בשבוע בצהריים. הכלב בן שנה וחצי, אנרגטי, ידידותי עם כלבים אחרים. מחפשים לטווח ארוך. "
    # " נשמח לקבל פרטים נוספים אם רלוונטי. תודה רבה! "
    message = """ היי מה נשמע? אשמח אם תוכל לשלוח לי בוואטסאפ הצעת מחיר למעבר של דירת 2 חדרים. מזרן 160,מיטה, שולחן,6 כיסאות, מכונת כביסה, ארון 200על80 וארון 180על60 ואיזור ה20 ארגזים. מקומה 1 עם מעלית בן אביגדור תל אביב
    לקומה 3 עם מעלית בשלמה המלך תל אביב מרחק של 3 קמ. המעבר ביום שישי ה9.6 בבוקר. תודה רבה.
      לא צריך לפרק או להרכיב שום דבר. אני אפרק וארכיב, הכל נכנס למעלית למעט המיטה והמזרן שבגודל 160*200 רק להעביר.  """
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

def sent_emails(txt_read):
    for email in txt_read.split('\n'):
        if email:
            send_email(email)

import yaml
# read yaml cred.yaml
with open('cred.yaml') as f:
    cred = yaml.load(f, Loader=yaml.FullLoader)

def send_email(email_txt):
    import email, smtplib, ssl

    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    subject = "Data Profficiency Request"
    body = f"""Hi.
    \n Thanks, \n Nir"""
    sender_email = cred['email']
    recipients = email_txt
    receiver_email = ", ".join(recipients) if type(recipients) == list else recipients
    password = cred['password']

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # message["Bcc"] = ''  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Add attachment to message and convert message to string
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

import os
import yaml
import base64
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials


def send_emailg(email_txt):
    # Load credentials from the cred.yaml file
    with open('cred.yaml', 'r') as f:
        cred = yaml.safe_load(f)

    # Set up necessary variables
    sender_email = cred['email']
    recipients = email_txt
    receiver_email = ", ".join(recipients) if isinstance(recipients, list) else recipients
    password = cred['password']

    # Create the email message
    message = create_message(sender_email, receiver_email, 'Subject', 'Message body')

    try:
        # Authorize and create the Gmail API service
        credentials = Credentials.from_authorized_user_file('ignore/cred_g.json')
        service = build('gmail', 'v1', credentials=credentials)

        # Send the email
        send_message(service, 'me', message)
        print('Email sent successfully!')
    except HttpError as error:
        print(f'An error occurred: {error}')


def create_message(sender, receiver, subject, message_text):
    message = {
        'raw': base64.urlsafe_b64encode(
            f"From: {sender}\r\n"
            f"To: {receiver}\r\n"
            f"Subject: {subject}\r\n"
            "\r\n"
            f"{message_text}"
        ).decode("utf-8")
    }
    return message


def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        return message
    except HttpError as error:
        print(f'An error occurred: {error}')








if __name__ == '__main__':
    # url = "https://www.iati.co.il/database-search.php?sector=1&medfield=0&category=0&subcategory=0&searchval="
    # fb_run(url)
    txt_read = read_txt_file('iati.txt')
    # run over txt_read
    txt_split = txt_read.split('\n')
    for txt in txt_read.split('\n'):
        # res = ask_gpt(txt)
        if txt:
            # Usage example
            # Call the send_email function with the recipients
            recipients = [txt]
            send_emailg(recipients)
