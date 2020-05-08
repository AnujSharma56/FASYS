import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

#Enter email address here
fromaddr = ""#configurable

def m_send(tomailaddr):
    toaddr=tomailaddr
    #print(toaddr)
    '''current date and time  '''
    from datetime import date

    today = date.today()

    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    print("d1 =", d1) #date

    from datetime import datetime

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)# time

    



    '''ends '''
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    '''The MimeMultipart class is an implementation of the abstract Multipart class that uses MIME conventions for the multipart data. ... An application can directly construct a MIME multipart object of any subtype by using the MimeMultipart(String subtype) constructor.
    '''
    # storing the senders email address   
    msg['From'] = fromaddr 
    
    # storing the receivers email address  
    msg['To'] = toaddr 
    
    # storing the subject  
    msg['Subject'] = "FASYS : Attendance Report :: "+d1 
    
    # string to store the body of the mail 
    body = "Attachment contains attendance report for \n Date : "+d1+"\n Time : "+current_time+" \n\n Thanks for using FASYS\nAnuj Sharma" 
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    # open the file to be sent  
    filename = "latest.csv"
    attachment = open("/Users/anujsharma/Documents/SIT major project/FINAL GUI/latest.csv", "rb") #path of file
    
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    
    # encode into base64 
    encoders.encode_base64(p) 
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # start TLS for security 
    s.starttls() 
    
    # Authentication 
    #Enter App password here
    s.login(fromaddr, "") #configurable
    
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    
    # terminating the session 
    s.quit() 
