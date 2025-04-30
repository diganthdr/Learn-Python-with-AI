import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    sender_email = "bitsandbytes01000100@gmail.com"
    sender_password = "qkmbwpidipqchevi"  # Use the App Password here
    recipient_email = "diganth@gmail.com"  # Replace with the recipient's email

    # Create the email
    subject = "Test Email"
    body = "This is a test email sent from Python."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Upgrade the connection to secure
        server.login(sender_email, sender_password)  # Log in to your Gmail account
        server.sendmail(sender_email, recipient_email, msg.as_string())  # Send the email
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    send_email()