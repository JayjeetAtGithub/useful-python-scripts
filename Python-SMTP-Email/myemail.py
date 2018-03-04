import smtplib
content = 'This email is from python'
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('jayjeetchakraborty25@gmail.com','jpassword25')
mail.sendmail('jayjeetchakraborty25@gmail.com','jcgithub25@gmail.com',content)
mail.quit()
print("email sent")
