import smtplib

# Enter user gmail account
# In order to be able to send from python you need to allow less secure apps through the account settings in gmail.
# insert sender's email (Replace astericks)
gmailaccount = '*****'
# Enter sender's password (Replace astericks)
gmailpassword = '*************'

# Enter recipients email
sentfrom = gmailaccount
# enter recepients email (Replace astericks)
to = ['***']
subject = 'This is my favorite class of the semester!'
body = 'Python Programming'

# Email Functionality
emailtext = """\
From: %s
To: %s
Subject: %s

%s
""" % (sentfrom, ", ".join(to), subject, body)

# Creating SMTP connection
try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmailaccount, gmailpassword)
    smtp_server.sendmail(sentfrom, to, emailtext)
    smtp_server.close()

    #Print whether send was successful
    print ("Email sent successfully!")
except Exception as ex:
    print ("Email was not successfully sent.",ex)
