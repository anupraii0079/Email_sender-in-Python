from email.message import EmailMessage
import ssl     #secure socket layrer
import smtplib #Simple Mail Transfer protocol


email_sender = 'sender_email@gmail.com'
email_password = 'password'  #which you will be create from your gmail ---> security---> on Two step verification ---> password ---> generate code

email_receiver = 'reciever_email@gmail.com'

subject = "Make more Projects"

body = """
      Making more projects sharp your programming skill and make 
      your resume more valuable 

"""

em = EmailMessage()
em['From'] = email_sender 
em['To'] = email_receiver
em['subject'] = subject 
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
