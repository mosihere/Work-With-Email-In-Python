# first of all we have to import smtplib module ( simple mail transfer protocol library )

import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587) # call the SMTP function and passing it the domain name of your email provider ( smtp servers )

conn.ehlo() # we call ehlo ( hello ) method just to connect to smtp server.

conn.starttls() # then we start TLS to begin encryption.

conn.login('yourGmail@gmail.com', 'somePassword') # then login method --> this is my app password ( can find in google -> app passwords )


# send mail method to send out the E-mails
conn.sendmail('yourGmail@gmail.com', 'AnEmailYouWantSendMessage@yahoo.com', 'Subject: Hello\n\nDear Moses.\nlong time ago we had met eachOther\n\n I guess you do not know me!\n\nVampire')
# first string is --> Email From ! --> second is Send it to ! --> the third one "Subject:" is necessary too )
conn.close()



# tips Bellow:

# Email Providers and Their SMTP Servers
# Gmail -->  smtp.gmail.com
# Outlook.com/Hotmail.com --> smtp.mail.outlook.com
# Yahoo Mail --> smtp.mail.yahoo.com
# AT&T --> smpt.mail.att.net(port 465)
# Verizon --> smtp.verizon.net(port 465)




# Checking Email Inbox with Python.
# Import imap Client module to access Email inbox
import imapclient
connection = imapclient.IMAPClient('imap.mail.yahoo.com', ssl=True) # we connect to imap domain name with email provider
connection.login('yourEmail@yahoo.com', 'somePassword') # log in to email

connection.select_folder('INBOX', readonly=True) # Select email folder and we use readonly=True to can't delete or modified them


UIDs = connection.search(['ALL']) # This will return a list of Unique ID's that refer to Real Emails
print(UIDs)
print('\n')

rawMessage = connection.fetch([245], ['BODY[]', 'FLAGS']) # here is the raw message that not human readable 
# print(message)


# Import pyzMail module to read email more clearly
import pyzmail
message = pyzmail.PyzMessage.factory(rawMessage[245][b'BODY[]'])
# print(message)

# print('\n')

# print(message.get_subject())

# print('\n')

# print(message.get_address('from'))

# print(message.text_part)
# print(message.html_part)

print(message.text_part.get_payload().decode('UTF-8'))

# Tip bellow:
# Gmail --> imap.gmail.com 
# Outlook.com/Hotmail.com --> imap-mail.outlook.com
# Yahoo Mail --> imap.mail.yahoo.com
# AT&T --> imap.mail.att.net
# Comcast --> imap.comcast.net
# Verizon --> incoming.verizon.net