#!/usr/bin/env python
# coding: utf-8

# In[8]:

import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

#set msg by calling multipart 
msg=MIMEMultipart()

body="Documents"

#to attach msg with plain

msg.attach(MIMEText(body, 'plain'))
filename="new.txt"

#open the file in location
attachment=open(r"C:\Users\Maddy\Desktop\new.txt","rb") 
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)

#add header with filename
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)

mail=smtplib.SMTP("smtp.gmail.com",587)

#mail starts with ehlo.
mail.ehlo()
mail.starttls()

#login id with password 
mail.login("loginid@gmail.com","password")

#mail sent from id to another id
mail.sendmail("loginid@gmail.com","receiverid@gmail.com",msg.as_string())

#mail is quit from that id
mail.quit()
