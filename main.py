import smtplib
from datetime import datetime
import random

with open("quotes.txt") as file:
    quotes_list = file.readlines()
    # print(quotes_list)

date = datetime.now()
now = date.weekday()
# print(type(now))


if now == 1:
    my_email = "YOUR EMAIL"
    password = "YOUR PASS"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="abdullah.mustafa11221@gmail.com",
                            msg=f"Subject: Motivation by python me\n\n {random.choice(quotes_list)}")
