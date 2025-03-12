'''
Created on 01-Jun-2020
@author: jaspreet
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class Test_Emails:
    def testemailReports(self):
        sender_email = "sachintester1983@gmail.com"
        rec_email = "gillkaurjas797@gmail.com"
        password = "8968585110"
        
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Report for Project"
        msg['From'] = sender_email
        msg['To'] = rec_email
        try:
            text = "Sending some Greetings....."
            filename = "report.html"
            attachment = open("D:\\Jaspreet\\Reports\\"+filename, "rb") 
            img = MIMEBase('application', 'octet-stream')   
            img.set_payload((attachment).read())   
            encoders.encode_base64(img) 
            img.add_header('Content-Disposition', "attachment; filename= %s" %filename)  
            msg.attach(img) 
            
            part1 = MIMEText(text,'plain')
            msg.attach(part1)
            
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, password)
            print("Login success")
            
            server.sendmail(sender_email, rec_email, msg.as_string())
            print("Email sent......")
            server.quit()
        except Exception:
            print("Nothing found to send as mail....")
