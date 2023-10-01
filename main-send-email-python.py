import smtplib
import ssl
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_scheduled_email(to, subject, body, gmail_user, gmail_password, num_emails):

    # Get input for the date and time components
    year = int(input("Enter the year to send the emails: "))
    month = int(input("Enter the month to send the emails: "))
    day = int(input("Enter the day to send the emails: "))
    hour = int(input("Enter the hour to send the emails: "))
    minute = int(input("Enter the minute to send the emails: "))
    second = int(input("Enter the second to send the emails: "))


    # Create the message to be sent
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = gmail_user
    message["To"] = to
    message.attach(MIMEText(body, "plain"))

    # Convert the date components to a Unix timestamp
    scheduled_time = time.mktime((year, month, day, hour, minute, second, 0, 0, -1))
    current_time = time.time()
    time_difference = scheduled_time - current_time

    # Wait until it's time to send the emails
    time.sleep(time_difference)

    # Send the emails
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(gmail_user, gmail_password)
        for i in range(num_emails):
            server.sendmail(gmail_user, to, message.as_string())


def send_instant_mail(to, subject, body, gmail_user, gmail_password):
    # Create the message to be sent
    message = MIMEMultipart()
    message["Subject"] = subject 
    message["From"] = gmail_user
    message["To"] = to
    message.attach(MIMEText(body, "plain"))


    # Send the emails
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(gmail_user, gmail_password)
        for i in range(num_emails):
            server.sendmail(gmail_user, to, message.as_string())

    
    



# Scheduled or Instant
sori = input("Do you want a (S)cheduled mail or an (I)nstant mail? (S/I)").upper()


# Gmail account credentials
gmail_user = #YOUR EMAIL ID
gmail_password = #YOUR GOOGLE APP PASSWORD(GO TO SECURITY>TWO FACTOR AUTHENTICATION>APP PASSWORDS AND CREATE A NEW APP)

# Recipient email address
to = input("Please enter the reciever's Gmail address: ")

# Message to be sent
subject = input("Please enter the subject: ")
body = input("Please enter the body: ")



# Number of emails to send at the scheduled time
num_emails = int(input("Enter the number of emails to send: "))


if sori == "S":
    send_scheduled_email(to, subject, body, gmail_user, gmail_password, num_emails)

elif sori == "I":
    send_instant_mail(to, subject, body, gmail_user, gmail_password)

else:
    print("Invalid Input")
    

print("Emails sent!")
