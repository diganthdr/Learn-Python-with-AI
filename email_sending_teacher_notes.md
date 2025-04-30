
# 📧 Sending Emails with Python - Teacher Notes

## 🕰️ A Brief History of Emails
- **1971**: The first email was sent by Ray Tomlinson across ARPANET.
- **1990s**: Emails became popular with the rise of the internet.
- **Today**: Billions of emails are sent daily for communication, marketing, security alerts, etc.

Email is still one of the most reliable, standard, and professional ways of communication.

---

# 🧠 What Students Will Learn Today

## Basics of Email
- What is SMTP (Simple Mail Transfer Protocol)
- Understanding ports: 25, 465 (SSL), and 587 (TLS)
- Email servers (Gmail, Outlook, Yahoo)

## Python Libraries
- Using `smtplib`
- Using `email` library to format emails

## Flow of Sending an Email

```mermaid
flowchart TD
    A[Compose Email (Python Code)] --> B[Connect to SMTP Server]
    B --> C[Login with Username and Password]
    C --> D[Send Email using Server]
    D --> E[Server Delivers to Recipient]
```

---

# ✍️ Code Snippets

## 1. Sending a Simple Email using Gmail SMTP

```python
import smtplib
from email.message import EmailMessage

# Create an EmailMessage object
msg = EmailMessage()
msg.set_content("Hello, this is a test email sent from Python!")
msg['Subject'] = 'Test Email from Python'
msg['From'] = 'your_email@gmail.com'
msg['To'] = 'recipient_email@gmail.com'

# Gmail SMTP server details
smtp_server = 'smtp.gmail.com'
port = 587

# Login credentials
your_email = 'your_email@gmail.com'
your_password = 'your_app_password'  # App password, not your main password

# Send the email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(your_email, your_password)
    server.send_message(msg)

print("✅ Email sent successfully!")
```

> ⚡ **Important:** Enable "Less secure app access" or create "App Password" in Gmail Settings.

---

# 🎯 Hands-On Assignment for Students

## 🧩 Part 1 - Modify the Email
- Change subject line.
- Change email body content.
- Send the email to yourself.

## 🧩 Part 2 - Send Multiple Emails
- Create a list of recipients.
- Loop through and send emails one by one.

### Bonus Challenge 💬
- Format the email body to include HTML (e.g., bold, headings).
- Attach a simple text file to the email.

---

# 📘 Resources
- [Official Python smtplib docs](https://docs.python.org/3/library/smtplib.html)
- [Email library docs](https://docs.python.org/3/library/email.message.html)
