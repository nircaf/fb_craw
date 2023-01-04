import pyautogui
import subprocess
import keyboard
import time
import random
import yaml
import mss


# Press the Enter key
pyautogui.press('enter')
#sleep for 2 seconds
pyautogui.sleep(2)
# Type the digits "123321456"
pyautogui.typewrite('123321456')
# Press the Enter key
pyautogui.press('enter')
# read cred.yaml file
with open(r'C:/Nir/meckano_auto/cred.yaml') as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)
print('meckano started')
randint = random.randint(60, 30*60)
print('meckano will run after ' + str(randint/60) + ' minutes')
# time.sleep(randint) #inclucive
subprocess.Popen(r'C:\Program Files\BlueStacks_nxt\HD-Player.exe')
pyautogui.sleep(20)

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

# get in the app
# click at 3352, 180
pyautogui.click(3352, 180)
pyautogui.sleep(5)
# press on new shift
# click at 3182, 423
pyautogui.click(3182, 423)
pyautogui.sleep(5)
# log in/out
# click at 3254, 274
# pyautogui.click(3254, 274)
# pyautogui.sleep(5)
# take screenshot
# Save the screenshot as a PNG file

name_png = 'screenshot.png'

with mss.mss() as sct:
    monitor = {"top": 100, "left": 3000, "width": 1000, "height": 500, "mon": 2}
    # Grab the data
    sct_img = sct.grab(monitor)
    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=name_png)

send_email(name_png)
# lock the computer
pyautogui.hotkey('win', 'l')
