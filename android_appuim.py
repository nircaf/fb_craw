import pyautogui
import subprocess
import keyboard
import time
import random
import yaml
import mss
from pynput import mouse

pyautogui.PAUSE = 2
# #sleep for 2 seconds
# pyautogui.sleep(2)
# read cred.yaml file
with open(r'C:/Nir/meckano_auto/cred.yaml') as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)
print('meckano started')
randint = random.randint(60, 30*60)
print('meckano will run after ' + str(randint/60) + ' minutes')
# time.sleep(randint) #inclucive
subprocess.Popen([r'C:\Program Files\BlueStacks_nxt\HD-Player.exe', '--instance', 'Nougat32', '--cmd', 'launchApp', '--package', 'com.kfir.Meckano'])
pyautogui.sleep(20)


def send_email(filenam,txt='meckano activated'):
    import email, smtplib, ssl

    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    gmail_user = cfg['gmail_user']
    password = cfg['gmail_password']

    sender_email = gmail_user
    subject = 'meckano activated'
    body = f'Hey, what time {time.ctime()} \n {txt}'
    recipients = ["nir@shopperai.ai"]
    receiver_email = ", ".join(recipients)
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # message["Bcc"] = ''  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = f"{filenam}"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

# Press the F11
pyautogui.press('f11')
print('meckano full screen')
# pyautogui pause 3 sec
time.sleep(2)
# log in/out
# click 3 times
pyautogui.click(1000,300,button='left', clicks=3, interval=0.25)
print('meckano logged in')
# sleep
time.sleep(2)

# take screenshot
# Save the screenshot as a PNG file
name_png = 'screenshot.png'



with mss.mss() as sct:
    monitor = {"top": 100, "left": 500, "width": 1000, "height": 500, "mon": 1}
    # Grab the data
    sct_img = sct.grab(monitor)
    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=name_png)
# sleep

time.sleep(2)
send_email(name_png)
print('meckano screenshot sent')
