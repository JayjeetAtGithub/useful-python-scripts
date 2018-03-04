import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
 
fromaddr = "jayjeetchakraborty25@gmail.com"
toaddr = "jcgithub25@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Full Email From Python"
 
body = "Hi i am a full beautiful email from python"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "jpassword25")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
print("email sent")
