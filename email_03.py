import smtplib
from email.mime.text import MIMEText

# Set up the email message
msg = MIMEText('Hello, this is a test email! email_03.py')
msg['Subject'] = 'Test Email'
msg['From'] = 'abiroopm2@gmail.com'
msg['To'] = 'abiroopmohan@yahoo.com'

# Connect to the SMTP server
smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server address
smtp_port = 587  # Replace with your SMTP server port
smtp_username = 'abiroopm2@gmail.com'  # Replace with your SMTP username
smtp_password = 'mdisnyytgwpicvvq'  # Replace with your SMTP password
smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_connection.starttls()
smtp_connection.login(smtp_username, smtp_password)

# Send the email message
smtp_connection.sendmail(msg['From'], msg['To'], msg.as_string())

# Disconnect from the SMTP server
smtp_connection.quit()