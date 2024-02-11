import pyautogui
import subprocess
import keyboard
import time
import random
import yaml
import mss
from pynput import mouse
import openai
import os
from dotenv import load_dotenv
# read cred.yaml file
with open(r'cred.yaml') as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)

openai.api_key = os.getenv("OPENAI_API_KEY")


def send_email(filenam,txt='meckano activated',email_address=cfg['gmail_user']):
    import email, smtplib, ssl

    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    gmail_user = cfg['gmail_user']
    password = cfg['gmail_password']

    sender_email = gmail_user
    subject = 'Data Science Position Inquiry'
    body = f"""Hi {txt},

Einat connected between us regarding the Data Scientist position.
My name is Nir and I have almost 3 years of experience as a Data Scientist in hightech.
I have a B.Sc from Ben-Gurion University and soon a M.Sc from Tel Aviv University including presentation of research at international conferences.
I have experience with Stack: ML, DL, Python, Pytocrch, Tensorflow, Pandas & Numpy, AWS, Git and more, and experience working with tabular data, NLP and CV.

Attached is my CV. Thank you, Nir.
    """
    recipients = [email_address]
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

def run_prompt(prompt):
    # response = openai.Completion.create(
    #     engine="text-curie-001",
    #     prompt=prompt,
    #     temperature=0.9,
    #     max_tokens=250,
    #     top_p=1,
    #     frequency_penalty=0.0,
    #     presence_penalty=0.0,
    #     stop=['!@#']
    # )
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "assistant", "content": prompt}],
        temperature=0.5
        )
    return response

