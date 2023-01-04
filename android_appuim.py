import pyautogui
import subprocess
import keyboard
import time
import random
import yaml
# read cred.yaml file
with open(r'C:/Nir/meckano_auto/config.yaml') as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)
print('meckano started')
randint = random.randint(60, 30*60)
print('meckano will run after ' + str(randint/60) + ' minutes')
subprocess.Popen(r'C:\Program Files\BlueStacks_nxt\HD-Player.exe')
# pyautogui.sleep(20)

def send_email(txt='meckano activated'):
    import smtplib

    gmail_user = cfg['gmail_user']
    gmail_password = cfg['gmail_password']

    sent_from = gmail_user
    to = ['nir@shopperai.ai']
    subject = 'meckano activated'
    body = f'Hey, what time {time.ctime()} \n {txt}'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    x = x
    y = y
    print('X =', x, '\nY =', y)

with Listener(on_click=on_click) as listener:
    listener.join()

# click at 3352, 180
pyautogui.click(3352, 180)
pyautogui.sleep(2)
# click at 3182, 423
pyautogui.click(3182, 423)
pyautogui.sleep(2)
# click at 3254, 274
pyautogui.click(3254, 274)
pyautogui.sleep(2)
send_email()
