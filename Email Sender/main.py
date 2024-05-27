import smtplib
import datetime as dt
import random

MY_EMAIL = "dhruv20030621@gmail.com"
MY_PASSWORD = "Dhruv@2106"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readline()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Monday Motivation\n\n{quote}")

# import smtplib
#
# my_email = "dhruv20030621@gmail.com"
# password = "pbhi atan insd nwyd"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="dhruv210603@yahoo.com", msg="Hello")