str_emails = """
Sagi BacharView Sagi Bachar’s profile
 • 1st
Talent Acquisition Manager at StartingUP ★ Global Sourcing Specialist 🎯 HR Consulting ★ LinkedIn Expert ★ Tech-Savvy ★ Life-Long Learner ★ Personalization Advocate
1w
יש לי אולי משרה סופר מרתקת ומיוחדת בתחום הdigital healthcare. אשמח שתשלחי פה בהודעה פרטית את הCV שלו או למייל sagi@startingup.io 
See translationSee translation of this comment

Like
like
1

Reply
1 Reply
1 Comment on Sagi Bachar’s comment


Einat BorohovichView Einat Borohovich’s profile
Author
Senior Data Scientist at Rambam Health Care Campus
1w
היי שגיא, נשמע מעולה!
תודה רבה על השיתוף.
הוא כתב לך בפרטי.
בהצלחה!
See translationSee translation of this comment

Like
support
1

Reply


Haddassah SkurnikView Haddassah Skurnik’s profile
 • 2nd
Head of Development Team at BUSOFT
1w
לי hadasa@busoft.co.il

Like
like
1

Reply
2 Replies
2 Replies on Haddassah Skurnik’s comment


Einat BorohovichView Einat Borohovich’s profile
Author
Senior Data Scientist at Rambam Health Care Campus
1w
היי הדסה , תודה רבה על ההתייחסות. הוא כתב לך בפרטי. בהצלחה!
See translationSee translation of this comment

Like
like
1

Reply


Haddassah SkurnikView Haddassah Skurnik’s profile
 • 2nd
Head of Development Team at BUSOFT
6d
מעולה!
See translationSee translation of this comment

Like

Reply


Hila Rubin הילה רוביןView Hila Rubin הילה רובין’s profile
 • 2nd
Your Relationship coach 🔶 I will help you achieve a happy and healthy relationship | emotional well-being | self esteem and self awareness 🔶 Couples and individual counseling & mentoring 🔶 Dating coach
1w
היי מוזמנת להעביר למייל 
gabyr@final.co.il זה בעלי והוא עובד בחברת פיינל שהיא חברה מדהימה מכל הבחינות!! בעלי שם כבר 13 שנה!! יכולה גם להעביר אליי בפרטי פה ואעביר לו. מה שנוח לך! 
המון בהצלחה!!! Einat Borohovich
See translationSee translation of this comment

Like
like
2

Reply
2 Replies
2 Replies on Hila Rubin הילה רובין’s comment


Einat BorohovichView Einat Borohovich’s profile
Author
Senior Data Scientist at Rambam Health Care Campus
1w
היי הילה, תודה רבה על ההתייחסות והחיבור. הוא כתב לך בפרטי.
See translationSee translation of this comment

Like

Reply


Hagai LugerView Hagai Luger’s profile
 • 2nd
I Develop Developers
5d
וואו. מאחל לו שיתקבל
חברה של גאונים
See translationSee translation of this comment

Like

Reply


Dan DanielView Dan Daniel’s profile
 • 2nd
VP R&D - We are hiring!
1w
Elik Sror Nofar Siedlaz
מוזמן לבוא לעבוד עם הטובים ביותר.
בהצלחה!
See translationSee translation of this comment

Like
like
3

Reply
3 Replies
3 Replies on Dan Daniel’s comment

Load previous repliesLoad previous replies on Dan Daniel’s comment

Einat BorohovichView Einat Borohovich’s profile
Author
Senior Data Scientist at Rambam Health Care Campus
1w
Nofar Siedlaz היי נופר, תודה רבה על ההתייחסות. הוא כתב לך בפרטי.
See translationSee translation of this comment

Like
like
1

Reply


Anat LaviView Anat Lavi’s profile
 • 2nd
Sourcing & Recruiting expert✨People person ✨Recriuting experts for Hi Tech companies, Startups & Stealth mode🦄 Always looking for Backend & Frontend & Data Engineers 🦄 jobsethr@gmail.com
1w
אשמח לקבל jobsethr@gmail.com
See translationSee translation of this comment

Like
like
1

Reply
1 Reply
1 Comment on Anat Lavi’s comment


Einat BorohovichView Einat Borohovich’s profile
Author
Senior Data Scientist at Rambam Health Care Campus
1w
היי ענת , תודה רבה על ההתייחסות. הוא כתב לך בפרטי. בהצלחה!
See translationSee translation of this comment

Like

Reply


Yael KiselmanView Yael Kiselman’s profile
 • 2nd
Data Scientist, Digital Turbine
1w
נפתחה אצלינו משרה בדיגיטל טורביין. מוזמן להגיש :) 
yael.kiselman@digitalturbine.com
See translationSee translation of this comment

Like
like
1

Reply
1 Reply
1 Comment on Yael Kiselman’s comment


Einat BorohovichView Einat Borohovich’s profile
Author
Senior Data Scientist at Rambam Health Care Campus
1w
היי יעל , תודה רבה על ההתייחסות. הוא כתב לך בפרטי. בהצלחה!
See translationSee translation of this comment

Like

Reply


Tslil GabayView Tslil Gabay’s profile
 • 2nd
Talent Acquisition Recruiter at Rafael Advanced Defense Systems
1w
 היי :) נפתחה לי משרת דאטה סיינטיסט אצלנו ברפאל. באם רלוונטי עבורו לעבוד בצפון אני יותר מאשמח לקבל את קורות החיים ולשוחח איתו. tslilgab@rafael.co.il
See translationSee translation of this comment

Like
like
1

Reply
1 Reply
1 Comment on Tslil Gabay’s comment


Einat BorohovichView Einat Borohovich’s profile
Author
Senior Data Scientist at Rambam Health Care Campus
1w
היי צליל , תודה רבה על ההתייחסות. הוא כתב לך בפרטי. בהצלחה!
See translationSee translation of this comment

Like

Reply


Lior TaboriView Lior Tabori’s profile
 • 2nd
Data Scientist & Economist @ Intuit
1w
אשמח לקבל :)
See translationSee translation of this comment

Like
like
1

Reply
1 Reply
1 Comment on Lior Tabori’s comment


Einat BorohovichView Einat Borohovich’s profile
Author
Senior Data Scientist at Rambam Health Care Campus
1w
היי ליאור, תודה רבה על ההתייחסות. הוא כתב לך בפרטי. בהצלחה!
See translationSee translation of this comment

Like

Reply


Or EllaView Or Ella’s profile
 • 2nd
Software Engineer at PLAYSTUDIOS
1w
אשמח ore@playstudios-il.com 

Like
like
1

Reply
1 Reply
1 Comment on Or Ella’s comment


Einat BorohovichView Einat Borohovich’s profile
Author
Senior Data Scientist at Rambam Health Care Campus
1w
היי אור, תודה רבה על ההתייחסות. הוא כתב לך בפרטי. בהצלחה!
See translationSee translation of this comment

Like

Reply

Status is online
Ifat Kahan יפעת קהןView Ifat Kahan יפעת קהן’s profile
 • 2nd
Employer Brand Leader and Talent Acquisition Partner ★Innovative Thinker ★ Data is your passion? Join us
1w
היי אשמח לקורות חיים ifat.kahan@g-stat.com
See translationSee translation of this comment

Like
like
1

Reply
1 Reply
1 Comment on Ifat Kahan יפעת קהן’s comment


Einat BorohovichView Einat Borohovich’s profile
Author
Senior Data Scientist at Rambam Health Care Campus
1w
היי יפעת , תודה רבה על ההתייחסות. הוא כתב לך בפרטי. בהצלחה!
See translationSee translation of this comment

Like

Reply


Eden Zaryan ☁️View Eden Zaryan ☁️’s profile
 • 2nd
HR and Recruiting Manager At Direct Experts - ⭐I'm hiring IT, Cloud & Devops, Cyber Security, Data & AI ⭐ 18K Followers
1w
לי eden@direct-ex.co.il

Like
like
1

Reply
1 Reply
1 Comment on Eden Zaryan ☁️’s comment


Einat BorohovichView Einat Borohovich’s profile
Author
Senior Data Scientist at Rambam Health Care Campus
1w
היי עדן , תודה רבה על ההתייחסות. הוא כתב לך בפרטי. בהצלחה!
See translationSee translation of this comment

Like

Reply


Iyar LinView Iyar Lin’s profile
 • 2nd
Data science lead at Loops
1w
אני אשמח.
iyarl@getloops.ai

Like
like
1

Reply
1 Reply
1 Comment on Iyar Lin’s comment


Einat BorohovichView Einat Borohovich’s profile
Author
Senior Data Scientist at Rambam Health Care Campus
1w
היי אייר , תודה רבה על ההתייחסות. הוא כתב לך בפרטי. בהצלחה!
See translationSee translation of this comment

Like

Reply

Status is reachable
Lahav AraratView Lahav Ararat’s profile
 • 2nd
Data Analyst | Business Analyst | Enjoys SQL and Tableau | 📈 Data to Insights in 3 Steps 💡 | People Lover
1w
נשמע 🔥

Like
like
1

Reply
1 Reply
1 Comment on Lahav Ararat’s comment


Einat BorohovichView Einat Borohovich’s profile
Author
Senior Data Scientist at Rambam Health Care Campus
1w
אלוף הפרגונים שאתה! איזה תותח! תודה רבה 🙏🏻🙏🏻🙏🏻
See translationSee translation of this comment

Like

Reply


Orr InbarView Orr Inbar’s profile
 • 2nd
Co-Founder & CEO at QuantHealth
1w
אשמח לקבל קוח, נפתחו אצלנו כמה משרות דטה סיינס בתחום הרפואה
See translationSee translation of this comment

Like
like
1

Reply
1 Reply
1 Comment on Orr Inbar’s comment


Einat BorohovichView Einat Borohovich’s profile
Author
Senior Data Scientist at Rambam Health Care Campus
1w
היי אור , תודה רבה על ההתייחסות. הוא כתב לך בפרטי. בהצלחה!
See translationSee translation of this comment

Like

Reply


Oren KochanskyView Oren Kochansky’s profile
 • 2nd
R&D Group Leader
1w
Oren.k@taboola.com

Like
like
1

Reply
1 Reply
1 Comment on Oren Kochansky’s comment


Einat BorohovichView Einat Borohovich’s profile
Author
Senior Data Scientist at Rambam Health Care Campus
1w
היי אורן, תודה רבה על ההתייחסות. הוא כתב לך בפרטי.
See translationSee translation of this comment

Like

Reply


Eyal Deri 🚀View Eyal Deri 🚀’s profile
 • 2nd
The Problem Solver, 🍒Operation Manager, Project Manager, 🤿🏋🏻‍♀️Personal branding, 🫡Ex-Ranger-Manager Nature and Parks Authority, 🚲Founder, Reserve Service as officer, Marketing Manager
1w
בהצלחה גדולה 🚀 Einat Borohovich
See translationSee translation of this comment

Like
like
1

Reply
1 Reply
1 Comment on Eyal Deri 🚀’s comment


Einat BorohovichView Einat Borohovich’s profile
Author
Senior Data Scientist at Rambam Health Care Campus
1w
תודה רבה 🙏🏻
See translationSee translation of this comment

Like

Reply


Shiri Eyal HabaView Shiri Eyal Haba’s profile
 • 2nd
Senior Manager, Site Reliability Engineering
6d
אשמח לקורות חיים shaba@akamai.com
See translationSee translation of this comment

Like

Reply


Tomer WikinskiView Tomer Wikinski’s profile
 • 2nd
Co-Managing Director, consultants & projects at LOG-ON
6d
אשמח
linkedin@log-on.com

Like

Reply

Status is online
Yuval LeshemView Yuval Leshem’s profile
 • 2nd
YUVAL LESHEM MBA |CEO:HR DIRECTOR:PMO:PMO:R&D| MES, OEM, PLM, TK, NPI, PMO, CP, CAD, CO.FOUNDING, START-UPS, MONETIZATIO, MEDICINE IND RESEEARCH. |36,000+Members| Hot Jobs 24/7.
6d
משרות בחברות סטארטאפ בהייטק ובתעשייה
השירות חופשי ללא תשלום למועסקים ולמעסיקים כתרומה לקהילה
https://www.linkedin.com/groups/1543497/
See translationSee translation of this comment

Like

Reply


Orit AzarzarView Orit Azarzar’s profile
 • 2nd
VP HR | Trusted advisor | Culture builder | People & impact | Creator| Trailblazer
1w
היי, אשמח! תודה רבה על השיתוף 
Orit@dream-security.com Tal Fialkow Ofir Shamay
See translationSee translation of this comment

Like
like
1

Reply


Hili ParyentiView Hili Paryenti’s profile
 • 2nd
Backend Developer & Squad Lead @Unity | Former 8200 | Data enthusiast
6d
אהלן! אני יכולה לבדוק אם יש אצלנו משרות רלוונטיות פתוחות (יוניטי איירוןסורס לשעבר) אפשר לשלוח קוח לhili.paryenti@unity3d.com
See translationSee translation of this comment

Like

Reply


Yonatan MizrahiView Yonatan Mizrahi’s profile
 • 3rd+
System Administrator
1w
אשמח לנסות לעזור
jyoni84@gmail.com
See translationSee translation of this comment

Like

Reply


Avishai Friedman - I'm HiringView Avishai Friedman - I'm Hiring’s profile
 • 2nd
Ceo blueprint software
6d
הי אשמח לקבל את קורות החיים שלך
Avishai@bpsoft.co.il
See translationSee translation of this comment

Like

Reply


Adi BarView Adi Bar’s profile
 • 2nd
Head-hunting services
6d
אשמח :) adibar.hr@gmail.com
"""
import re
# get email addresses from str_emails
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str_emails)
# run over emails
for email in emails:
    # remove any non english chars
    email = re.sub(r'[^\x00-\x7F]+', ' ', email)
    # get first part of email address
    name = email.split('@')[0]
    # get from gpt the name of the person
    promt = f'return only the name from the string "{name}" first letter uppercase'
    response = run_prompt(promt)
    try:
        name_fixed = response['choices'][0]['message']['content']
    except:
        continue
    send_email('Nirs Resume.pdf',name_fixed,email)
