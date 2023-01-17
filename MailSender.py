#importing required Libraries
import os
import time
import psutil
import urllib.request
import smtplib
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#Function which checks whether the device is connected to internet or not
def is_connected():
    try:
        #Checks random URL by opening it if the connection is there or not
        urllib.request.urlopen("https://www.google.com/",timeout=1)
        return True
    
    except urllib.request.URLError as err:
        return False

#Function to send mail using Python Automation
def MailSender(filename,time):
    try:
        #Enter Sender's mail-id here....
        fromaddr="pralav5848@gmail.com"

        #Enter Receiver's mail-id here....
        toaddr = "pralavphakatkar007@gmail.com"

        #Creating Object
        msg = MIMEMultipart()

        #This will add mail-id into the from and to portion
        msg['From'] = fromaddr
        msg['To']=toaddr

        #This will write content into the body of the mail
        body = """  
        Hello %s,
        Welcome to Python world.
        please find attachment document which contains log of Running Processess
        Log file is created at : %s

        This is auto generated mail.

        Thanks and Regards
        Pralav Phakatkar
        """%(toaddr,time)

        #This will enter your subject of the mail
        Subject="""
        Process Log generated at : %s
        """%(time)

        msg['Subject'] = Subject

        msg.attach(MIMEText(body,'plain'))

        #This is used to attach any file to the mail
        attachment = open(filename,'rb')

        p = MIMEBase("application","octet-stream")

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header("Content-Disposition","attachment; filename= %s"% filename)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com',587)

        s.starttls()

        #This will login to your gmail
        s.login(fromaddr,"yavtttnbhreiqxje")

        text = msg.as_string()

        #This will send the mail with all the content
        s.sendmail(fromaddr,toaddr,text)

        s.quit()

        print("Log file successfully sent through mail")
    
    except Exception as E:
        print("Unable to send mail.",E)