import smtplib

def send_email(to, subject, body):
    # Configure your email service provider and account details
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "your-email@gmail.com"
    password = "your-password"

    # Login to your email account
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)

        # Compose and send your email
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, to, message)

# Send a notification email
to = "recipient-email@example.com"
subject = "New job application response"
body = "A new job application response has been received. Check your LinkedIn account for details."
send_email(to, subject, body)
